import os
import pandas as pd

def load_em_um_novo_excel(df: pd.DataFrame, output_folder: str, output_file_name: str) -> None:
    """
    Salva um DataFrame em um arquivo Excel no diretório especificado.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo em arquivo Excel.
        output_folder (str): Caminho da pasta onde o arquivo Excel será salvo.
        output_file_name (str): Nome do arquivo Excel a ser criado.

    Não retorna nada, mas salva o arquivo Excel no caminho especificado.
    """
    # Verifica se a pasta de saída existe, se não, cria a pasta
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Salva o DataFrame em um arquivo Excel no caminho especificado
    file_path = os.path.join(output_folder, output_file_name)
    df.to_excel(file_path, index=False)  # O parâmetro index=False remove o índice do DataFrame no arquivo Excel
