import pandas as pd
import pytest
from auditoria import limpar_valor, analisar_dataframe, formatar_resultado

def test_limpar_valor():
    assert limpar_valor("R$ 1.234,56") == 1234.56
    assert limpar_valor("R$ 0,00") == 0.0
    assert limpar_valor(None) == 0.0
    assert limpar_valor("texto inválido") == 0.0


def test_analisar_dataframe():
    dados = {
        "Diferença": ["R$ 100,00", "R$ -50,00", "R$ 200,00"]
    }
    df = pd.DataFrame(dados)

    resultado = analisar_dataframe(df, "Diferença")

    assert resultado["total_linhas"] == 3
    assert resultado["total_pago_a_mais"] == 300.0
    assert resultado["total_pago_a_menos"] == -50.0
    assert resultado["resultado_final"] == 250.0


def test_analisar_dataframe_coluna_invalida():
    df = pd.DataFrame({"OutraColuna": ["R$ 10,00"]})
    with pytest.raises(ValueError):
        analisar_dataframe(df, "Diferença")


def test_formatar_resultado():
    resultado = {
        "total_linhas": 3,
        "total_pago_a_mais": 300.0,
        "total_pago_a_menos": -50.0,
        "resultado_final": 250.0,
    }
    saida = formatar_resultado(resultado)
    assert "RESULTADO FINAL DA AUDITORIA" in saida
    assert "a mais" in saida