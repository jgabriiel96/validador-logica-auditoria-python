# -*- coding: utf-8 -*-
"""
Arquivo de Testes Automatizados

Este arquivo contém os testes unitários para as funções do módulo `auditoria.py`.
Ele utiliza a biblioteca Pytest para verificar se cada função se comporta como o esperado
em diferentes cenários.

Para executar os testes, rode o comando `pytest` no terminal na raiz do projeto.
"""

# Importa as bibliotecas necessárias
import pandas as pd  # Para criar DataFrames de teste
import pytest      # Framework de testes
from auditoria import limpar_valor, analisar_dataframe, formatar_resultado # Importa as funções que vamos testar

# --- Testes para a função limpar_valor ---

def test_limpar_valor():
    """
    Testa a função `limpar_valor` com diferentes formatos de entrada para garantir
    que a conversão para float seja feita corretamente.
    """
    # Cenário 1: Testa um valor padrão no formato brasileiro com separador de milhar.
    assert limpar_valor("R$ 1.234,56") == 1234.56
    
    # Cenário 2: Testa o valor zero.
    assert limpar_valor("R$ 0,00") == 0.0
    
    # Cenário 3: Testa um input nulo (None). A função deve retornar 0.0 e não quebrar.
    assert limpar_valor(None) == 0.0
    
    # Cenário 4: Testa um texto que não é um número. A função deve retornar 0.0 e não quebrar.
    assert limpar_valor("texto inválido") == 0.0


# --- Testes para a função analisar_dataframe ---

def test_analisar_dataframe():
    """
    Testa a função `analisar_dataframe` com um DataFrame válido para verificar
    se os cálculos de totais e resultado final estão corretos.
    """
    # 1. PREPARAÇÃO (Arrange): Cria um DataFrame de exemplo com dados de teste.
    dados = {
        "Diferença": ["R$ 100,00", "R$ -50,00", "R$ 200,00"]
    }
    df = pd.DataFrame(dados)

    # 2. EXECUÇÃO (Act): Chama a função que queremos testar.
    resultado = analisar_dataframe(df, "Diferença")

    # 3. VERIFICAÇÃO (Assert): Compara o resultado obtido com o resultado esperado.
    assert resultado["total_linhas"] == 3
    assert resultado["total_pago_a_mais"] == 300.0
    assert resultado["total_pago_a_menos"] == -50.0
    assert resultado["resultado_final"] == 250.0


def test_analisar_dataframe_coluna_invalida():
    """
    Testa se a função `analisar_dataframe` levanta um erro do tipo `ValueError`
    quando um nome de coluna que não existe é fornecido.
    """
    # PREPARAÇÃO: Cria um DataFrame que não possui a coluna "Diferença".
    df = pd.DataFrame({"OutraColuna": ["R$ 10,00"]})
    
    # EXECUÇÃO E VERIFICAÇÃO:
    # O `pytest.raises(ValueError)` é um gerenciador de contexto que confirma
    # que o código dentro dele DEVE levantar um erro do tipo ValueError.
    # Se o erro não for levantado, o teste falha.
    with pytest.raises(ValueError):
        analisar_dataframe(df, "Diferença")


# --- Testes para a função formatar_resultado ---

def test_formatar_resultado():
    """
    Testa a função `formatar_resultado` para garantir que o texto de saída
    contenha as informações chave esperadas.
    """
    # PREPARAÇÃO: Cria um dicionário de resultado de exemplo.
    resultado = {
        "total_linhas": 3,
        "total_pago_a_mais": 300.0,
        "total_pago_a_menos": -50.0,
        "resultado_final": 250.0,
    }
    
    # EXECUÇÃO: Chama a função de formatação.
    saida = formatar_resultado(resultado)

    # VERIFICAÇÃO: Em vez de testar o texto exato (que pode mudar), verificamos
    # se frases importantes estão presentes na string de saída.
    assert "RESULTADO FINAL DA AUDITORIA" in saida
    assert "a mais" in saida # Verifica se a conclusão está correta para um resultado positivo.

def test_formatar_resultado_negativo():
    """
    Testa a função `formatar_resultado` para garantir que a conclusão
    está correta quando o resultado final da auditoria é negativo.
    """
    # PREPARAÇÃO: Cria um dicionário de resultado com um valor final negativo.
    resultado = {
        "total_linhas": 3,
        "total_pago_a_mais": 50.0,
        "total_pago_a_menos": -300.0,
        "resultado_final": -250.0,
    }
    
    # EXECUÇÃO: Chama a função de formatação.
    saida = formatar_resultado(resultado)

    # VERIFICAÇÃO: Garante que a conclusão contém a frase "a menos".
    assert "RESULTADO FINAL DA AUDITORIA" in saida
    assert "a menos" in saida