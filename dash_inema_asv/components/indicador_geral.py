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
                html.Hr(),
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
                                    "Àrea Autorizada (ha)",
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
                    },
                ),
            ],
            style={"width": "100%"},
        ),
    ],
    className="div-box",
    style={
        "width": "100%",
        "padding": "2% 2% 2% 2%",
        "margin": "8px",
    },
)


@callback(
    Output("qtd-processo", "children"),
    Input("seia-asv", "data"),
    # Input("demo-dropdown", "value"),
)
def quantidade_processo(dados):
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)
    quantidade_processo = len(dff)

    return f"{quantidade_processo:,}".replace(",", ".")


@callback(
    Output("qtd-area-concedida-geom", "children"),
    Input("seia-asv", "data"),
    # Input("demo-dropdown", "value"),
)
def quantidade_area_concedidada_geom(dados):
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)

    quantidade_area_concedida = round(dff["area_ha_concedida_geom"].sum())

    return f"{quantidade_area_concedida:,}".replace(",", ".")
