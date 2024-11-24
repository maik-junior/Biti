import spotipy
from spotipy.oauth2 import SpotifyOAuth
import librosa
import streamlit as st
import pprint

# Configurar a página
st.set_page_config(page_title="Minha Aplicação Streamlit", page_icon="./file/_d3fc50e1-94f8-4676-a898-dcfbef9ef0f8.jpeg")

# Exibir logo
logo = "./file/_6fcb1e6b-6203-49f8-96b0-97652c5fe0a6.jpeg"  # Substitua pelo caminho da sua imagem
st.image(logo, width=700)  # Você pode ajustar a largura conforme necessário

st.markdown(
    """
    <h2 style="font-size: 22px;">Encontrar músicas semelhantes às que você ama só aqui no Biti :)</h2>
    """, 
    unsafe_allow_html=True
)

st.markdown('---')

st.header('É novo(a) aqui?')
with st.expander('>>> Clique Aqui!'):
    st.write(""" Hei... Seja Bem-vindo(a)! Você está a um passo de descobrir uma infinidade de músicas novas. Esta aplicação te ajuda a encontrar hits semelhantes aos que você gosta no Spotify. O Spotify tem total zelo pelos direitos autorais dos conteúdos de sua plataforma. Para conseguir obter recomendações, você precisa fornecer dois dados de autenticação de usuário válidos no Spotify. Siga os passos do tutorial a seguir que, rapidinho, passamos daqui.""")


#==> Campo de entrada de texto
in_client_id = st.text_input("Digite o seu Cliente ID:")

#==> Campo de entrada numérica
in_client_secret = st.text_input("Digite o seu Cliente Secret:")

#==> Definindo porta
porta_selecionada = st.selectbox(
    "Escolha uma porta:",
    [8082, 8089, 8090]
)





# Sidebar para navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio("Escolha uma página:", ["Home", "Sobre", "Contato"])

# Lógica para diferentes páginas
if page == "Home":
    st.header("Página Inicial")
    st.write("Bem-vindo à página inicial da aplicação.")
    
elif page == "Sobre":
    st.header("Sobre")
    st.write("Esta aplicação foi criada para demonstrar a navegação.")
    
elif page == "Contato":
    st.header("Contato")
    st.write("Você pode entrar em contato pelo e-mail exemplo@dominio.com.")




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
    recommendations = sp.recommendations(seed_tracks=[track_id], limit=100)
    return recommendations['tracks']

#Exemplo de uso:
similar_tracks = recommend_similar_tracks(track_id)
for track in similar_tracks:
    print(track['name'], "-", track['artists'][0]['name'])



# Interface com Streamlit
st.title("Vai brota hit aí 💥")

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
        # st.balloons()


#----------------------





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

#-------------------------------------



#-------------------------------------

# Função para recomendar músicas semelhantes
def recommend_based_on_audio_features(tempo, genero_da_musica='pop'):    
    recommendations = sp.recommendations(seed_genres=[genero_da_musica], limit=100, target_tempo=tempo)
    return recommendations['tracks']

# Interface do Streamlit
st.title("Seleciona aquela favorita 🤗")

#-----------------------------------------------------------

# Lista de gêneros musicais disponíveis no Spotify
genres = [
    'pop', 'rock', 'hip-hop', 'jazz', 'classical', 'blues', 'country', 'dance',
    'electronic', 'funk', 'soul', 'indie', 'k-pop', 'metal', 'reggae', 'r&b',
    'salsa', 'techno', 'trance', 'latino'
]

# Selectbox para escolher o gênero
genero_escolhido = st.selectbox("Escolha um gênero musical", genres)


#--------------------------------------------

uploaded_file = st.file_uploader("Selecione uma música (MP3) em no botão (Broser files) ⏩⏩⏩", type=["mp3"])

if uploaded_file:
    with open("temp_music.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write("Analisando a música...")
    audio_features = analyze_local_track("temp_music.mp3")
    # st.write(f"Tempo: {audio_features['tempo']}")

    st.write("Recomendando músicas semelhantes...")
    similar_tracks = recommend_based_on_audio_features(audio_features['tempo'], genero_escolhido)
    
    for track in similar_tracks:
        st.write(f"{track['name']} - {track['artists'][0]['name']}")