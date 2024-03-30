"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os
from typing import List

import pandas as pd
from pandas import DataFrame


def extract_excel(input_folder: str) -> List[DataFrame]:
    """
    Extrai dados de todos os arquivos Excel em uma pasta especificada.

    Args:
        input_folder (str): Caminho da pasta contendo os arquivos Excel.

    Returns:
        List[DataFrame]: Lista de DataFrames, cada um contendo dados de um arquivo Excel.

    Raises:
        ValueError: Se nenhum arquivo Excel for encontrado na pasta.
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")

    all_data: List[DataFrame] = [pd.read_excel(file) for file in files]
    return all_data
