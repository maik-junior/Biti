#==> importando bibliotecas
import streamlit as st
import time

#==> Verificando credenciais didponiveis
if 'sp' in st.session_state:
    sp = st.session_state.sp

#==> Recupera link da musica e fornece id para analise da api spotify
def recomendacao_spotify_api():
    #==> Analisa o audio com api spotify
    @st.cache_data
    def get_audio_analysis(track_id):
        return sp.audio_analysis(track_id)  # Chama a análise de áudio
        
    #==> Recomenda baseado na musica de entrada
    @st.cache_data
    def recommend_similar_tracks(track_id):
        time.sleep(1)
        recommendations = sp.recommendations(seed_tracks=[track_id], limit=100)
        return recommendations['tracks']
    
    #==> Interface com Streamlit
    st.title("Vai brotar hit aí 💥")
    
    #==> Solicita link da musica para o usuario
    track_url = st.text_input("Digite a URL da música no Spotify:")
    
    if track_url:
        #==> Extrair o id da musica a partir do link
        in_track_id = track_url.split("/")[-1].split("?")[0]
    
        if 'in_session_track_id' not in st.session_state:
            st.session_state.in_session_track_id = in_track_id
    
        #==> Recurando dados da musica
        audio_features = get_audio_analysis(in_track_id)
        
        if 'features' not in st.session_state:
            st.session_state.features = audio_features
    
        #==> Mostrar recomendacoes
        st.write("Recomendando músicas semelhantes...")
        similar_tracks = recommend_similar_tracks(st.session_state.in_session_track_id)
        # similar_tracks = recommend_similar_tracks(in_track_id)
        for track in similar_tracks:
            
            # st.write(f"{track['name']} - {track['artists'][0]['name']}")
            
            #==> Incorporar a musica usando o embed do Spotify
            embed_url = f"https://open.spotify.com/embed/track/{track['id']}"
            st.markdown(f'<iframe style="border-radius:12px" src="{embed_url}" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)
    
            #==> Exibir o id da musica
            # st.write(f"ID da faixa: {track['id']}")