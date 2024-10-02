"""Dashboard InemaS"""

from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc

from .app import app

from .components import (
    header,
    map_,
    graph,
    controller_datapicker,
    indicador_geral,
    table,
    footer
)
from dash_inema_asv.dataset.data import seia_asv
from .utils import filtrando_dataframe

server = app.server


app.layout = [
    dbc.Container(
        [
            dcc.Store(id="seia-asv"),
            # Cabeçalho do Painel
            dbc.Row([header.header]),
            # Filtros
            dbc.Row(
                [
                    html.Div(
                        [
                            controller_datapicker.date_range_picker,
                        ],
                        # style={"padding": "0px"},
                    )
                ], style={'padding': '0.1%', "background": "#1F2D4D"},
            ),
            # Indicadores e Paineis
            dbc.Row(
                [
                    dbc.Col(
                        [indicador_geral.indicador_geral_, map_.map_],
                        width=4,
                        style={"padding": "8px",
                               'display': 'flex',
                               'flex-direction': 'column',
                               'box-sizing':'border-box'},
                    ),
                    dbc.Col(
                        [graph.graphs, table.table_div], 
                        width=8,
                        style={"padding": "8px",
                                'display': 'flex',
                               'flex-direction': 'column',
                               'box-sizing':'border-box'
                               }),
                ],
            ),
            # dbc.Row([footer.footer]),
            # html.Div(id="dd-output-container"),
            html.Div(id="output-container-date-picker-range"),
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
    app.run_server(debug=True, port=8051)
