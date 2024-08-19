from dash import html, dcc, Output, Input, callback
from datetime import date

filtro = html.Div([])

controller_filter = html.Div(
    [
        html.Div(
            [
                html.P("Filtro", style={"margin": "0", "color": "#FFFFFF"}),
                dcc.Dropdown(
                    ["NYC", "MTL", "SF"],
                    placeholder="Selecione",
                    id="demo-dropdown",
                    style={
                        "width": "161.23px",
                        "height": "32px",
                        "backgroundColor": "#C7C6C6",
                        "borderRadius": "3px",
                        "border": "0.5px solid #C7C6C63",
                    },
                ),
            ],
            style={"width": "161.72px", "height": "52px"},
        ),
    ],
    id="controller_filter",
    style={
        "width": "1440px",
        "height": "84px",
        "background": "#1F2D4D",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
    },
)


@callback(Output("dd-output-container", "children"), Input("demo-dropdown", "value"))
def update_output(value):
    return f"You have selected {value}"
