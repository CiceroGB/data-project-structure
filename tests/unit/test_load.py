import os

import pandas as pd
import pytest

from app.etl import load_em_um_novo_excel


@pytest.fixture
def dados_exemplo():
    """Fornece um DataFrame de exemplo para os testes."""
    return pd.DataFrame({"A": [1, 2, 3, 4, 5, 6], "B": ["a", "b", "c", "d", "e", "f"]})


@pytest.fixture
def pasta_entrada_mock(tmpdir, dados_exemplo):
    """
    Cria uma pasta de entrada mock com arquivos Excel de exemplo para os testes.
    """
    pasta_entrada = tmpdir.mkdir("pasta_entrada")
    arquivo1_path = pasta_entrada.join("arquivo1.xlsx")
    arquivo2_path = pasta_entrada.join("arquivo2.xlsx")
    dados_exemplo.iloc[:3].to_excel(arquivo1_path, index=False)
    dados_exemplo.iloc[3:].to_excel(arquivo2_path, index=False)
    return str(pasta_entrada)


@pytest.fixture
def pasta_saida_mock(tmpdir):
    """Cria uma pasta de saída mock para os testes."""
    return str(tmpdir.mkdir("pasta_saida"))


def test_carregar_sem_permissao(tmpdir, dados_exemplo):
    pasta_protegida = tmpdir.mkdir("pasta_protegida")
    os.chmod(str(pasta_protegida), 0o444)  # Permissões somente leitura

    with pytest.raises(PermissionError) as exc_info:
        load_em_um_novo_excel(dados_exemplo, str(pasta_protegida), "teste.xlsx")

    assert "Permission denied" in str(
        exc_info.value
    ), "Deveria falhar com erro de permissão"


def test_carregar_sucesso(pasta_saida_mock, dados_exemplo):
    nome_arquivo_saida = "consolidado.xlsx"
    load_em_um_novo_excel(dados_exemplo, pasta_saida_mock, nome_arquivo_saida)

    caminho_arquivo_saida = os.path.join(pasta_saida_mock, nome_arquivo_saida)
    assert os.path.exists(
        caminho_arquivo_saida
    ), "O arquivo Excel de saída não foi criado."

    df_carregado = pd.read_excel(caminho_arquivo_saida)
    pd.testing.assert_frame_equal(df_carregado, dados_exemplo)
