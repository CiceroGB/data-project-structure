"""Tests for unit functionalities."""

import pandas as pd
import pytest

from app.etl import transforma_em_um_unico


def test_transforma_em_um_unico_com_dados_validos():
    # Cria DataFrames de teste
    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]})

    # Concatena os DataFrames manualmente para servir de referência
    expected_df = pd.concat([df1, df2], ignore_index=True)

    # Chama a função com os DataFrames de teste
    result_df = transforma_em_um_unico([df1, df2])

    # Verifica se o DataFrame resultante é igual ao esperado
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_transforma_em_um_unico_sem_dados():
    # Verifica se a função lança ValueError quando a lista está vazia
    with pytest.raises(ValueError):
        transforma_em_um_unico([])
