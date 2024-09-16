"""Controllers"""

from dash import html
import dash_mantine_components as dmc
from ..dataset.data import max_date, min_date, year_start


date_range_picker = html.Div(
    [
        html.Div(
            [
                html.P("Data", style={"margin": "0", "color": "#FFFFFF"}),
                dmc.DateRangePicker(
                    id="date-picker-range",
                    minDate=min_date,
                    maxDate=max_date,
                    value=[year_start, max_date],
                    inputFormat="DD/MM/YYYY",
                    zIndex=1000,
                    style={
                        "background-color": '#C7C6C6',
                    }
                ),
            ],
            style={"width": "240.72px", "height": "52px"},
        ),
    ],
    id="controller_filter_datarange",
    style={
        "width": "100%",
        "height": "84px",
        "background": "#1F2D4D",
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
    },
)
