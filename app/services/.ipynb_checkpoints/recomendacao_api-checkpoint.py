#==> importando bibliotecas
import streamlit as st
import time

#==> Lista para armazenar músicas favoritas
favorite_tracks = []
if 'faixas_favoritas' not in st.session_state:
    st.session_state.faixas_favoritas = favorite_tracks

#==> Recupera link da musica e fornece id para analise da api spotify
def recomendacao_spotify_api():
    #==> Verificando credenciais disponíveis
    if 'sp' in st.session_state:
        sp = st.session_state.sp
    
    #==> Analisa o áudio com API Spotify
    @st.cache_data
    def get_audio_analysis(track_id):
        return sp.audio_analysis(track_id)  
        
    #==> Recomenda baseado na música de entrada
    @st.cache_data
    def recommend_similar_tracks(track_id):
        time.sleep(1)
        recommendations = sp.recommendations(seed_tracks=[track_id], limit=10)
        return recommendations['tracks']
    
    #==> Interface com Streamlit
    st.title("Vai brotar hit aí 💥")
    
    #==> Solicita link da música para o usuário
    track_url = st.text_input("Digite a URL da música no Spotify:")
    
    if track_url:
        #==> Extrair o id da música a partir do link
        in_track_id = track_url.split("/")[-1].split("?")[0]
    
        if 'in_session_track_id' not in st.session_state:
            st.session_state.in_session_track_id = in_track_id
    
        #==> Recuperando dados da música
        audio_features = get_audio_analysis(in_track_id)
        
        if 'features' not in st.session_state:
            st.session_state.features = audio_features
    
        #==> Mostrar recomendações
        st.write("Recomendando músicas semelhantes...")
        similar_tracks = recommend_similar_tracks(st.session_state.in_session_track_id)

        #==> Exibir as recomendações
        for i, track in enumerate(similar_tracks):
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            track_id = track['id']
            
            #==> Exibir o nome da música e do artista
            # st.write(f"**{track_name}** - {artist_name}")
            
            #==> Incorporar a música usando o embed do Spotify
            embed_url = f"https://open.spotify.com/embed/track/{track_id}"
            st.markdown(f"""
                <iframe style="border-radius:12px" src="{embed_url}" width="100%" height="152" frameBorder="0" 
                allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                loading="lazy"></iframe>
            """, unsafe_allow_html=True)
            
            #==> Checkbox para marcar como favorito
            if st.checkbox(f"👍", key=f"fav_{i}"):
                #==> Verifica se a musica ja esta na lista pelo ID
                if not any(track['id'] == track_id for track in favorite_tracks):
                    favorite_tracks.append({
                        "name": track_name,
                        "artist": artist_name,
                        "id": track_id
                    })
        

    st.write(favorite_tracks) 

