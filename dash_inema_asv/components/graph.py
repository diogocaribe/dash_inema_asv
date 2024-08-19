"""Barra de graficos."""

import json
from dash import dcc, html, Input, Output, callback
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import geopandas as gpd

import pandas as pd

template_graph = {
    "layout": {
        "modebar": {
            "remove": [
                "zoom",
                "pan",
                "select",
                "zoomIn",
                "zoomOut",
                "lasso2d",
                "autoscale",
            ]
        },
        "separators": ".",
        "showlegend": False,
    }
}

graphs = html.Div(
    [
        html.Div(
            [
                dcc.Graph(
                    id="grafico-dia",
                    config={"displaylogo": False, "scrollZoom": False},
                ),
            ]
        ),
    ]
)


# Callback no grafico de desmatamento diário
# TODO adicinar um filtro aninhado (chaincallback) para agrupar o tempo (D, M, Y)
@callback(
    Output("grafico-dia", "figure"),
    Input("seia-asv", "data"),
)
def update_output_grafico_dia(dados):
    """
    Grafico de atualização de dados do dia
    """
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)

    data_day = go.Bar(
        x=dff.data_portaria,
        y=dff["area_ha_concedida"],
        customdata=np.stack(dff["numero_processo"], axis=-1),
    )
    layout = go.Layout(
        title="<b>ASV</b>",
        xaxis={"title": "Data"},
        yaxis={"title": "Área (ha)"},
    )

    grafico_dia = go.Figure(data=data_day, layout=layout)

    grafico_dia.update_layout(template=template_graph)
    grafico_dia.update_yaxes(fixedrange=False)
    grafico_dia.update_traces(
        hovertemplate="""Número do processo: %{customdata}<br>Data: %{x}<br>Área concedida (ha): %{value:.2f}<extra></extra>"""
    )

    return grafico_dia
