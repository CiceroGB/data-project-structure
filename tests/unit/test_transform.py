import pandas as pd
import pytest

from app.etl import transforma_em_um_unico


def test_transforma_em_um_unico_sucesso():
    # Cria DataFrames de teste
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})

    # Lista com os DataFrames de teste
    all_data = [df1, df2]

    # Executa a função
    result_df = transforma_em_um_unico(all_data)

    # Verifica se o resultado é a concatenação correta dos DataFrames
    expected_df = pd.concat([df1, df2], ignore_index=True)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_transforma_em_um_unico_lista_vazia():
    # Verifica se a função levanta uma ValueError com lista vazia
    with pytest.raises(ValueError) as exc_info:
        transforma_em_um_unico([])

    assert "No data to transform" in str(exc_info.value)


def test_transforma_em_um_unico_lista_invalida():
    # Verifica se a função levanta uma ValueError com lista contendo elementos não-DataFrame
    with pytest.raises(ValueError) as exc_info:
        transforma_em_um_unico([1, "not a dataframe"])

    assert "All elements in the list must be pandas DataFrames" in str(exc_info.value)
