from dash import html, dash_table
from pandas import DataFrame

def box_indicador_geral(df: DataFrame):
    '''Função para gerar tabela a partir de um pandas Dataframe

    Args:
        df (DataFrame): Dataframe para criação da tabela

    Returns:
        _type_: Tabela para o layout
    '''

    box = html.Div([
        html.P('Processos Asv', className='titulo-box'),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            # Sort
            sort_action='native',
            sort_mode='multi',
            editable=False,
            # Style
            style_as_list_view=True,  # Linhas entre as celulas (sem linhas nas colunas)
            style_data={
                'border': '1px solid #DFDFDF',
                'height': '15px',
            },  # Estinho da linha entre as celulas
            style_table={
                'border': '1px solid #DFDFDF',
                'height': '483px',
                'overflowY': 'auto',
                'border-radius': '4px 4px 0px 0px',
            },  # Borda ao redor da tabela
            style_header={
                'backgroundColor': '#F4F4F6',
                'height': '37px',
                'whiteSpace': 'normal',
                'position': 'sticky',  # Fixa o cabeçalho
                'top': '0',  # Define a posição do cabeçalho no topo
                'zIndex': '1',
            },
            style_cell={
                'textAlign': 'center',
                'font-family': 'Roboto',
                'font-size': '12px',
                'font-weight': 400,
                'line-height': '13.5px',
                'letter-spacing': '0.005em',
            },
        ),
    ], className='div-table')

    return box
