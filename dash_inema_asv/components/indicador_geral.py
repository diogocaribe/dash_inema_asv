import json
import dash_bootstrap_components as dbc
from dash import html, Input, Output, callback
import geopandas as gpd


indicador_geral_ = html.Div(
    [
        html.P("Quantitativo Geral", className="titulo-box"),
        html.Div(
            [
                html.P("Indicadores", className="titulo-indicador"),
                html.Hr(style={"width": "397px"}),
                html.Div(
                    [
                        html.Div(
                            [
                                html.P(
                                    "Processos",
                                    className="titulo-conteudo-indicador",
                                ),
                                html.P(
                                    id="qtd-processo", className="conteudo-indicador"
                                ),
                            ],
                            className="box-interno-indicador-geral",
                        ),
                        html.Div(
                            [
                                html.P(
                                    "Àrea Suprimida (ha)",
                                    className="titulo-conteudo-indicador",
                                ),
                                html.P(
                                    id="qtd-area-concedida-geom",
                                    className="conteudo-indicador_segundo",
                                ),
                            ],
                            className="box-interno-indicador-geral",
                        ),
                    ],
                    style={
                        "display": "flex",
                        "justifyContent": "space-between",
                        "alignItems": "center",  # Opcional: Alinha verticalmente no centro
                        "width": "397px",  # Ajusta a largura do container conforme necessário
                    },
                ),
            ]
        ),
    ],
    className="div-box",
    style={
        "width": "429px",
        "height": "248px",
        "padding": "16px 0px 0px 16px",
    },
)


@callback(
    Output("qtd-processo", "children"),
    Input("seia-asv", "data"),
    Input("demo-dropdown", "value"),
)
def quantidade_processo(dados, value):
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)
    quantidade_processo = len(dff)

    return f"{quantidade_processo:,}".replace(",", ".")


@callback(
    Output("qtd-area-concedida-geom", "children"),
    Input("seia-asv", "data"),
    Input("demo-dropdown", "value"),
)
def quantidade_area_concedidada_geom(dados, value):
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)

    quantidade_area_concedida = round(dff["area_ha_concedida_geom"].sum())

    return f"{quantidade_area_concedida:,}".replace(",", ".")
