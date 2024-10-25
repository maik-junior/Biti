#==> Importando bibliotecas
import streamlit as st

#==> Definindo layout
st.set_page_config(layout='wide')

#==> Titulo
st.title("Aprenda teoria musical.")

#==> Exibe video
st.video("https://www.youtube.com/embed/CYFcEyne4xc?si=UbBsgKhsuTEagpfB")

#==> Exibe marcacoes do video
with st.expander('Conteúdo do curso:'):
    st.markdown("""

    | Tempo     | Seção                                 |
|-----------|---------------------------------------|
| 0:00      | 0.0 - Apresentação                    |
| 1:01      | 1.0 - Propriedades do som             |
| 2:17      | 1.1 - Notas musicais                  |
| 2:38      | 1.2 - Pauta                           |
| 3:01      | 1.3 - Claves                          |
| 4:26      | 1.4 - Leitura clave de sol            |
| 5:35      | 1.5 - Leitura clave de fá             |
| 6:35      | 1.6 - Dó central                      |
| 7:20      | 1.7 - Linhas suplementares            |
| 9:05      | 1.8 - Oitavas                         |
| 9:40      | 2.0 - A importância do tempo          |
| 10:05     | 2.1 - Figuras musicais                |
| 10:15     | 2.2 - Nomenclatura das figuras        |
| 13:05     | 2.3 - Ponto de aumento                |
| 13:45     | 2.4 - Ponto de diminuição             |
| 14:10     | 2.5 - Ligadura de tempo               |
| 15:10     | 3.0 - Compasso                        |
| 17:00     | 3.1 - Andamento e pulso               |
| 18:18     | 3.2 - Síncope                         |
| 19:00     | 3.3 - Contratempo                     |
| 19:30     | 3.4 - Numerador e denominador         |
| 19:57     | 3.5 - Tabela da figura de 1 tempo     |
| 20:24     | 3.6 - Novos valores das figuras       |
| 22:05     | 3.7 - Quiáltera                       |
| 23:08     | 4.0 - Sinais na partitura             |
| 26:20     | 5.0 - Acidentes                       |
| 27:00     | 5.1 - Sustenido e bemol               |
| 29:30     | 5.2 - Tom e Semitom                   |
| 30:15     | 5.3 - Distância entre duas notas      |
| 30:55     | 5.4 - Mais acidentes                  |
| 31:40     | 5.5 - Acidentes na prática            |
| 33:35     | 6.0 - Intervalos                      |
| 33:45     | 6.1 - Contagem de intervalos          |
| 34:00     | 6.2 - Classificação de intervalos     |
| 34:18     | 6.3 - Tabela dos intervalos           |
| 34:40     | 6.4 - Categorias dos intervalos       |
| 35:02     | 6.5 - Classificação na prática        |
| 36:05     | 6.6 - Intervalo descendente           |
| 41:06     | 7.0 - Escalas                         |
| 41:10     | 7.1 - Escala Maior                    |
| 41:40     | 7.2 - Formando escalas na prática     |
| 43:50     | 7.3 - Escala menor                    |
| 44:38     | 7.4 - Tipos de escalas menores        |
| 48:15     | 7.5 - Escala menor natural            |
| 48:20     | 7.6 - Escala menor harmônica          |
| 48:25     | 7.7 - Escala menor melódica           |
| 48:35     | 7.8 - Resumo das escalas              |
| 49:35     | 7.9 - Ciclo das quartas e quintas     |
| 50:00     | 7.10 - Ciclo na aplicação prática     |
| 52:40     | 8.0 - Acordes                         |
| 52:40     | 8.1 - Cifras                          |
| 52:40     | 8.2 - Acorde Maior                    |
| 53:52     | 8.3 - Acorde menor                    |
| 56:49     | 8.4 - Comparativo entre Maior e menor |
| 57:17     | 8.5 - Acorde com quinta aumentada     |
| 57:31     | 8.6 - Acorde com quinta bemol         |
| 57:50     | 8.7 - Acorde suspenso                 |
| 58:20     | 8.8 - Resumo dos acordes              |
| 58:40     | 9.0 - Campo harmônico                 |
| 59:10     | 9.1 - Formação do campo harmônico Maior|
| 59:20     | 9.2 - Fórmula do campo harmônico Maior|
| 1:00:00   | 9.3 - Campo harmônico na prática      |
| 1:02:10   | 9.4 - Fórmula de outros campos harmônicos |
| 1:02:45   | 10.0 - Conclusão                      |

""")




