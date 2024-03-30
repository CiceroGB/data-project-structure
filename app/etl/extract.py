import os
import pandas as pd
import glob


def extract_excel(input_folder: str) -> pd.DataFrame:
    """
    Extrai dados de todos os arquivos Excel em uma pasta especificada.

    Args:
        input_folder (str): Caminho da pasta contendo os arquivos Excel.

    Returns:
        pd.DataFrame: DataFrame consolidado com dados de todos os arquivos Excel.

    Raises:
        ValueError: Se nenhum arquivo Excel for encontrado na pasta.
        Exception: Para erros ocorridos durante a leitura dos arquivos Excel.
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")

    all_data = []
    for file in files:
        try:
            data = pd.read_excel(file)
            all_data.append(data)
        except Exception as e:
            raise Exception(f"Error reading {file}: {e}")

    if not all_data:
        return pd.DataFrame()

    return pd.concat(all_data, ignore_index=True)   
   
    


