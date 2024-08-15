import pandas as pd


def filtrando_dataframe(inicio: str, fim: str, coluna_data: str, df):
    """_summary_

    Args:
        inicio (str): Data de inicio do filtro
        fim (str): Data do final do filtro
        coluna_data (str): Coluna do dataframe em formato data 'YYYY-MM-DD'
        df (_type_): Dataframe a ser filtrado

    Returns:
        _type_: Dataframe
    """
    # Filtra o DataFrame pelo intervalo de datas
    filtro = (df[coluna_data] >= inicio) & (df[coluna_data] <= fim)
    df_filtrado = df[filtro]

    return df_filtrado
