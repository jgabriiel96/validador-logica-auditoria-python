import os
import pandas as pd
from auditoria import analisar_dataframe, formatar_resultado

# --- CONFIGURAÇÕES ---
NOME_ARQUIVO = "amostra_dados.xlsx"  # pode ser .csv também
NOME_COLUNA_VALORES = "Diferença"    # coluna com os valores a analisar

# --- EXECUÇÃO ---
if not os.path.exists(NOME_ARQUIVO):
    print(f"ERRO: O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
else:
    _, extensao = os.path.splitext(NOME_ARQUIVO)

    if extensao == ".xlsx":
        df = pd.read_excel(NOME_ARQUIVO)
    elif extensao == ".csv":
        df = pd.read_csv(NOME_ARQUIVO, sep=None, engine="python")
    else:
        raise ValueError(f"Formato não suportado: {extensao}")

    try:
        resultado = analisar_dataframe(df, NOME_COLUNA_VALORES)
        print("\n--- Análise da Auditoria ---")
        print(formatar_resultado(resultado))
    except Exception as e:
        print(f"Erro durante análise: {e}")