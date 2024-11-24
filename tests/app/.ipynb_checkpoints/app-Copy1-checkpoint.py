import spotipy
from spotipy.oauth2 import SpotifyOAuth
import librosa
import streamlit as st
import pprint

# Configurar credenciais do Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="90f6e5fda01e4b67a02038e59d92399a",
    client_secret="8eccd12384384becbda6c0c6db8b92e1",
    redirect_uri="http://localhost:8889/callback",
    scope="user-library-read"
))

def get_audio_analysis(track_id):
    return sp.audio_analysis(track_id)  # Chama a análise de áudio

# Exemplo de chamada para uma música específica
track_id = '5pAflWrIzq6wChGbMH7Dal'  # Apenas o ID da faixa
audio_analysis = get_audio_analysis(track_id)

# Imprime a análise de áudio detalhada
# pprint.pp(audio_analysis)



def recommend_similar_tracks(track_id):
    recommendations = sp.recommendations(seed_tracks=[track_id], limit=10)
    return recommendations['tracks']

#Exemplo de uso:
similar_tracks = recommend_similar_tracks(track_id)
for track in similar_tracks:
    print(track['name'], "-", track['artists'][0]['name'])



# Interface com Streamlit
st.title("Spotify Music Recommender")

# Input para o usuário fornecer o link da música
track_url = st.text_input("Digite a URL da música no Spotify:")

if track_url:
    # Extrair o ID da música a partir do link
    track_id = track_url.split("/")[-1].split("?")[0]

    # # Mostrar os dados recuperados
    # st.write("Recuperando dados da música...")
    # audio_features = get_audio_analysis(track_id)
    # st.json(audio_features)

    # Mostrar recomendações
    st.write("Recomendando músicas semelhantes...")
    similar_tracks = recommend_similar_tracks(track_id)
    for track in similar_tracks:
        st.write(f"{track['name']} - {track['artists'][0]['name']}")


#------------------------------------------------------------------------------------------------------------

# Função para carregar e analisar música local
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

# Função para recomendar músicas semelhantes
def recommend_based_on_audio_features(tempo):
    recommendations = sp.recommendations(seed_genres=['pop'], limit=10, target_tempo=tempo)
    return recommendations['tracks']

# Interface do Streamlit
st.title("Music Recommender Based on Local File")

uploaded_file = st.file_uploader("Escolha uma música (MP3)", type=["mp3"])

if uploaded_file:
    with open("temp_music.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Analisando a música...")
    audio_features = analyze_local_track("temp_music.mp3")
    st.write(f"Tempo: {audio_features['tempo']}")

    st.write("Recomendando músicas semelhantes...")
    similar_tracks = recommend_based_on_audio_features(audio_features['tempo'])
    
    for track in similar_tracks:
        st.write(f"{track['name']} - {track['artists'][0]['name']}")