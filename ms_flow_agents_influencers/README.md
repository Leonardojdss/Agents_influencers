# flow_agents Crew

Este projeto é um microserviço que concentra agentes especialistas em diversas tarefas, todos gerenciados por um agente gerente, utilizo o framework CrewAI para orquestrar a colaboração entre os agentes e garantir que cada tarefa seja executada de maneira eficiente e coordenada.

## Estrutura do Projeto

O microserviço é composto por vários agentes, cada um especializado em uma área específica:

- **trend_youtube**: Especialista em vídeos RAG, responsável por identificar e analisar tendências no YouTube.
- **trend_researcher**: Pesquisador de conteúdo na internet, focado em encontrar tópicos populares e relevantes.
- **content_analyst**: Analista de conteúdo, que desconstrói postagens bem-sucedidas para identificar elementos-chave.
- **content_creator**: Criador de conteúdo, que desenvolve narrativas atraentes baseadas em insights de pesquisa.
- **seo_specialist**: Especialista em SEO, que otimiza o conteúdo para aumentar a visibilidade nos mecanismos de busca.

O agente gerente, **agent_manager**, é responsável por gerenciar o fluxo de trabalho desses agentes, garantindo que todas as tarefas sejam concluídas de maneira eficiente.

## Tecnologias Utilizadas

- **CrewAI**: Framework utilizado para criar e gerenciar os agentes e suas interações.
- **FastAPI**: Framework web para construir a API do microserviço.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.

## Como Iniciar o Microserviço localmente sem docker (Ambiente Linux ubuntu)

1. Criar um ambiente virtual com virtualenv:
   ```sh
   virtualenv env
2. Acessar o ambiente virtual criado e instalar as dependências do arquivo requirements.txt
    ```sh
    source env/bin/activate
    pip install -r requirements.txt
3. Navegar até o diretório
    ```sh
    cd Agents_influencers/ms_flow_agents_influencers/src
4. Iniciar o servidor utilizando Uvicorn:
    ```sh
    uvicorn flow_agents.main:app --host 0.0.0.0 --port 8500 --reload

## Como Iniciar o Microserviço localmente com docker (Ambiente Linux ubuntu)

1. Acessar diretorio onde está o arquivo dockerfile
    ```sh
    cd Agents_influencers/ms_flow_agents_influencers
2. Criar build da imagem docker
    ```sh
    sudo docker build -t ms_flow_agents_influencers .
3. Iniciar container com a imagem criada
    ```sh
    sudo docker run -d -p 8500:8500  ms_flow_agents_influencers


Com esses passos, o microserviço estará em execução e pronto para receber requisições. O endpoint /influencers pode ser utilizado para iniciar os agentes e executar as tarefas definidas.

Este projeto é uma solução robusta para gerenciar e automatizar tarefas complexas, aproveitando o poder dos agentes especializados e do framework CrewAI.

## Exemplo de requisição:
curl -X 'POST' \
  'http://localhost:8500/ms_flow_agents_influencers/influencers' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "identifique o assunto mais falado anteontem dia 20 de janeiro de 2025 e monte um pequeno texto informativo para o instagram"
}'