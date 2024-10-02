"""Barra de graficos."""

import json
from dash import dcc, html, Input, Output, callback
import numpy as np
import plotly.graph_objects as go

import geopandas as gpd

from ..utils import group_by_time

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
        "plot_bgcolor": "white",  # Área do fundo do gráfico
        "yaxis": {
            "automargin": True,
            "gridcolor": "#C4C4C4",  # Cor da linha
            "linecolor": "black",  # Cor do eixo y e x
            "title": {"standoff": 15},
        },
        "font": {"family": "Roboto", "weight": 400, "size": 12, "color": "#969BAB"},
    }
}

graphs = html.Div(
    [
        html.Div(
            [
                html.P("Autorização Supressão Vegetação", className="titulo-box"),
                dcc.Dropdown(
                    ["Dia", "Mês", "Ano"],
                    placeholder="Selecione",
                    clearable=False,
                    id="dropdown-tempo",
                    value="Dia",
                    style={
                        "width": "161.23px",
                        "height": "32px",
                        "backgroundColor": "white",
                        "borderRadius": "3px",
                        "border": "0.5px solid #C7C6C63",
                    },
                ),
            ],
            style={
                "display": "flex",
                "align-items": "center",
                "justify-content": "space-between",
                "height": "42px",
            },
        ),
        dcc.Graph(
            id="grafico-dia",
            config={"displaylogo": False, "scrollZoom": False},
        ),
    ],
    className="div-box-graph",
    style={'margin': '8px'}
)


# Callback no grafico de desmatamento diário
# TODO adicinar um filtro aninhado (chaincallback) para agrupar o tempo (D, M, Y)
@callback(
    Output("grafico-dia", "figure"),
    Input("seia-asv", "data"),
    Input("dropdown-tempo", "value"),
)
def update_output_grafico_dia(dados, value):
    """
    Grafico de atualização de dados do dia
    """
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)

    dff = group_by_time(
        periodo=value,
        df=dff,
        dtc_column_name="data_portaria",
        list_columns_sum="area_ha_concedida_geom",
    )

    if value == "Dia":
        data_day = go.Bar(
            x=dff.data_portaria,
            y=dff["area_ha_concedida_geom"],
            customdata=np.stack(dff["numero_processo"], axis=-1),
            marker=dict(color="#3D5AFF"),
        )
    else:
        data_day = go.Bar(
            x=dff.index,
            y=dff["area_ha_concedida_geom"],
            marker=dict(color="#3D5AFF"),
        )

    layout = go.Layout(
        xaxis={"title": "Data"},
        yaxis={"title": "Área (ha)"},
    )

    grafico_dia = go.Figure(data=data_day, layout=layout)

    grafico_dia.update_layout(template=template_graph)
    grafico_dia.update_yaxes(fixedrange=False)

    if value == "Dia":
        grafico_dia.update_traces(
            hovertemplate="""Data: %{x}<br>Área concedida (ha): %{value:.2f}<extra></extra>"""
        )
    else:
        grafico_dia.update_traces(
            texttemplate="%{value}",
            textposition="outside",  # Posiciona os valores no topo das barras
            textfont=dict(family="Roboto", size=11, color="#212227"),
            hovertemplate="""Data: %{x}<br>Área concedida (ha): %{value:.2f}<extra></extra>""",
        )

    return grafico_dia
