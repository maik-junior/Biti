#==> Importando bibliotecas
import streamlit as st

#==> Definindo layout da pagina
st.set_page_config(layout="wide")

#==> Exibe video
st.video('../data/media/videos/client_id_secret.mp4')

#==> Exibe site para obter credenciais
st.header('Site: https://developer.spotify.com/')

#==> Portas de escucao da aplicacao
codigo_exemplo = """
portas: 
        http://localhost:8889/callback
        http://localhost:8890/callback
        http://localhost:8888/callback
"""

#==> Exibe portas
st.code(codigo_exemplo, language='markdown')
