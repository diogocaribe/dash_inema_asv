"""Controllers"""

from dash import html
import dash_mantine_components as dmc
from ..dataset.data import max_date, min_date, min_date_90_dias


date_range_picker = html.Div(
    [
        html.Div(
            [
                html.P("Data", style={"margin": "0", "color": "#FFFFFF"}),
                dmc.DateRangePicker(
                    id="date-picker-range",
                    clearable=False,
                    minDate=min_date,
                    maxDate=max_date,
                    value=[min_date_90_dias, max_date],
                    inputFormat="DD/MM/YYYY",
                    zIndex=10000,
                ),
            ],
            style={"width": "200px", "height": "52px"},
        ),
    ],
    id="controller_filter_datarange",
    style={
        "width": "100%",
        "height": "100%",
        # "background": "#1F2D4D",
        "display": "flex",
        "justifyContent": "flex-start",
        "alignItems": "center",
    },
)
