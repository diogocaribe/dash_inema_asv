"""Barra de graficos."""

from dash import dcc, html, Input, Output, callback
import numpy as np
import plotly.express as px
from .controller import date_range_picker
import plotly.graph_objects as go
from io import StringIO

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
                date_range_picker,
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
    dff = pd.read_json(dados)

    data_day = go.Bar(
        x=dff.index,
        y=dff["Conced_area_tot_supres_ha"],
        customdata=np.stack(dff["nom_municipio"], axis=-1),
    )
    layout = go.Layout(
        title="<b>Evolução diária do desmatamento</b>",
        xaxis={"title": "Data"},
        yaxis={"title": "Área (ha)"},
    )

    grafico_dia = go.Figure(data=data_day, layout=layout)

    grafico_dia.update_layout(template=template_graph)
    grafico_dia.update_yaxes(fixedrange=False)
    grafico_dia.update_traces(
        hovertemplate="""Município: %{customdata}<br>Data: %{x}<br>Área (ha): %{value:.2f}<extra></extra>"""
    )

    return grafico_dia
