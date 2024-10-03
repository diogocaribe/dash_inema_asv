import dash_leaflet as dl
from dash import Input, Output, callback, html
import json


map = html.Div(
    [
        html.P(
            "Mapa de Monitoramento",
            className="titulo-box",
            style={"padding-bottom": "1.5%"},
        ),
        dl.Map(
            [dl.TileLayer(), dl.GeoJSON(id="geojson-mapa")],
            center=[56, 10],
            zoom=5,
            preferCanvas=True,
            maxBounds=[[-8.4, -46.6], [-18.3, -37.3]],
            id="leaflet-map",
            style={
                "width": "100%",
                "height": "95.5%",
            },
        ),
    ],
    className="div-map",
    style={
        "width": "100%",
        "height": "100%",
        "padding": "3% 3% 3% 3%",
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
        # zoomToBoundsOnClick=True,
        options={"style": {"color": "red"}},
    )

    return map_geojson
