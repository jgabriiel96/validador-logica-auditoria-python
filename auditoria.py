import pandas as pd
import locale

def limpar_valor(valor_texto: str) -> float:
    """
    Converte uma string de moeda para float, lidando com os formatos
    'R$ 1.234,56' (padrão BR) e 'R$ 1234.56' (padrão direto/US).
    """
    try:
        valor_texto = str(valor_texto)
        # Remove o prefixo "R$" e qualquer texto extra como " (pago a mais)"
        valor_limpo = valor_texto.split('(')[0].replace('R$', '').strip()

        # Verifica se o formato é brasileiro (contém vírgula como decimal)
        if ',' in valor_limpo and '.' in valor_limpo:
            # Formato "1.234,56" -> remove o ponto de milhar, depois troca a vírgula por ponto
            valor_limpo = valor_limpo.replace('.', '').replace(',', '.')
        elif ',' in valor_limpo:
            # Formato "1234,56" -> apenas troca a vírgula por ponto
             valor_limpo = valor_limpo.replace(',', '.')
        
        # Se não houver vírgula, o formato já é "1234.56", então não fazemos nada com o ponto.
        # Apenas removemos vírgulas que possam ser de milhar (ex: "1,234.56")
        valor_limpo = valor_limpo.replace(',', '')

        return float(valor_limpo)
    except (ValueError, TypeError):
        return 0.0

def analisar_dataframe(df: pd.DataFrame, coluna: str) -> dict:
    """
    Recebe um DataFrame e o nome da coluna de valores e retorna um dicionário com os resultados.
    """
    if coluna not in df.columns:
        raise ValueError(f"A coluna '{coluna}' não existe no DataFrame.")

    df['valor_numerico'] = df[coluna].apply(limpar_valor)
    resultado_final = df['valor_numerico'].sum()
    total_pago_a_mais = df[df['valor_numerico'] > 0]['valor_numerico'].sum()
    total_pago_a_menos = df[df['valor_numerico'] < 0]['valor_numerico'].sum()

    return {
        "total_linhas": len(df),
        "total_pago_a_mais": total_pago_a_mais,
        "total_pago_a_menos": total_pago_a_menos,
        "resultado_final": resultado_final,
    }


def formatar_resultado(resultado: dict) -> str:
    """
    Formata a saída final da auditoria em texto.
    """
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        pass  # Se não tiver suporte, segue padrão

    resumo = []
    resumo.append(f"Total de linhas analisadas: {resultado['total_linhas']}")
    resumo.append(f"Total pago a mais: {locale.currency(resultado['total_pago_a_mais'], grouping=True)}")
    resumo.append(f"Total pago a menos: {locale.currency(resultado['total_pago_a_menos'], grouping=True)}")
    resumo.append(f"RESULTADO FINAL DA AUDITORIA: {locale.currency(resultado['resultado_final'], grouping=True)}")

    if resultado['resultado_final'] > 0:
        resumo.append(f"Conclusão: O balanço final indica que foi realizado {locale.currency(resultado['resultado_final'], grouping=True)} a mais.")
    elif resultado['resultado_final'] < 0:
        resumo.append(f"Conclusão: O balanço final indica que foi realizado {locale.currency(resultado['resultado_final'], grouping=True)} a menos.")
    else:
        resumo.append("Conclusão: O balanço final é zero.")

    return "\n".join(resumo)