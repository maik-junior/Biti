#==> Importacao de bibliotecas
import librosa
import streamlit as st
from services.apresentacao import apresenta_app
from services.requisicao import credentials
from services.recomendacao_api import recomendacao_spotify_api
from services.recomendacao_local import recomendacao_musica_local

#==> Configurarcoes de pagina
st.set_page_config(page_title='Biti', 
                   page_icon='🎧',
                  initial_sidebar_state='expanded')

#==> Verificando conteudo na sessao
if 'sp' in st.session_state:
    sp = st.session_state.sp

#==> Executa elementos do projeto
def Biti():  
    #==> Dipoe lodo e menssagem de bosas vindas
    apresenta_app()
    
    #==> Recuperando e disponinibilizando credenciais para o app
    credentials()
    
    #==> Criando as abas
    tab1, tab2 = st.tabs(['TEM O LINK DA MUSICA', 'SELECIONAR MUSICA NO COMPUTADOR'])
    
    #==> Aba 1
    with tab1:
        #==> Recomenda musicas baseado na analise de link fornecido
        recomendacao_spotify_api()
    
    #==> aba 2
    with tab2:     
        recomendacao_musica_local()

if __name__ == "__main__":
    Biti()