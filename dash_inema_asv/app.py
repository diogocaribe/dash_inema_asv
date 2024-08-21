'''Dashboard Inema'''
# coding: utf-8

import dash
import dash_bootstrap_components as dbc
from flask import Flask

import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# css para deixar o layout bonito
external_stylesheets = [dbc.themes.MATERIA, dbc.themes.BOOTSTRAP]

server = Flask(__name__)
app = dash.Dash(server=server, external_stylesheets=external_stylesheets)
app.title = 'AsvDashboard'
