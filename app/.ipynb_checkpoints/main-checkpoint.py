#==> Importando bibliotecas
import pandas as pd
import streamlit as st
import requests as rq
from services.dicionario_de_dados import dicionario
import json

#==> Escrevendo nome d a aplicacao
st.title('Biti Match')
st.markdown('''
Este projeto tem como objetivo desenvolver uma solução que analisa os dados de uma ou mais músicas no desktop, detecta seu ritmo e, a partir disso, sugere músicas com características semelhantes no Spotify.
''')

#==> Carregar o arquivo de audio
audio_file = st.file_uploader("Carregue seu áudio mp3 aqui para análise.", type=["mp3"])

#==> Carregar arquivo
if audio_file is not None:
    #==> Le o arquivo em bytes
    audio_bytes = audio_file.read()
    
    #==> Exibe o player de audio
    st.audio(audio_bytes, format="audio/wav")

#==> Lendo amostra de dados de um audio
df = pd.read_csv('./file/amostra_de_dados.csv')

#==> Escrevendo dicionari da amostra
st.title('Dicionario de dados')
st.markdown(dicionario())
st.title('Amostra de analise de faixa de audio')
st.dataframe(data=df)