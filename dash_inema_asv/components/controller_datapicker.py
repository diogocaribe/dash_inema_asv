"""Controllers"""

from dash import html
import dash_mantine_components as dmc
from dataset.data import max_date, min_date, year_start


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
                    style={
                            "backgroundColor": "#C7C6C6",  # Cor de fundo desejada
                            "color": "#000000",  # Cor do texto
                        }
                    ),
            ],
            style={"width": "240.72px", "height": "52px"},
        ),
    ],
    id="controller_filter_datarange",
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