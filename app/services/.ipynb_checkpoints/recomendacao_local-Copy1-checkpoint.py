#==> Imporatando bibliotecas
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import librosa

#==> Carrega e analiza musica local
@st.cache_data
def analyze_local_track(file_path):
    y, sr = librosa.load(file_path, sr=None)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    
    return {
        "tempo": tempo,
        "pitches": pitches,
        "mfcc": mfcc
    }

#==> Recomenda musicas semelhantes
@st.cache_data
def recommend_based_on_audio_features(tempo, genero_da_musica='pop'):  
    sp = st.session_state.sp
    recommendations = sp.recommendations(seed_genres=[genero_da_musica], limit=100, target_tempo=tempo)
    return recommendations['tracks']

#==> Pesquisa e faz recomendacao
def recomendacao_musica_local(): 
    #==> Titulo
    st.title("Seleciona aquela favorita 🤗")
    
    #==> Lista de generos
    genres = [
        'pop', 'rock', 'hip-hop', 'jazz', 'classical', 'blues', 'country', 'dance',
        'electronic', 'funk', 'soul', 'indie', 'k-pop', 'metal', 'reggae', 'r&b',
        'salsa', 'techno', 'trance', 'latino'
    ]
    
    #==> Escolher genero
    genero_escolhido = st.selectbox("Escolha um gênero musical", genres)

    #==> Upload do arquivo
    uploaded_file = st.file_uploader("Selecione uma música (MP3) em no botão (Browse files) ⏩⏩⏩", type=["mp3"])
     
    if uploaded_file:
        with open("temp_music.mp3", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write("Analisando a música...")
        audio_features = analyze_local_track("temp_music.mp3")
        
        st.write("Recomendando músicas semelhantes...")
        similar_tracks = recommend_based_on_audio_features(audio_features['tempo'], genero_escolhido)
        
        #==> Exibir as recomendacoes como embeds
        for track in similar_tracks:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            track_id = track['id']
            
            #==> Exibir o nome da musica e do artista
            st.write(f"**{track_name}** - {artist_name} - id {track_id}")
            
            #==> URL de embed do Spotify
            embed_url = f"https://open.spotify.com/embed/track/{track_id}"
            
            #==> Incorporar o player do Spotify com estilo customizado
            st.markdown(f"""
                <iframe style="border-radius:12px" src="{embed_url}" width="100%" height="152" frameBorder="0" 
                allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                loading="lazy"></iframe>
            """, unsafe_allow_html=True)