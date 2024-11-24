#==> Importando bibliotecas
import streamlit as st
import requests
import json

#==> Funcao envia muicas para api e recebe ordendenadas
def ordena_similares():
    faixas_favoritas = []
    #==> Verificando faixas na sessao
    if 'faixas_favoritas' in st.session_state:
        faixas_favoritas = st.session_state.faixas_favoritas
                   
    #==> Exibindo faixas
    st.write("Lista de músicas:")
    if faixas_favoritas:
        for item in faixas_favoritas:
            st.write(f"Música: {item['name']}, Artista: {item['artist']}, ID: {item['id']}")
    
        url = "http://127.0.0.1:4000/salvar/"
    
        #==> Envia musicas para api
        if faixas_favoritas:
            try:
                #==> POST
                response = requests.post(
                    url, 
                    headers={"Content-Type": "application/json"}, 
                    data=json.dumps(faixas_favoritas)
                )
        
                #==> Verificando o status da requisicao
                if response.status_code == 200:
                    st.success("Músicas enviadas com sucesso!")
                else:
                    st.error(f"Erro ao enviar músicas: {response.json()}")
        
            except Exception as e:
                st.error(f"Erro ao se conectar à API: {str(e)}")

    #==> Exibe lista de musicas salvas na api
    if st.button("Lista API", key=5):
        response = requests.get("http://127.0.0.1:4000/listar/")
        data = response.json()
        st.json(data)
    

    