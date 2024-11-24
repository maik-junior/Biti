#==> Importacao de bibliotecas
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#==> Recupera credenciais e diponibliza na sessao
def credentials():
    #==> Recupera cliente_id
    in_client_id = st.text_input("Digite o seu Cliente ID:")
    
    #==> Recupera cliente_secret
    in_client_secret = st.text_input("Digite o seu Cliente Secret:")
    
    #==> Definindo porta
    porta_selecionada = st.selectbox(
        "Escolha uma porta:",
        [8082, 8089, 8090]
    )   
    
    #==> Configurar credenciais do Spotify
    if in_client_id and in_client_secret and porta_selecionada:
        #==> Construir o redirect_uri dinamicamente com base na porta selecionada
        redirect_uri = f"http://localhost:{porta_selecionada}/callback"
        
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=in_client_id,
        client_secret=in_client_secret,
        redirect_uri=redirect_uri,
        scope="user-library-read"
        ))
        
        #==> Dispondo credential na sessao
        if 'sp' not in st.session_state:
            st.session_state.sp = sp
        

    