from typing import List
import pandas as pd


def transforma_em_um_unico(all_data: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Consolida uma lista de DataFrames do pandas em um único DataFrame.

    Args:
        all_data (List[pd.DataFrame]): Lista de DataFrames do pandas para consolidar.

    Returns:
        pd.DataFrame: DataFrame único consolidado de todos os DataFrames na lista.

    Raises:
        ValueError: Se a lista `all_data` estiver vazia, indicando que não há dados para transformar.
    """
    # Verifica se a lista all_data contém algum elemento
    if not all_data:
        raise ValueError("No data to transform")

    # Concatena todos os DataFrames na lista em um único DataFrame
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)

    return consolidated_df
