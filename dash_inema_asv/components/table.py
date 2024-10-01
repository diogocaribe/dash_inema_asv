import json
from dash import html, dash_table, html, Input, Output, callback
import geopandas as gpd


table_div = html.Div(
    [
        html.P("Processos Autorização de Supressão Vegetação", 
               className="titulo-box", style={'padding': '0% 0% 2% 0%'}),
        html.Div(id="tabela-processo"),
    ],
    className="div-box-table",
)


@callback(
    Output("tabela-processo", "children"),
    Input("seia-asv", "data"),
)
def update_tabela(dados):
    """_summary_

    Args:
        dados (_type_): _description_

    Returns:
        _type_: _description_
    """
    data_json = json.loads(dados)

    df = gpd.GeoDataFrame.from_features(data_json)
    df = df.loc[
        :,
        [
            "data_portaria",
            "numero_portaria",
            "numero_processo",
            "area_ha_concedida_geom",
        ],
    ]
    df.rename(columns={
            "data_portaria": 'Data Portaria',
            "numero_portaria": 'Nº Portaria',
            "numero_processo": 'Nº Processo',
            "area_ha_concedida_geom": 'Área (ha)'}, inplace=True
        )

    tabela = dash_table.DataTable(
                data=df.to_dict("records"),
                columns=[{"id": c, "name": c} for c in df.columns],
                # Sort
                sort_action="native",
                sort_mode="multi",
                editable=False,
                # Style
                style_as_list_view=True,  # Linhas entre as celulas (sem linhas nas colunas)
                style_data={
                    "border": "1px solid #DFDFDF",
                    "height": "15px",
                },  # Estinho da linha entre as celulas
                style_table={
                    "border": "1px solid #DFDFDF",
                    "overflowY": "auto",
                    "border-radius": "4px 4px 0px 0px",
                    "height": '28vh',
                },  # Borda ao redor da tabela
                style_header={
                    "backgroundColor": "#F4F4F6",
                },
                style_cell={
                    "textAlign": "center",
                    "font-family": "Roboto",
                    "font-size": "0.8rem",
                    "font-weight": 400,
                    "line-height": "13.5px",
                    "letter-spacing": "0.005em",
                },
                fixed_rows={'headers': True},
        )
    return tabela
