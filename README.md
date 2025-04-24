Repositório dedicado aos meus estudos do curso de Python Avançado oferecido pelo canal [DATAV](https://www.youtube.com/@datav9580) no YouTube, além de um projeto prático de ETL e análise de dados com Python, Power BI e Figma.

Aqui estão reunidos scripts, anotações e exemplos práticos dos conteúdos abordados no curso, além de um projeto completo de análise de acidentes rodoviários no Brasil.

---

## 📚 Conteúdos estudados no curso (em andamento):

- ✅ **Funções:**
  - `def`
  - Função `lambda`
- ✅ **Estruturas de repetição:**
  - `while`
  - `for`
- ✅ **Condicionais:**
  - `if`
  - Tratamento de erros com `try` / `except`
- ✅ **Métodos de string:**
  - `capitalize`
  - `upper`
  - `lower`
  - `isdigit`
  - `replace`
  - `split`
  - `startswith` / `endswith`
  - `strip`
- ✅ **Estruturas de dados:**
  - Listas
    - Criação e manipulação
    - Fatiamento (`lista[início:fim:passo]`)
    - Métodos como `.append()`, `.remove()`, `.count()` etc.
  - Dicionários
  - Tuplas
- ✅ **Módulos e pacotes:**
  - `datetime`
  - `math`
  - `random`
  - `time`
- ✅ **Estatística básica**

> ⚠️ Novos conteúdos serão adicionados em futuros commits.



Este repositório contém um projeto de ETL e análise de dados utilizando Python (pandas), Power BI e Figma, baseado em registros de acidentes rodoviários da Polícia Rodoviária Federal (PRF) entre 2017 e 2023. O objetivo foi estruturar e transformar os dados para facilitar a análise e geração de insights estratégicos.

🚀 Tecnologias Utilizadas
Python (pandas) – Processamento e transformação dos dados (ETL)
Power BI – Modelagem e visualização dos dados
Figma – Design do dashboard para melhor experiência visual
⚙️ Processamento dos Dados com Python (ETL)
1️⃣ Extração e Pré-processamento:

O dataset original foi obtido no Kaggle, contendo quase 1 milhão de registros armazenados em JSON (1.282 KB).
Para otimizar a performance, o arquivo foi convertido para CSV (382 KB), reduzindo significativamente o tempo de leitura e processamento.
2️⃣ Tratamento e Limpeza dos Dados:

Remoção de colunas irrelevantes e ajustes na tipagem dos dados.
Tratamento de valores nulos e inconsistências.
3️⃣ Modelagem e Organização:

Estruturação do modelo relacional, separando os dados em tabelas Fato e Dimensão para otimizar o desempenho no Power BI.
Remoção de duplicatas e criação de índices otimizados.
4️⃣ Exportação dos Dados:

Cada tabela processada foi exportada para ser utilizada no Power BI, garantindo uma arquitetura eficiente para visualização.
📊 Storytelling com Dados
Após o processamento, os dados revelaram insights críticos sobre a segurança viária no Brasil:

🔹 Entre 2017 e 2023, ocorreram aproximadamente 29 mil mortes em acidentes rodoviários. Isso representa uma média de 4 mil mortes por ano, equivalente a 3,4% do total de acidentes registrados.

🔹 Distribuição por Horário:

Os acidentes são significativamente mais frequentes durante o pleno dia (564 mil registros), representando 80,1% a mais do que no período da plena noite (313 mil registros).
Esse dado sugere que fatores como tráfego intenso, distração e menor fiscalização diurna podem contribuir para o aumento das ocorrências.
🔹 Distribuição Geográfica:

Minas Gerais lidera o ranking com 103.609 ocorrências, registrando 10,4% a mais que o segundo estado com maior número de acidentes, Santa Catarina (93.765 casos).
Ambos os estados fazem parte das principais rotas rodoviárias do Brasil, o que reforça a necessidade de fiscalização rigorosa e campanhas educativas.
🔹 Conclusão e Recomendações:
Para reduzir a incidência de acidentes, recomenda-se:
✅ Aumento da fiscalização eletrônica e implantação de barreiras em trechos críticos.
✅ Campanhas de conscientização sobre direção defensiva e segurança no trânsito.
✅ Melhoria na sinalização e infraestrutura viária, especialmente em rodovias de alto tráfego.

📌 Como Utilizar Este Repositório
Pré-requisitos
Certifique-se de ter instalado:

Python 3.x
Pandas (pip install pandas)
Jupyter Notebook (opcional, para exploração interativa)
Executando o ETL
Clone o repositório e execute o script de ETL:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
python etl_acidentes.py
Os dados transformados serão salvos em um diretório específico para importação no Power BI.

🏆 Resultados
O uso de Python (pandas) para ETL, Power BI para modelagem e visualização e Figma para design resultou em um dashboard dinâmico e estratégico, permitindo uma análise clara e detalhada dos acidentes rodoviários da PRF.

🔗 Acesse o dashboard interativo aqui (https://lnkd.in/dGS58VPx).

📌 Repositório atualizado continuamente com novos insights e melhorias!

📧 Contato
Se tiver dúvidas, sugestões ou quiser contribuir para o projeto, entre em contato:
📩 Ribeirodouglas7007@gmail.com
🌎 https://www.linkedin.com/in/douglas-ribeiro-da-silva/
