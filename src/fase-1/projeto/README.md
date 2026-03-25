# Farm Tech Solution - Play no desenvolvimento

Este projeto é uma solução tecnológica para a Startup FarmTech Solutions, focado em auxiliar fazendas na transição para a Agricultura Digital. A aplicação integra Python para o manejo de dados e insumos, e R para análises estatísticas e integração com APIs meteorológicas.

---

## 📂 Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`main.py`**: Ponto de entrada da aplicação Python. Contém o menu principal e a lógica de interação com o usuário.
- **`utils.py`**: Funções auxiliares para cálculos de manejo de insumos, operações de CRUD (Create, Read, Update, Delete) e persistência de dados.
- **`data.json`**: Arquivo utilizado para armazenar os dados inseridos pelo usuário (vetores de culturas e cálculos).
- **`analise.R`**: Script em R responsável por realizar análises estatísticas básicas (média, desvio padrão, etc.) sobre os dados gerados.
- **`wheater.r`**: Script em R que se conecta à API HG Brasil Weather para buscar e exibir a previsão do tempo de uma cidade informada.
- **`.env`**: Arquivo de configuração para variáveis de ambiente (contém a `API_KEY` para a previsão do tempo).
- **`requirements.txt`**: Lista de dependências Python necessárias para o projeto.
- **`Uso de VANTs em Agricultura de Precisão.pdf`**: Resumo do artigo solicitado na disciplina de Formação Social.

---

## 🛠️ Dependências

### Python
As bibliotecas necessárias estão listadas no `requirements.txt`:
- `tabulate`: Para formatação de tabelas no terminal.

### R
Os seguintes pacotes devem estar instalados no ambiente R:
- `httr2`: Para requisições HTTP à API.
- `dotenv`: Para leitura do arquivo `.env`.
- `jsonlite`: Para processamento de dados JSON.

---

## 🚀 Como Utilizar

### 1. Configuração Inicial
Clone o repositório e navegue até a pasta do projeto:
```shell
git clone git@github.com:kaique-cadimiel-dev/curso-fiap-machine-learning.git
cd src/fase-1/projeto
```

### 2. Instalação das Dependências
Instale as dependências do Python:
```shell
pip install -r requirements.txt
```

Certifique-se de que os pacotes do R estão instalados. Você pode instalá-los via terminal R:
```R
install.packages(c("httr2", "dotenv", "jsonlite"))
```

### 3. Configuração da API Key
Crie ou edite o arquivo `.env` na raiz do projeto e adicione sua chave da HG Brasil Weather:
```env
API_KEY=sua_chave_aqui
```

### 4. Execução
Inicie a aplicação principal:
```shell
python main.py
```

### Menu de Opções:
1.  **Inserir dados**: Calcula o manejo de insumos para culturas (ex: Café, Soja) e salva.
2.  **Listar dados**: Exibe os dados armazenados em formato de tabela.
3.  **Atualizar dados**: Permite modificar um registro existente.
4.  **Deletar dados**: Remove um registro da lista.
5.  **Ver Estatísticas (R)**: Executa o script R para análise dos dados.
6.  **Ver Previsão do Tempo (R)**: Solicita uma cidade (ex: `Belo Horizonte,MG`) e exibe o clima atual via API.
0.  **Sair**: Encerra a aplicação.

---

## 📝 Requisitos do Projeto (FIAP)
- Suporte a pelo menos 2 tipos de culturas.
- Cálculos de área e manejo de insumos.
- Organização dos dados em vetores.
- CRUD completo (Entrada, Saída, Atualização, Deleção).
- Integração R/Python.
- Conexão com API meteorológica externa em R.

## API Previsão do Tempo

<a href="https://hgbrasil.com/docs/weather">Acessar HG Brasil Weather API</a>