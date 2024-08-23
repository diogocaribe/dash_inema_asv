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


def group_by_time(periodo: str, df, dtc_column_name: str, list_columns_sum: str):
    """Essa função agrupa os dados por mês a ano

    Args:
        periodo (str): São as opções para seleção no dropdown
                Opções: 'Dia', 'Mês', 'Ano'
        df (Dataframe):  Conjunto de dados para análise
        dtc_column_name (str): Nome da coluna que tem a data
        list_sum_Columns (list): Lista de colunas que serão agrupadas pela soma

    Returns:
        _type_: Dataframe do agrupamento
    """
    col = dtc_column_name

    list_columns = dtc_column_name, list_columns_sum

    dff = df.copy()
    
    if periodo == "Dia":
        return df
    if periodo == "Mês":
        dff = dff.loc[:,[dtc_column_name, list_columns_sum]]
        dff['data_portaria'] = pd.to_datetime(dff['data_portaria'])
        df['data_portaria'] = pd.to_datetime(df['data_portaria']).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))
        group = df.groupby('data_portaria')['area_ha_concedida_geom'].sum()
        from pandas import DataFrame
        group = DataFrame(group)
        print(group)
        return group
    if periodo == "Ano":
        dff = dff[list_columns]
        group = dff.groupby(dff[col].dt.year)[list_columns].sum()
        return group
