#==> Importacao de bibliotecas
import librosa
import streamlit as st
import requests
import json

#==> Importacao de funcoes
from services.apresentacao import apresenta_app
from services.requisicao import credentials
from services.recomendacao_api import recomendacao_spotify_api
from services.recomendacao_local import recomendacao_musica_local
from services.ordenar_favoritas import ordena_similares

#==> Configurarcoes de pagina
st.set_page_config(page_title='Biti', 
                   page_icon='🎧',
                   initial_sidebar_state='expanded')


#==> Executa elementos do projeto
def Biti(): 
    #==> Dipoe lodo e menssagem de bosas vindas
    apresenta_app()
    
    #==> Recuperando e disponinibilizando credenciais para o app
    credentials()

    #==> Criando as abas
    tab1, tab2, tab3 = st.tabs(['TEM O LINK DA MUSICA', 'SELECIONAR MUSICA NO COMPUTADOR', 'FAVORITAS'])
    
    #==> Aba 1
    with tab1:
        #==> Recomenda musicas baseado na analise de link fornecido
        recomendacao_spotify_api()
    
    #==> aba 2
    with tab2: 
        #==> Recomenda musicas baseado na analise de audio fornecido
        recomendacao_musica_local()

    #==> aba 3
    with tab3:
        #==> Envia musicas para api
        ordena_similares()
       
if __name__ == "__main__":
    Biti()