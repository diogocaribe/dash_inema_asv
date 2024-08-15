"""Dashboard InemaS"""

from datetime import datetime
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app


from components import footer, header, map_, graph
from dataset.data import seia_asv
from utils import filtrando_dataframe

server = app.server


app.layout = [
    dbc.Container(
        [
            dcc.Store(id="seia-asv"),
            dbc.Row([header.header]),  # 5vh
            dbc.Row(  # 92vh
                [
                    dbc.Col([map_.map_], width=7),
                    dbc.Col(
                        [graph.graphs],
                        width=5,
                        style={"overflow-y": "scroll", "height": "92vh"},
                    ),
                ]
            ),
            dbc.Row([footer.footer]),  # 92vh
        ],
        class_name="overflow-hidden",
        fluid=True,
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
    app.run_server(debug=True)
