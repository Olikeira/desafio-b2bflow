# Desafio de Estágio em Python - b2bflow

Este projeto é a solução para a primeira etapa do processo seletivo para a vaga de Estágio em Desenvolvimento Python na b2bflow.

O script em Python lê uma lista de contatos de um banco de dados Supabase e envia uma mensagem personalizada para cada um deles através da Z-API.

## Fluxo de Funcionamento

1.  **Conexão com o Supabase**: O script se conecta ao banco de dados usando as credenciais de ambiente.
2.  **Busca de Contatos**: Realiza uma consulta na tabela `contacts` para obter o nome (`name`) e o telefone (`phone`) dos contatos.
3.  **Envio de Mensagem**: Para cada contato, o script envia a mensagem `"Olá {{nome_contato}}, tudo bem com você?"` via Z-API, de forma personalizada.
4.  **Logs**: A execução do script gera logs no terminal, informando o status do processo e um resumo final.

## Requisitos

-   Python 3.8+
-   Conta no [Supabase](https://supabase.com/)
-   Conta na [Z-API](https://www.z-api.io/)

## Setup do Projeto

#### 1. Tabela no Supabase

Crie uma tabela em seu projeto Supabase com o nome `contacts` e as seguintes colunas:
-   `name` (tipo `text`)
-   `phone` (tipo `text`, armazene no formato E.164, ex: `5514999998888`)

#### 2. Variáveis de Ambiente

Na raiz do projeto, crie um arquivo `.env` e adicione as seguintes variáveis com suas respectivas chaves:

```
# Credenciais do Supabase (Project Settings > API)
SUPABASE_URL="SUA_URL_DO_PROJETO_SUPABASE"
SUPABASE_KEY="SUA_CHAVE_ANON_PUBLIC"

# Credenciais da Z-API
ZAPI_INSTANCE_ID="SEU_ID_DE_INSTANCIA"
ZAPI_TOKEN="SEU_TOKEN_DA_INSTANCIA"
```

## Como Rodar

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/Olikeira/desafio-b2bflow.git](https://github.com/Olikeira/desafio-b2bflow.git)
    cd desafio-b2bflow
    ```

2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  Execute o script principal:
    ```bash
    python src/main.py
    ```