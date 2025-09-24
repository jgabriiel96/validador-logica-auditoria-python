import pandas as pd
import locale
import os # Biblioteca para interagir com o sistema operacional, usada aqui para pegar a extensão do arquivo

# --- CONFIGURAções ---
# Agora você pode colocar 'sua_planilha.xlsx' ou 'seus_dados.csv'
NOME_ARQUIVO = 'valores.xlsx' 

# Substitua pelo nome exato da coluna que contém os valores
NOME_COLUNA_VALORES = 'Diferença' 

# --- FUNÇÕES AUXILIARES ---

def limpar_valor(valor_texto):
    """
    Função para converter uma string de moeda no formato da imagem para um número (float).
    """
    try:
        valor_texto = str(valor_texto)
        valor_limpo = valor_texto.split('(')[0].replace('R$', '').strip()
        return float(valor_limpo)
    except (ValueError, TypeError):
        return 0

# --- INÍCIO DO SCRIPT ---

# Configura a localização para o formato brasileiro
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Localidade 'pt_BR.UTF-8' não encontrada. Usando formatação padrão.")

# Tenta carregar e processar a planilha
try:
    print(f"Analisando o arquivo: '{NOME_ARQUIVO}'...")

    # --- LÓGICA DE DETECÇÃO DE FORMATO ---
    # Pega a extensão do arquivo para decidir como lê-lo
    _, extensao = os.path.splitext(NOME_ARQUIVO)

    if extensao == '.xlsx':
        df = pd.read_excel(NOME_ARQUIVO)
    elif extensao == '.csv':
        # CSVs no Brasil frequentemente usam ';' como separador. Se o seu usar ',', altere para sep=','
        df = pd.read_csv(NOME_ARQUIVO, sep=';') 
    else:
        # Se o formato não for suportado, levanta um erro claro
        raise ValueError(f"Formato de arquivo não suportado: '{extensao}'. Por favor, use .xlsx ou .csv.")
    
    print("Arquivo carregado com sucesso. Iniciando a análise...")

    # Verifica se a coluna especificada existe
    if NOME_COLUNA_VALORES not in df.columns:
        print(f"\nERRO: A coluna '{NOME_COLUNA_VALORES}' não foi encontrada.")
        print("Verifique se o nome está correto e se o separador do CSV está certo (',' ou ';').")
        print("Colunas disponíveis:", list(df.columns))
    else:
        # --- O CORAÇÃO DA ANÁLISE ---
        df['valor_numerico'] = df[NOME_COLUNA_VALORES].apply(limpar_valor)
        resultado_final = df['valor_numerico'].sum()
        total_pago_a_mais = df[df['valor_numerico'] > 0]['valor_numerico'].sum()
        total_pago_a_menos = df[df['valor_numerico'] < 0]['valor_numerico'].sum()
        
        # --- APRESENTAÇÃO DOS RESULTADOS ---
        print("\n--- Análise da Auditoria Concluída ---")
        print(f"Total de linhas analisadas: {len(df)}")
        print(f"Total pago a mais: {locale.currency(total_pago_a_mais, grouping=True)}")
        print(f"Total pago a menos: {locale.currency(total_pago_a_menos, grouping=True)}")
        print("------------------------------------------")
        print(f"RESULTADO FINAL DA AUDITORIA: {locale.currency(resultado_final, grouping=True)}")
        print("------------------------------------------")

        if resultado_final > 0:
            print("Conclusão: O balanço final indica que foram realizados pagamentos a mais.")
        elif resultado_final < 0:
            print("Conclusão: O balanço final indica que foram realizados pagamentos a menos.")
        else:
            print("Conclusão: O balanço final é zero.")

except FileNotFoundError:
    print(f"\nERRO: O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
    print("Verifique se o nome do arquivo está correto e se ele está na mesma pasta que o script.")
except ValueError as ve:
    print(f"\nERRO: {ve}")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")