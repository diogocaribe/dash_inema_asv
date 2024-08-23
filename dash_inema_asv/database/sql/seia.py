# TODO Verificar se precisaremos adicionar o status do ato na consulta (deferido e transferido)
seia_sql_geom = '''SELECT (select unnest(array_agg(gid)) as id_array2 order by id_array2 limit 1) AS gid
	, area_ha_concedida
	, ROUND(sum(area_ha_concedida_geom)::NUMERIC, 4) area_ha_concedida_geom
	, ROUND(sum(area_ha_concedida_geom)::NUMERIC, 4) - area_ha_concedida AS diff
	, nome_ato_ambiental
	, numero_processo
	, numero_portaria
	, data_portaria
	, st_union(geom) AS geom
FROM (
	SELECT lg.ide_localizacao_geografica AS gid
			,  pac.val_atividade AS area_ha_concedida -- Para o caso da ASV
			, CASE 
				WHEN sc.srid IN ('31983') THEN st_area(st_transform(dg.the_geom,31983))/10000
				WHEN sc.srid IN ('31984') THEN st_area(st_transform(dg.the_geom,31984))/10000
				WHEN sc.srid IN ('29193') THEN st_area(st_transform(dg.the_geom,29193))/10000
				WHEN sc.srid IN ('29194') THEN st_area(st_transform(dg.the_geom,29194))/10000
				ELSE st_area(st_transform(dg.the_geom, 31983))/10000 -- Conversao considerando menor desvio para UTM 23S (Foco: Cerrado)
			  END AS area_ha_concedida_geom
			, aa.nom_ato_ambiental AS nome_ato_ambiental
			, p.num_processo AS numero_processo
			, p2.num_portaria AS numero_portaria
			, p2.dtc_portaria::Date AS data_portaria
			, dg.the_geom AS geom
	FROM localizacao_geografica lg 
	JOIN dado_geografico dg ON dg.ide_localizacao_geografica = lg.ide_localizacao_geografica 
	JOIN processo_ato_concedido pac ON pac.ide_localizacao_geografica = lg.ide_localizacao_geografica 
	JOIN processo_ato pa ON pa.ide_processo_ato = pac.ide_processo_ato
	JOIN ato_ambiental aa ON aa.ide_ato_ambiental = pa.ide_ato_ambiental
	JOIN processo p ON p.ide_processo =  pa.ide_processo 
	JOIN portaria p2 ON p2.ide_processo = p.ide_processo 
	JOIN sistema_coordenada sc ON sc.ide_sistema_coordenada = lg.ide_sistema_coordenada
	WHERE aa.ide_ato_ambiental = 12 -- 12 é o valor para ASV
	AND ST_GeometryType(the_geom) <> 'ST_Point' -- Removendo pontos
	-- Removendo as duplicatas de registro quando o gid e a área concedidada são iguais
	GROUP BY lg.ide_localizacao_geografica, pac.val_atividade, sc.srid, aa.nom_ato_ambiental, p.num_processo, p2.num_portaria, p2.dtc_portaria, dg.the_geom
) t
GROUP BY area_ha_concedida, nome_ato_ambiental, numero_processo, numero_portaria, data_portaria;'''
