import dash_bootstrap_components as dbc
from dash import html


indicador_geral = html.Div(
    [
        html.P("Quantitativo Geral", className="titulo-box"),
        html.Div(
            [
                html.P("Indicadores"),
                html.Hr(style={"width": "397px"}),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P("Àrea Suprimida (ha)"),
                                        html.Div([html.P(7777, style={})]),
                                    ]
                                )
                            ],
                            className="div-box",
                            style={
                                "width": "190px",
                                "height": "125px",
                                "padding": "16px 0px 0px 13px",
                            },
                        ),
                        html.Div(
                            [html.Div([html.P("Processos"), html.Div([html.P(4500)])])],
                            className="div-box",
                            style={
                                "width": "190px",
                                "height": "125px",
                                "padding": "16px 0px 0px 13px",
                            },
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
        "padding": "16px 0px 0px 13px",
    },
)
