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
                    style={"width": "161.23px", "height": "32px", "backgroundColor": "#C7C6C6", 'borderRadius': '3px', 'border': '0.5px solid #C7C6C63'},

                ),
            ],
            style={"width": "161.72px", "height": "52px"},
        ),
        html.Div(id="dd-output-container"),
        dcc.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2017, 9, 19),
            initial_visible_month=date(2017, 8, 5),
            end_date=date(2017, 8, 25),
        ),
        html.Div(id="output-container-date-picker-range"),
    ],
    id="controller_filter",
    style={
        "width": "1440px",
        "height": "84px",
        "top": "42px",
        "background": "#1F2D4D",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "gap": "20px",
    },
)


@callback(Output("dd-output-container", "children"), Input("demo-dropdown", "value"))
def update_output(value):
    return f"You have selected {value}"


@callback(
    Output("output-container-date-picker-range", "children"),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date"),
)
def update_output_1(start_date, end_date):
    string_prefix = "You have selected: "
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime("%B %d, %Y")
        string_prefix = string_prefix + "Start Date: " + start_date_string + " | "
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime("%B %d, %Y")
        string_prefix = string_prefix + "End Date: " + end_date_string
    if len(string_prefix) == len("You have selected: "):
        return "Select a date to see it displayed here"
    else:
        return string_prefix
