seia_sql_geom = """SELECT * 
FROM (
	SELECT DISTINCT  
		pa.ide_processo_ato 
	,	aa.nom_ato_ambiental
	,	tspa.nom_tipo_status_processo_ato AS status_ato
	,	p2.num_portaria
	,	p2.dtc_publicacao_portaria
	,	spa.num_prazo_validade AS validade_anos
	,	DATE(p2.dtc_publicacao_portaria) +(spa.num_prazo_validade||' year')::INTERVAL AS dtc_prazo_validade
	,	p.num_processo 
	,	r.num_requerimento
	,	CASE
			WHEN pes.ide_pessoa = pf.ide_pessoa_fisica THEN pf.nom_pessoa
			ELSE pj.nom_razao_social
		END AS nome_requerente
	,	CASE
			WHEN pes.ide_pessoa = pf.ide_pessoa_fisica THEN pf.num_cpf
			ELSE pj.num_cnpj
		END AS cpf_cnpj_requerente
	,	a.nom_area AS area_da_analise 
	,	fa1.num_area_supressao AS Requer_area_tot_supres_ha
	,	fa1.num_area_app AS Requer_supres_app_ha
	,	fa1.num_area_suprimida AS Requer_supres_app_percent_tot_empreendimento -- percentual relacionado ao valor de area do empreendimento como um todo (somatorio de todos imoveis)
	,   (select SUM(esa.volume_total_em_app) from especie_supressao_autorizacao esa where esa.ide_fce_asv = fa1.ide_fce_asv) as Requer_vol_tot_em_app
	,   (select SUM(esa.volume_total_fora_app) from especie_supressao_autorizacao esa where esa.ide_fce_asv = fa1.ide_fce_asv) as Requer_vol_tot_fora_app
	,	fa2.num_area_supressao AS Conced_area_tot_supres_ha
	,	fa2.num_area_app AS Conced_supres_app_ha
	,	fa2.num_area_suprimida AS Conced_supres_app_percent_tot_empreendimento
	,   (select SUM(esa.volume_total_em_app) from especie_supressao_autorizacao esa where esa.ide_fce_asv = fa2.ide_fce_asv) as Conced_vol_tot_em_app
	,   (select SUM(esa.volume_total_fora_app) from especie_supressao_autorizacao esa where esa.ide_fce_asv = fa2.ide_fce_asv) as Conced_vol_tot_fora_app
	------------------------------------- comeco da espacializacao ("teoricamente")
	,	estado.des_sigla AS estado_uf
	,	m.nom_municipio
	,	m.cod_ibge_municipio
	,	e.ide_empreendimento
	,	e.nom_empreendimento AS nome_empreendimento
	,	ie.ide_imovel
	,	CASE
		WHEN ie.ide_imovel = (SELECT ide_imovel FROM imovel WHERE ide_imovel = ie.ide_imovel AND ide_tipo_imovel = 3) THEN 'CessÃ£o'
		WHEN ie.ide_imovel = (SELECT ide_imovel FROM imovel WHERE ide_imovel = ie.ide_imovel AND ide_tipo_imovel = 2) THEN 'Urbano'
		WHEN ie.ide_imovel = (SELECT ide_imovel FROM imovel WHERE ide_imovel = ie.ide_imovel AND ide_tipo_imovel = 1) THEN 'Rural'
		END AS tipo_vinculo
	,	(SELECT num_sicar FROM imovel_rural_sicar irs WHERE irs.ide_imovel_rural = ie.ide_imovel) AS num_sicar
	,	pac.ide_localizacao_geografica AS ide_loc_PAC
	,	csg.nom_classificacao_secao AS tipo_geom_PAC
	,	sc.srid || ' || ' || sc.nom_sistema_coordenada AS sist_ref
	,	CASE 
			WHEN csg.nom_classificacao_secao = 'Ponto' THEN pac.val_atividade -- quando ponto, tecnico insere manualmente portanto pac.val_atividade parece estar sem erros
			ELSE CASE 
					WHEN sc.srid IN ('31983') THEN st_area(st_transform(dg.the_geom,31983))/10000
					WHEN sc.srid IN ('31984') THEN st_area(st_transform(dg.the_geom,31984))/10000
					WHEN sc.srid IN ('29193') THEN st_area(st_transform(dg.the_geom,29193))/10000
					WHEN sc.srid IN ('29194') THEN st_area(st_transform(dg.the_geom,29194))/10000
					ELSE st_area(st_transform(dg.the_geom,31983))/10000 -- Conversao considerando menor desvio para UTM 23S (Foco: Cerrado)
				END::NUMERIC(10, 4)
		END AS area_concedida_por_imovel
--	,	st_x(st_centroid(dg.the_geom)) AS longitude
--	,	st_y(st_centroid(dg.the_geom)) AS latitude
	,   dg.the_geom AS geom
	FROM processo p 
	INNER JOIN requerimento r ON r.ide_requerimento = p.ide_requerimento
	INNER JOIN controle_tramitacao ct  ON ct.ide_processo = p.ide_processo 
			AND ct.ide_controle_tramitacao = (
				SELECT MAX(ide_controle_tramitacao) FROM controle_tramitacao WHERE controle_tramitacao.ide_processo = p.ide_processo )
	LEFT JOIN controle_tramitacao ct_a ON ct_a.ide_processo = p.ide_processo
			AND ct_a.ide_controle_tramitacao = (
				SELECT MAX(ide_controle_tramitacao) FROM controle_tramitacao WHERE controle_tramitacao.ide_status_fluxo = 6 AND controle_tramitacao.ide_processo = p.ide_processo )
	LEFT JOIN area a ON a.ide_area = ct_a.ide_area 
	LEFT JOIN portaria p2 ON p2.ide_processo = p.ide_processo
	LEFT JOIN processo_ato pa ON pa.ide_processo = p.ide_processo 
	LEFT JOIN ato_ambiental aa ON aa.ide_ato_ambiental = pa.ide_ato_ambiental 
	LEFT JOIN status_processo_ato spa ON spa.ide_processo_ato = pa.ide_processo_ato
			AND spa.ide_status_processo_ato = (
				SELECT MAX(ide_status_processo_ato) FROM status_processo_ato WHERE status_processo_ato.ide_processo_ato = pa.ide_processo_ato )
	LEFT JOIN tipo_status_processo_ato tspa ON tspa.ide_tipo_status_processo_ato = spa.ide_tipo_status_processo_ato
	INNER JOIN empreendimento_requerimento er ON er.ide_requerimento = r.ide_requerimento
	INNER JOIN empreendimento e ON e.ide_empreendimento = er.ide_empreendimento
	LEFT JOIN imovel_empreendimento ie ON ie.ide_empreendimento = e.ide_empreendimento
	LEFT JOIN processo_ato_concedido pac ON pac.ide_processo_ato = pa.ide_processo_ato 
			AND pac.ide_imovel = ie.ide_imovel 
	LEFT JOIN localizacao_geografica lg ON lg.ide_localizacao_geografica = pac.ide_localizacao_geografica
	LEFT JOIN classificacao_secao_geometrica csg ON csg.ide_classificacao_secao = lg.ide_classificacao_secao
	LEFT JOIN dado_geografico dg ON dg.ide_localizacao_geografica = pac.ide_localizacao_geografica
	LEFT JOIN sistema_coordenada sc ON sc.ide_sistema_coordenada = lg.ide_sistema_coordenada
	--LEFT JOIN imovel_rural ir ON ir.ide_imovel_rural = ie.ide_imovel
	INNER JOIN requerimento_pessoa rp ON r.ide_requerimento = rp.ide_requerimento AND rp.ide_tipo_pessoa_requerimento = 1
	INNER JOIN pessoa pes ON	(rp.ide_pessoa = pes.ide_pessoa)
	LEFT JOIN pessoa_fisica pf ON pf.ide_pessoa_fisica = pes.ide_pessoa 
	LEFT JOIN pessoa_juridica pj ON pj.ide_pessoa_juridica = pes.ide_pessoa 
	LEFT JOIN fce f1 ON f1.ide_requerimento = r.ide_requerimento -- Dados requeridos [Alfanumericos]
			AND f1.ide_fce = (
				SELECT ide_fce FROM fce WHERE fce.ide_requerimento = r.ide_requerimento AND fce.ide_origem_fce = 1 AND fce.ide_documento_obrigatorio = 2000 )
	LEFT JOIN fce f2 ON f2.ide_requerimento = r.ide_requerimento -- Dados concedidos [Alfanumericos]
			AND f2.ide_fce = (
				SELECT ide_fce FROM fce WHERE fce.ide_requerimento = r.ide_requerimento AND fce.ide_origem_fce = 2 AND fce.ide_documento_obrigatorio = 2000 )
	LEFT JOIN fce_asv fa1 ON fa1.ide_fce = f1.ide_fce -- Dados requeridos [Alfanumericos]
	LEFT JOIN fce_asv fa2 ON fa2.ide_fce = f2.ide_fce -- Dados concedidos [Alfanumericos]
	LEFT JOIN endereco_empreendimento ee ON e.ide_empreendimento = ee.ide_empreendimento 
			AND ee.ide_tipo_endereco = 4
	LEFT JOIN endereco e2 ON ee.ide_endereco = e2.ide_endereco
	LEFT JOIN logradouro l ON l.ide_logradouro = e2.ide_logradouro
	LEFT JOIN municipio m ON m.ide_municipio = l.ide_municipio 
	LEFT JOIN estado ON estado.ide_estado = m.ide_estado 
	WHERE r.ide_tipo_requerimento = 1
	AND ct.ide_status_fluxo IN (2) -- Considerar 'ConcluÃ­do' (2)? e 'Arquivado' (10) ou 'Cancelado' (17)?
	AND aa.ide_ato_ambiental IN (12,16) -- Considerar 'ASV' (12) e AMPF (16); e 'ARTA' (14)?
	AND tspa.nom_tipo_status_processo_ato IN ('Deferido','Transferido') -- Considerar 'Deferidos' (2) e 'Transferidos' (7)
	AND (p2.dtc_publicacao_portaria >= '2024-01-01' AND p2.dtc_publicacao_portaria < '2024-12-31')
	ORDER BY p2.dtc_publicacao_portaria DESC, r.num_requerimento ASC
) AS t
WHERE geom NOTNULL AND ST_GeometryType(geom) <> 'ST_Point';"""