# Plataforma de Apoio para Criadores de Conteúdo

Este projeto é uma solução completa que integra um microserviço de agentes especializados e um front-end interativo para auxiliar influenciadores e criadores de conteúdo a gerar conteúdo de qualidade, identificar tendências e se manter atualizados sobre os últimos acontecimentos na internet. O principal objetivo deste projeto é demonstrar o poder dos agentes e, principalmente, o uso do agente gerente (manager) para controlar o fluxo dos agentes, selecionar os agentes para cada tarefa e garantir a execução eficiente das atividades.

## Estrutura do Projeto

O projeto é composto por dois principais componentes:

1. **Microserviço de Agentes**: Utiliza o framework CrewAI para orquestrar a colaboração entre agentes especializados em diversas tarefas, com foco no agente gerente que controla o fluxo de trabalho.
2. **Front-End**: Utiliza Streamlit para criar uma interface web interativa que permite aos usuários interagir com os agentes.

## Tecnologias Utilizadas

- **CrewAI**: Framework utilizado para criar e gerenciar os agentes e suas interações.
- **FastAPI**: Framework web para construir a API do microserviço.
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI.
- **Streamlit**: Framework utilizado para criar a interface web interativa.
- **Requests**: Biblioteca para realizar requisições HTTP.

## Como Iniciar o Projeto

### 1. Iniciar o Microserviço de Agentes
 - Atualizar arquivo .env com a chave do LLM da Openai (pago por requisição) e a chave da api serper (gratuita)
 - Seguir os passos da documentação para subir locamente, link - https://github.com/Leonardojdss/Agents_influencers/blob/main/ms_flow_agents_influencers/README.md

### 2. Iniciar o Front-End
- Seguir os passos da documentação para subir locamente, link - https://github.com/Leonardojdss/Agents_influencers/blob/main/front_end_plataform_agents/README.MD

## Conclusão
Com esses passos, o microserviço e o front-end estarão em execução e prontos para serem utilizados. Este projeto é uma solução para demonstrar o poder dos agentes especializados, com ênfase no gerenciamento do fluxo de trabalho pelo agente gerente e no uso do framework CrewAI, além de proporcionar uma interface interativa para os usuários.
