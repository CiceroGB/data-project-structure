import os
import pandas as pd

def load_em_um_novo_excel(df: pd.DataFrame, output_folder: str, output_file_name: str) -> None:
    """
    Salva um DataFrame do pandas em um arquivo Excel em um diretório especificado.
    
    Args:
        df (pd.DataFrame): DataFrame que será salvo em um arquivo Excel.
        output_folder (str): Caminho do diretório onde o arquivo Excel será salvo.
        output_file_name (str): Nome do arquivo Excel a ser criado.
    
    Raises:
        PermissionError: Se ocorrer um erro de permissão ao salvar o arquivo Excel.
        Exception: Se ocorrer um erro ao salvar o arquivo Excel.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        file_path = os.path.join(output_folder, output_file_name)
        df.to_excel(file_path, index=False)
    except PermissionError as e:
        raise PermissionError(f"Erro de permissão ao salvar o arquivo Excel: {e}")
    except Exception as e:
        raise Exception(f"Erro ao salvar o arquivo Excel: {e}")