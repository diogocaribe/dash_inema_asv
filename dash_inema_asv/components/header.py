from dash import html

header = html.Header(
    [html.H4("Autorização de Supressão de Vegetação | DIRRE"), html.H5("Inema")],
    className="""bg-primary
                    text-light font-size-adjust 
                    d-flex justify-content-between align-items-center""",
    style={"height": "5vh"},
)
