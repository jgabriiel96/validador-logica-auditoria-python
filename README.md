# Validador de Lógica de Auditoria com Python

> Automação sem QA é só um jeito mais rápido de cometer erros em escala.

## 📝 Contexto do Projeto

Antes de automatizar a auditoria com diversas linhas financeiras, fizemos a pergunta mais importante: **"Como podemos ter 100% de certeza de que a nossa lógica de cálculo está correta?"**

Em projetos de automação, especialmente quando lidamos com dados financeiros, a pressa para entregar o produto final pode ser traiçoeira. Um pequeno erro na interpretação de um dado, quando multiplicado por milhares de linhas, pode levar a decisões desastrosas.

É por isso que, antes de construir a pipeline completa, demos um passo atrás e focamos em **Quality Assurance**. O que começou como um script de validação (PoC) evoluiu para uma ferramenta mais robusta, com a lógica de negócio modularizada e coberta por testes automatizados, garantindo que a base da automação seja sólida e confiável.

### O Processo com Pandas

Com a biblioteca Pandas, o processo foi direto:

* 💻 **`pd.read_excel()` / `pd.read_csv()`**: Carregamos o arquivo de amostra para um DataFrame, com detecção automática do formato.
* 🔧 **`.apply()` com uma função de limpeza**: Aqui está a mágica. Uma pequena função para extrair apenas o valor numérico de cada célula, tratando exceções e garantindo que `"R$ -16.82 (pago a menos)"` se tornasse o float `-16.82`.
* 📊 **`.sum()`**: Com a coluna de dados finalmente limpa e numérica, uma simples soma nos deu o resultado da auditoria da amostra. Preciso e instantâneo.

### Ganhos da Abordagem de QA

Essa pequena etapa de validação nos deu a luz verde e a confiança necessária para integrar essa função na automação completa. Os benefícios são claros:

* **Velocidade**: O que levaria horas de verificação manual, agora leva segundos.
* **Escalabilidade**: A lógica validada funciona para 10 mil ou 10 milhões de linhas.
* **Confiabilidade**: A automação validada e agora coberta por testes com **Pytest** elimina o erro humano e garante a manutenção futura do código.
* **Inteligência**: Abre portas para análises mais estratégicas: qual a média das diferenças? Qual o maior valor pago a menos?

Isso é desmistificar a automação. Não é um botão mágico. É um processo de engenharia, e toda boa engenharia se baseia em testes rigorosos. Testar a lógica em pequena escala antes de escalar é a diferença entre um projeto de sucesso e uma dor de cabeça cara.

---

## 🚀 Como Usar

Para executar este script de validação em sua máquina local, siga os passos abaixo.

### Pré-requisitos
- Python 3.x
- Git

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/jgabriiel96/validador-logica-auditoria-python.git](https://github.com/jgabriiel96/validador-logica-auditoria-python.git)
    cd validador-logica-auditoria-python
    ```

2.  **(Recomendado) Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows: venv\Scripts\activate
    # No Linux/macOS: source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Execução da Análise

1.  Certifique-se de que o arquivo de amostra (`amostra_dados.xlsx` ou `.csv`) está na pasta.
2.  No script `main.py`, ajuste as variáveis `NOME_ARQUIVO` e `NOME_COLUNA_VALORES` conforme sua necessidade.
3.  Execute o script principal pelo terminal:
    ```bash
    python main.py
    ```
O resultado da análise será exibido no terminal.

## 🧪 Como Executar os Testes

Para verificar a integridade do código e garantir que todas as funções de negócio operam como esperado, execute a suíte de testes automatizados com Pytest.

Com o ambiente virtual ativado, execute na raiz do projeto:

```bash
pytest
```