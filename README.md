\# Validador de Lógica de Auditoria com Python



> Automação sem QA é só um jeito mais rápido de cometer erros em escala.



\## 📝 Contexto do Projeto



Antes de automatizar a auditoria com diversas linhas financeiras, fizemos a pergunta mais importante: \*\*"Como podemos ter 100% de certeza de que a nossa lógica de cálculo está correta?"\*\*



Em projetos de automação, especialmente quando lidamos com dados financeiros, a pressa para entregar o produto final pode ser traiçoeira. Um pequeno erro na interpretação de um dado, quando multiplicado por milhares de linhas, pode levar a decisões desastrosas.



É por isso que, antes de construir a pipeline completa, demos um passo atrás e focamos em \*\*Quality Assurance\*\*.



Para isso, criamos um script de teste focado usando Python e Pandas. O objetivo não era processar o arquivo inteiro, mas sim criar uma "prova de conceiro" (PoC) para validar nossa função de limpeza de dados em um ambiente controlado.



\### O Processo com Pandas



Com a biblioteca Pandas, o processo foi direto:



\* 💻 \*\*`pd.read\_excel()` / `pd.read\_csv()`\*\*: Carregamos o arquivo de amostra para um DataFrame, com detecção automática do formato.

\* 🔧 \*\*`.apply()` com uma função de limpeza\*\*: Aqui está a mágica. Uma pequena função para extrair apenas o valor numérico de cada célula, tratando exceções e garantindo que `"R$ -16.82 (pago a menos)"` se tornasse o float `-16.82`.

\* 📊 \*\*`.sum()`\*\*: Com a coluna de dados finalmente limpa e numérica, uma simples soma nos deu o resultado da auditoria da amostra. Preciso e instantâneo.



\### Ganhos da Abordagem de QA



Essa pequena etapa de validação nos deu a luz verde e a confiança necessária para integrar essa função na automação completa, sabendo que o pilar do nosso processo estava sólido. Os benefícios são claros:



\* \*\*Velocidade\*\*: O que levaria horas de verificação manual, agora leva segundos.

\* \*\*Escalabilidade\*\*: A lógica validada funciona para 10 mil ou 10 milhões de linhas.

\* \*\*Confiabilidade\*\*: A automação validada elimina o erro humano no cálculo.

\* \*\*Inteligência\*\*: Abre portas para análises mais estratégicas: qual a média das diferenças? Qual o maior valor pago a menos? Quais fornecedores apresentam mais inconsistências?



Isso é desmistificar a automação. Não é um botão mágico. É um processo de engenharia, e toda boa engenharia se baseia em testes rigorosos. Testar a lógica em pequena escala antes de escalar é a diferença entre um projeto de sucesso e uma dor de cabeça cara.



---



\## 🚀 Como Usar



Para executar este script de validação em sua máquina local, siga os passos abaixo.



\### Pré-requisitos

\- Python 3.x

\- Git



\### Instalação



1\.  \*\*Clone o repositório:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/jgabriiel96/validador-logica-auditoria-python.git](https://github.com/jgabriiel96/validador-logica-auditoria-python.git)

&nbsp;   cd validador-logica-auditoria-python

&nbsp;   ```



2\.  \*\*(Opcional, mas recomendado) Crie e ative um ambiente virtual:\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   source venv/bin/activate  # No Windows: venv\\Scripts\\activate

&nbsp;   ```



3\.  \*\*Instale as dependências:\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



\### Execução



1\.  Certifique-se de que o arquivo de amostra (`amostra\_dados.csv` ou `.xlsx`) está na pasta.

2\.  No script `analise\_auditoria.py`, ajuste as variáveis `NOME\_ARQUIVO` e `NOME\_COLUNA\_VALORES` conforme sua necessidade.

3\.  Execute o script pelo terminal:

&nbsp;   ```bash

&nbsp;   python analise\_auditoria.py

&nbsp;   ```

xx