#==> Importacao de bibliotecas
import streamlit as st

#==> Dipoe lodo e menssagem de bosas vindas
def apresenta_app():
    #==> Exibe logo
    st.image('https://th.bing.com/th/id/OIG1.oqgns..sYYCUjHtEB6mz?pid=ImgGn')
    # logo = "./file/_6fcb1e6b-6203-49f8-96b0-97652c5fe0a6.jpeg" 
    # #==> defininco tamannho
    # st.image(logo, width=700)

    #==> Exibe menssagem 
    st.markdown(
        """
        <h2 style="font-size: 22px;">Encontrar músicas semelhantes às que você ama só aqui no Biti :)</h2>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown('---')
    
    #==> Mensagem de introducao ao app
    st.header('É novo(a) aqui?')
    with st.expander('>>> Clique Aqui!'):
        st.markdown(""" Hei... Seja Bem-vindo(a)! Você está a um passo de descobrir uma infinidade de músicas novas. Esta aplicação te ajuda a encontrar hits semelhantes aos que você gosta no Spotify. O Spotify tem total zelo pelos direitos autorais dos conteúdos de sua plataforma. Para conseguir obter recomendações, você precisa fornecer dois dados de autenticação de usuário válidos no Spotify. Siga os passos do tutorial a seguir que, rapidinho, passamos daqui. [`>>> Assistir tutorial`](0._Tutorial_-_Comece_Aqui)""")
            
        
        
    