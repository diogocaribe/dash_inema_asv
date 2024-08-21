from dash import html

header = html.Header(
    [
        html.P(
            'Autorização de Supressão de Vegetação | DIRRE',
            style={
                'fontFamily': 'Roboto',
                'fontSize': '20px',
                'fontWeight': '400',
                'margin': '0',
                'color': '#FFFFFF',
            },
        ),
        html.Img(
            src='../assets/marca_inema_branca_sem_fundo.png',
            alt='image',
            style={'width': '85px', 'height': '27px', 'top': '7.5px', 'left': '1339px'},
        ),
    ],
    style={'width': '1440px', 'height': '42px', 'background': '#3C71DD', 'display': 'flex',
        'justifyContent': 'space-between', 'alignItems': 'center'},
)
