# -*- coding: utf-8 -*-
"""
Módulo de Auditoria Financeira

Este módulo contém as funções principais para limpar, analisar e formatar
dados de auditoria a partir de um DataFrame do Pandas.
"""

import pandas as pd
import locale

def limpar_valor(valor_texto: str) -> float:
    """
    Converte uma string de moeda para float, lidando com os formatos
    'R$ 1.234,56' (padrão BR) e 'R$ 1234.56' (padrão direto/US).

    Args:
        valor_texto (str): O texto a ser convertido (ex: "R$ -50,25 (pago a menos)").

    Returns:
        float: O valor numérico extraído. Retorna 0.0 em caso de erro.
    """
    try:
        # Garante que o input seja uma string para evitar erros
        valor_texto = str(valor_texto)

        # 1. Remove textos auxiliares como " (pago a mais)" pegando apenas a parte antes do "("
        # 2. Remove o símbolo da moeda "R$"
        # 3. Remove espaços em branco no início e no fim
        valor_limpo = valor_texto.split('(')[0].replace('R$', '').strip()

        # --- Lógica para tratar múltiplos formatos de número ---

        # Se contém tanto '.' quanto ',', é o formato brasileiro completo (ex: "1.234,56")
        if ',' in valor_limpo and '.' in valor_limpo:
            # Remove o separador de milhar ('.') e troca o decimal (',') por ponto
            valor_limpo = valor_limpo.replace('.', '').replace(',', '.')
        # Se contém apenas ',', é o formato brasileiro sem milhar (ex: "1234,56")
        elif ',' in valor_limpo:
            # Apenas troca a vírgula decimal por ponto
             valor_limpo = valor_limpo.replace(',', '.')
        
        # Se não houver vírgula, assume-se que o formato já é o padrão americano/internacional
        # com ponto decimal (ex: "1234.56").
        # A linha abaixo serve como uma segurança para remover vírgulas de milhar no formato americano (ex: "1,234.56")
        valor_limpo = valor_limpo.replace(',', '')

        # Converte a string limpa e padronizada para float
        return float(valor_limpo)
    
    # Em caso de qualquer erro de conversão (ex: texto vazio, formato inesperado), retorna 0.0
    except (ValueError, TypeError):
        return 0.0


def analisar_dataframe(df: pd.DataFrame, coluna: str) -> dict:
    """
    Recebe um DataFrame e o nome da coluna de valores e retorna um dicionário com os resultados da análise.

    Args:
        df (pd.DataFrame): O DataFrame contendo os dados da auditoria.
        coluna (str): O nome da coluna que contém os valores em texto.

    Returns:
        dict: Um dicionário com os totais e o resultado final.
    """
    # Validação: Verifica se a coluna informada realmente existe no DataFrame
    if coluna not in df.columns:
        # Se não existir, levanta um erro claro para o usuário
        raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")

    # Aplica a função de limpeza em cada linha da coluna especificada para criar uma nova coluna numérica
    df['valor_numerico'] = df[coluna].apply(limpar_valor)

    # Calcula as métricas da auditoria usando a nova coluna numérica
    resultado_final = df['valor_numerico'].sum()
    total_pago_a_mais = df[df['valor_numerico'] > 0]['valor_numerico'].sum()
    total_pago_a_menos = df[df['valor_numerico'] < 0]['valor_numerico'].sum()

    # Retorna todos os resultados em um dicionário bem estruturado
    return {
        "total_linhas": len(df),
        "total_pago_a_mais": total_pago_a_mais,
        "total_pago_a_menos": total_pago_a_menos,
        "resultado_final": resultado_final,
    }


def formatar_resultado(resultado: dict) -> str:
    """
    Formata o dicionário de resultados em um texto legível e pronto para exibição.

    Args:
        resultado (dict): O dicionário gerado pela função analisar_dataframe.

    Returns:
        str: Uma string multi-linha com o relatório final da auditoria.
    """
    # Tenta configurar a localidade para o Português do Brasil para formatar a moeda corretamente (ex: R$ 1.234,56)
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        # Se o sistema não tiver suporte à localidade, o programa continua sem quebrar, usando a formatação padrão
        pass

    # Cria uma lista de strings que formarão o relatório
    resumo = []
    resumo.append(f"Total de linhas analisadas: {resultado['total_linhas']}")
    resumo.append(f"Total pago a mais: {locale.currency(resultado['total_pago_a_mais'], grouping=True)}")
    resumo.append(f"Total pago a menos: {locale.currency(resultado['total_pago_a_menos'], grouping=True)}")
    resumo.append(f"RESULTADO FINAL DA AUDITORIA: {locale.currency(resultado['resultado_final'], grouping=True)}")

    # Adiciona uma linha de conclusão baseada no resultado final
    if resultado['resultado_final'] > 0:
        resumo.append(f"Conclusão: O balanço final indica que foi realizado {locale.currency(resultado['resultado_final'], grouping=True)} a mais.")
    elif resultado['resultado_final'] < 0:
        resumo.append(f"Conclusão: O balanço final indica que foi realizado {locale.currency(resultado['resultado_final'], grouping=True)} a menos.")
    else:
        resumo.append("Conclusão: O balanço final é zero.")

    # Junta todas as linhas do relatório em uma única string, separadas por quebras de linha
    return "\n".join(resumo)