from typing import List
import pandas as pd

def transforma_em_um_unico(all_data: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Consolida uma lista de DataFrames do pandas em um único DataFrame.

    Esta função concatena verticalmente todos os DataFrames fornecidos na lista `all_data`.
    O índice do DataFrame resultante é redefinido para garantir a unicidade.

    Args:
        all_data (List[pd.DataFrame]): Lista de DataFrames do pandas para consolidar.

    Returns:
        pd.DataFrame: DataFrame único consolidado de todos os DataFrames na lista.

    Raises:
        ValueError: Se a lista `all_data` estiver vazia ou contiver elementos que não são DataFrames.
    """
    if not all_data:
        raise ValueError("No data to transform")

    # Verifica se todos os elementos na lista são DataFrames
    if not all(isinstance(df, pd.DataFrame) for df in all_data):
        raise ValueError("All elements in the list must be pandas DataFrames")

    # Concatena todos os DataFrames na lista em um único DataFrame
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)

    return consolidated_df
