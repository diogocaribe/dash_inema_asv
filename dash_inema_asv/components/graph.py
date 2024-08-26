'''Barra de graficos.'''

import json
from dash import dcc, html, Input, Output, callback
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

import geopandas as gpd

import pandas as pd

from utils import group_by_time

template_graph = {
    'layout': {
        'modebar': {
            'remove': [
                'zoom',
                'pan',
                'select',
                'zoomIn',
                'zoomOut',
                'lasso2d',
                'autoscale',
            ]
        },
        'separators': '.',
        'showlegend': False,
    }
}

graphs = html.Div(
            [
                dcc.Dropdown(
                    ['Dia', 'Mês', 'Ano'],
                    placeholder='Selecione',
                    id='dropdown-tempo',
                    value='Mês',
                    style={
                        'width': '161.23px',
                        'height': '32px',
                        'backgroundColor': '#C7C6C6',
                        'borderRadius': '3px',
                        'border': '0.5px solid #C7C6C63',
                    },
                ),
                dcc.Graph(
                    id='grafico-dia',
                    config={'displaylogo': False, 'scrollZoom': False},
                ),
            ])


# Callback no grafico de desmatamento diário
# TODO adicinar um filtro aninhado (chaincallback) para agrupar o tempo (D, M, Y)
@callback(
    Output('grafico-dia', 'figure'),
    Input('seia-asv', 'data'),
    Input('dropdown-tempo', 'value')
)
def update_output_grafico_dia(dados, value):
    '''
    Grafico de atualização de dados do dia
    '''
    data_json = json.loads(dados)

    dff = gpd.GeoDataFrame.from_features(data_json)

    dff = group_by_time(periodo=value, df=dff, dtc_column_name='data_portaria', list_columns_sum='area_ha_concedida_geom')

    if value == 'Dia':
        data_day = go.Bar(
            x=dff.data_portaria,
            y=dff['area_ha_concedida_geom'],
            customdata=np.stack(dff['numero_processo'], axis=-1),
        )
    else:
        data_day = go.Bar(
            x=dff.index,
            y=dff['area_ha_concedida_geom'],
        )
    layout = go.Layout(
        title='<b>ASV</b>',
        xaxis={'title': 'Data'},
        yaxis={'title': 'Área (ha)'},
    )

    grafico_dia = go.Figure(data=data_day, layout=layout)

    grafico_dia.update_layout(template=template_graph)
    grafico_dia.update_yaxes(fixedrange=False)
    grafico_dia.update_traces(
        hovertemplate='''Número do processo: %{customdata}<br>Data: %{x}<br>Área concedida (ha): %{value:.2f}<extra></extra>'''
    )

    return grafico_dia
