"""Controllers"""

# Atenção: para a lib dash_matine_components utilizamos a versão 0.12
# Documentação https://dmc-docs-0-13.onrender.com/
import dash_mantine_components as dmc
from datetime import datetime, date
from dash import html
from dash import Input, Output, callback
from dash.exceptions import PreventUpdate

from datetime import datetime, timedelta, date

import dash_mantine_components as dmc
from dash import Input, Output, html, callback
from dash.exceptions import PreventUpdate


from dataset.data import year_start, year_end, min_date, max_date

date_range_picker = dmc.DateRangePicker(
    id="date-picker-range",
    label="Intervalo de data",
    description="Selecione o intervalo temporal para análise",
    minDate=min_date,
    maxDate=max_date,
    value=[year_start, year_end],
    inputFormat="DD/MM/YYYY",
)
