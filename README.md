# Processamento de Linguagem Natural e Extração de Dados Culinários

Trabalho prático desenvolvido para a disciplina de Inteligência Artificial da Universidade Federal de São João del-Rei (UFSJ).

Enquanto o primeiro módulo do projeto é focado em aprendizado supervisionado e sistemas de recomendação, este repositório concentra-se na etapa de **coleta, processamento e estruturação de dados culinários** por meio de técnicas de **Web Scraping**, **Processamento de Linguagem Natural (PLN)** e **IA Generativa**.

O objetivo é transformar receitas disponíveis na web em uma base de dados estruturada, padronizada e adequada para aplicações de mineração de dados e sistemas inteligentes.

---

## Arquitetura do Pipeline

Para evitar a dependência exclusiva de bases de dados prontas, foi desenvolvido um pipeline completo de extração e tratamento de informações culinárias.

O fluxo é dividido em três etapas principais:

### 1. Coleta e Web Scraping

Responsável pela aquisição dos dados diretamente de sites de receitas.

Principais componentes:

* `get_links.py` — coleta automática de URLs de receitas.
* `requests.py` — download do conteúdo HTML das páginas.
* `recipe_links.txt` — armazenamento das URLs coletadas.

Nesta etapa são obtidos os dados brutos que servirão como entrada para o processamento textual.

---

### 2. Limpeza e Tratamento Textual

Responsável pela remoção de ruídos e extração das informações relevantes.

Principais componentes:

* `treat.py`
* `passos.py`

Entre as tarefas executadas estão:

* Remoção de tags HTML.
* Limpeza de caracteres especiais.
* Padronização textual.
* Extração de ingredientes.
* Extração do modo de preparo.

O resultado é um conjunto de textos mais consistentes e adequados para processamento posterior.

---

### 3. Normalização e Estruturação dos Dados

Responsável pela transformação dos textos em informações estruturadas.

Principais componentes:

* `gemini.py`
* `merged.json`

Nesta etapa são utilizadas técnicas de PLN e modelos de linguagem para:

* Reconhecimento de entidades culinárias.
* Padronização de nomes de ingredientes.
* Identificação de unidades de medida.
* Normalização de quantidades.
* Estruturação dos dados em formato JSON.

O resultado final é uma base de dados consistente e pronta para aplicações analíticas ou sistemas de recomendação.

---

## Tecnologias Utilizadas

* Python
* Pandas
* Requests
* BeautifulSoup (bs4)
* Google Generative AI (Gemini)
* Jupyter Notebook

---

## Requisitos e Dependências

Instale as dependências necessárias:

```bash
pip install pandas requests beautifulsoup4 google-generativeai notebook
```

---

## Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Criar um Ambiente Virtual

```bash
python -m venv venv
```

Ativação no Windows:

```bash
venv\Scripts\activate
```

Ativação no Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install pandas requests beautifulsoup4 google-generativeai notebook
```

### 4. Executar o Pipeline

#### Coleta de Dados

Utilize os scripts da pasta `scrapper` para coletar novas receitas e gerar listas de URLs.

#### Processamento dos Dados

Utilize os scripts da pasta `process` para:

* Limpeza dos textos.
* Extração de ingredientes.
* Extração dos passos de preparo.
* Normalização dos dados.

#### Testes e Validação

Para visualizar resultados intermediários e validar o pipeline:

```bash
jupyter notebook
```

Abra o arquivo:

```text
teste.ipynb
```

---

## Estrutura do Projeto

```text
.
├── scrapper/
│   ├── get_links.py
│   ├── requests.py
│   └── recipe_links.txt
│
├── process/
│   ├── treat.py
│   ├── passos.py
│   ├── load.py
│   └── gemini.py
│
├── teste.ipynb
│
├── merged.json
├── steps.json
└── recipe_links.txt
```

### Principais Arquivos

| Arquivo        | Descrição                             |
| -------------- | ------------------------------------- |
| `get_links.py` | Coleta URLs de receitas               |
| `requests.py`  | Realiza requisições e obtém HTML      |
| `treat.py`     | Limpeza e padronização textual        |
| `passos.py`    | Processamento do modo de preparo      |
| `load.py`      | Carregamento e integração dos dados   |
| `gemini.py`    | Estruturação utilizando IA Generativa |
| `teste.ipynb`  | Ambiente de prototipação e testes     |

---

## Aplicações

A base produzida por este projeto pode ser utilizada em:

* Sistemas de recomendação de receitas.
* Motores de busca culinária.
* Mineração de dados alimentares.
* Análise de ingredientes.
* Construção de datasets para Machine Learning.
* Aplicações de Processamento de Linguagem Natural.

---

## Desenvolvedores

* André Arcuri Martins
* Gabriel da Silva Souza
* Giulia Mota Apinagés dos Santos
* Guilherme De Luca Testoni Neiva Pereira
* José Vitor Santos Alves
