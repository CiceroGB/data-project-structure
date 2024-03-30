"""Módulo para iniciar o ETL."""

from .extract import extract_excel
from .load import load_em_um_novo_excel
from .transform import transforma_em_um_unico


def pipeline_completa(
    input_folder: str, output_folder: str, output_file_name: str
) -> None:
    """
    Executa um processo ETL completo.

    Extrai dados de arquivos Excel em uma pasta,
    transforma esses dados consolidando-os em um único DataFrame, e carrega esse DataFrame
    em um novo arquivo Excel na pasta de destino especificada.

    Args:
        input_folder (str): Caminho da pasta de onde os arquivos Excel serão extraídos.
        output_folder (str): Caminho da pasta onde o arquivo Excel resultante será salvo.
        output_file_name (str): Nome do arquivo Excel a ser criado na pasta de destino.

    Returns:
        None: Esta função não retorna nada, mas salva o arquivo Excel no local especificado.
    """
    # Extrai dados dos arquivos Excel na pasta de entrada
    data = extract_excel(input_folder)

    # Transforma os dados extraídos em um único DataFrame
    consolidated_df = transforma_em_um_unico(data)

    # Carrega o DataFrame consolidado em um novo arquivo Excel na pasta de saída
    load_em_um_novo_excel(consolidated_df, output_folder, output_file_name)
