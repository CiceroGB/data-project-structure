"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

from typing import List

import pandas as pd
from pandas import DataFrame


def transforma_em_um_unico(all_data: List[DataFrame]) -> DataFrame:
    """
    Consolida uma lista de DataFrames em um único DataFrame.

    Args:
        all_data (List[DataFrame]): Lista de DataFrames para serem consolidados.

    Returns:
        DataFrame: DataFrame consolidado contendo todos os dados dos DataFrames da lista.

    Raises:
        ValueError: Se a lista `all_data` estiver vazia ou contiver elementos que não são DataFrames.
    """
    if not all_data:
        raise ValueError("No data to transform")

    if not all(isinstance(item, DataFrame) for item in all_data):
        raise ValueError("All elements in the list must be pandas DataFrames")

    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)
    return consolidated_df
