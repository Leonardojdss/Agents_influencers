# Plataforma de Agentes para Influenciadores

Este código em um front-end para agentes que auxiliam influenciadores e criadores de conteúdo a gerar conteúdo de qualidade, identificar tendências e se manter atualizados sobre os últimos acontecimentos na internet.

## Estrutura do Projeto
A plataforma permite que os usuários conversem com agentes especializados que ajudam em diversas tarefas relacionadas à criação de conteúdo.

## Tecnologias Utilizadas
- **Streamlit**: Framework utilizado para criar a interface web interativa.
- **Requests**: Biblioteca para realizar requisições HTTP.

## Como Iniciar o frontend localmente sem docker (Ambiente Linux ubuntu)

1. Criar um ambiente virtual com virtualenv:
   ```sh
   cd Agents_influencers/front_end_plataform_agents
   virtualenv env
2. Acessar o ambiente virtual criado e instalar as dependências do arquivo requirements.txt
    ```sh
    source env/bin/activate
    pip install -r requirements.txt
3. Navegar até o diretório
    ```sh
    cd app
4. Iniciar a aplicação utilizando Streamlit:
    ```sh
    streamlit run main.py

## Como Iniciar o Microserviço localmente com docker (Ambiente Linux ubuntu)

1. Acessar diretorio onde está o arquivo dockerfile
    ```sh
    cd Agents_influencers/front_end_plataform_agents
2. Criar build da imagem docker
    ```sh
    sudo docker build -t front_end_plataform_agents .
3. Iniciar container com a imagem criada
    ```sh
    sudo docker run -d -p 8501:8501 front_end_plataform_agents