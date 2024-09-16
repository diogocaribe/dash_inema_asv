"""Dashboard InemaS"""

from datetime import datetime
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from .app import app


from .components import (
    header,
    map_,
    graph,
    controller_filter,
    controller_datapicker,
    indicador_geral,
    table
)
from dash_inema_asv.dataset.data import seia_asv
from .utils import filtrando_dataframe

server = app.server


app.layout = [
    dbc.Container(
        [
            dcc.Store(id="seia-asv"),
            dbc.Row([header.header]),
            # Filtro
            dbc.Row(
                [
                    html.Div(
                        [
                            # controller_filter.controller_filter,
                            controller_datapicker.date_range_picker,
                        ],
                        style={"padding": "0px", "display": "flex"},
                    )
                ]
            ),
            # Indicadores
            dbc.Row(
                [
                    dbc.Col(
                        [indicador_geral.indicador_geral_],
                        style={
                            # "display": "flex",
                            # "flex-direction": "column",
                            # "align-items": "center",
                            # "justify-content": "center",
                            # "with": '910px'
                        },
                    ),
                    dbc.Col(
                        [map_.map_],
                        style={
                            # "display": "flex",
                            # "flex-direction": "column",
                            # "align-items": "center",
                            # "justify-content": "center",
                            # 'flex': '1'
                        },
                    ),
                ],
                # className="g-1",
            ),
            dbc.Row(
                [
                    dbc.Col([graph.graphs, table.table_div]),
                ]
            ),
            # dbc.Row([footer.footer]),
            # html.Div(id="dd-output-container"),
            html.Div(id="output-container-date-picker-range"),
        ],
        class_name="overflow-hidden",
        fluid=True,
        # style={"width": "100vw", "height": "300vh"},
    )
]


# DataStore monitoramento-desmatamento-municipio
@app.callback(
    Output("seia-asv", "data"),
    Input("date-picker-range", "value"),
)
def filter_seia_asv_geom(dates):
    """
    Metodo que filtra os dados e retorna para os callbacks.
    """

    start_date = dates[0]
    end_date = dates[1]

    dff = filtrando_dataframe(
        inicio=start_date, fim=end_date, coluna_data="data_portaria", df=seia_asv
    )
    dff["data_portaria"] = dff["data_portaria"].astype("string")

    return dff.to_json()


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
