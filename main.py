# -*- coding: utf-8 -*-
"""
Script Principal de Execução

Este é o ponto de entrada da aplicação. Ele é responsável por:
1. Definir as configurações de entrada (nome do arquivo e da coluna).
2. Carregar os dados do arquivo (.xlsx ou .csv).
3. Chamar as funções do módulo de auditoria para processar os dados.
4. Exibir o resultado final no terminal.
"""

# Importa as bibliotecas necessárias
import os  # Para interagir com o sistema de arquivos (verificar se o arquivo existe)
import pandas as pd  # Para carregar e manipular os dados do arquivo
from auditoria import analisar_dataframe, formatar_resultado  # Importa as funções do nosso módulo local

# --- CONFIGURAÇÕES ---
# Nesta seção, o usuário deve ajustar as variáveis de acordo com seu arquivo.

# Nome do arquivo de dados que será analisado.
# O arquivo deve estar na mesma pasta que este script.
NOME_ARQUIVO = "amostra_dados.xlsx"  # pode ser .csv também

# Nome exato da coluna da planilha que contém os valores a serem auditados.
NOME_COLUNA_VALORES = "Diferença"    # Ex: "Valor", "Diferença Apurada", etc.


# --- EXECUÇÃO ---
# O código abaixo será executado quando o script for chamado (ex: python main.py)

# Passo 1: Validação do arquivo de entrada
# Verifica se o arquivo configurado em NOME_ARQUIVO realmente existe na pasta.
if not os.path.exists(NOME_ARQUIVO):
    # Se não existir, exibe uma mensagem de erro clara e encerra o script.
    print(f"ERRO: O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
else:
    # Se o arquivo existe, o script continua.
    print(f"Carregando o arquivo: '{NOME_ARQUIVO}'...")

    # Passo 2: Carregamento dos dados
    # Extrai a extensão do nome do arquivo (ex: ".xlsx" ou ".csv")
    _, extensao = os.path.splitext(NOME_ARQUIVO)

    # Decide como carregar o arquivo com base na sua extensão
    if extensao == ".xlsx":
        # Se for um arquivo Excel, usa a função read_excel do Pandas
        df = pd.read_excel(NOME_ARQUIVO)
    elif extensao == ".csv":
        # Se for um arquivo CSV, usa a função read_csv com detecção automática de separador
        df = pd.read_csv(NOME_ARQUIVO, sep=None, engine="python")
    else:
        # Se a extensão não for suportada, levanta um erro
        raise ValueError(f"Formato de arquivo não suportado: '{extensao}'. Use .xlsx ou .csv.")

    print("Arquivo carregado com sucesso!")

    # Passo 3: Análise e Exibição dos Resultados
    # O bloco try...except garante que, se ocorrer um erro durante a análise,
    # o programa mostrará uma mensagem amigável em vez de quebrar.
    try:
        # Chama a função de análise, passando o DataFrame carregado e o nome da coluna
        resultado = analisar_dataframe(df, NOME_COLUNA_VALORES)

        # Imprime um cabeçalho para o relatório
        print("\n--- Análise da Auditoria ---")
        
        # Chama a função de formatação e imprime o resultado final no terminal
        print(formatar_resultado(resultado))

    except Exception as e:
        # Se qualquer erro ocorrer dentro do bloco 'try', ele será capturado
        # e uma mensagem de erro será exibida.
        print(f"Ocorreu um erro durante a análise: {e}")