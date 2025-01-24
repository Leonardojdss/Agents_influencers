import streamlit as st
from streamlit_option_menu import option_menu
import requests
import logging

logging.basicConfig(level=logging.DEBUG)

def agents(input):
    body = {
  "text": f"{input}"
    }
    request_agent = requests.post("https://ms-flow-agents-influencers.azurewebsites.net/ms_flow_agents_influencers/influencers", json=body)
    response_agent = request_agent.json()
    return response_agent

if __name__ == "__main__":

    st.markdown("<h1 style='text-align: center;'>Plataforma de Agentes para influenciadores e criadores de conteúdo</h1>", unsafe_allow_html=True)
    
    menu = option_menu(None, 
    ["chat com agentes"], 
    icons=["chat", "data"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal")

    logging.debug(f"Menu selected: {menu}")

    if menu == "chat com agentes":

        st.markdown(
            "<h3 style='font-size:16px;'>Nesta seção você pode conversar com os agentes, que irão te ajudar a criar conteúdo de qualidade, identificar tendências, estar atualizado sobre os últimos acontecimentos na internet. Converse com os agentes e veja o poder deles em ação.</h3>", 
            unsafe_allow_html=True
        )
        input = st.text_input("Digite o que deseja pedir para os agentes")
        with st.spinner("Os agentes estão trabalhando, aguarde!"):
            if st.button("Enviar"):
                response = agents(input)
                response_content = response['result']
                st.markdown(response_content)