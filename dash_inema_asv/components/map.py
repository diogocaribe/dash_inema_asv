import dash_bootstrap_components as dbc
import dash_leaflet as dl
from dash import Input, Output, callback, dcc, html
import json


map = html.Div(
    [
        html.P(
            "Mapa de Monitoramento",
            className="titulo-box",
            style={"padding-bottom": "16px"},
        ),
        dl.Map(
            [dl.TileLayer(), dl.GeoJSON(id="geojson-mapa")],
            center=[-16.50, -41],
            zoom=6,
            minZoom=6,
            maxBounds=[[-21.0, -50.0], [-5.0, -30.0]],
            id="leaflet-map",
            style={
                "width": "100%",
                "height": "91%",
            },
        ),
    ],
    className="div-map",
    style={
        "width": "100%",
        "height": "100%", # 600px
        "padding": "16px 16px 0px 16px",
        "margin": "8px 8px 8px 8px",
    },
)



# Callback mapa
@callback(
    Output("geojson-mapa", "children"),
    Input("seia-asv", "data"),
)
def update_output_mapa(gdf):
    """
    Função para atualização dos dados do mapa.
    """
    map_geojson = dl.GeoJSON(
        data=json.loads(gdf),
        # zoomToBounds=True,
        zoomToBoundsOnClick=True,
        options={"style": {"color": "red"}},
    )

    return map_geojson
