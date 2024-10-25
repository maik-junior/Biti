#==> Importando bibliotecas
import streamlit as st

#==> Exibe titulo
st.header('Dicionário de dados')

#==> Exibe descricao dos metadados
st.markdown("""

### Meta

| Campo             | Tipo    | Descrição                                                                                       | Exemplo                         |
|-------------------|---------|-------------------------------------------------------------------------------------------------|---------------------------------|
| `analyzer_version` | string  | A versão do Analisador usada para analisar esta faixa.                                           | `"4.0.0"`                       |
| `platform`        | string  | A plataforma usada para ler os dados de áudio da faixa.                                         | `"Linux"`                       |
| `detailed_status` | string  | Um código de status detalhado para esta faixa. Se os dados de análise estiverem ausentes, esse código pode explicar o motivo. | `"OK"`                          |
| `status_code`     | integer | O código de retorno do processo de análise. 0 se bem-sucedido, 1 se ocorreram erros.            | `0`                             |
| `timestamp`       | integer | O timestamp Unix (em segundos) no qual esta faixa foi analisada.                                | `1495193577`                    |
| `analysis_time`   | number  | O tempo gasto para analisar esta faixa.                                                         | `6.93906`                       |
| `input_process`   | string  | O método usado para ler os dados de áudio da faixa.                                             | `"libvorbisfile L+R 44100->22050"`|

### Track

| Campo                | Tipo    | Descrição                                                                                                 | Exemplo          |
|----------------------|---------|-----------------------------------------------------------------------------------------------------------|------------------|
| `num_samples`        | integer | O número exato de amostras de áudio analisadas dessa faixa. Veja também `analysis_sample_rate`.            | `4585515`        |
| `duration`           | number  | Duração da faixa em segundos.                                                                              | `207.95985`      |
| `sample_md5`         | string  | Este campo sempre conterá uma string vazia.                                                                | `""`             |
| `offset_seconds`     | integer | Um deslocamento para o início da região da faixa que foi analisada. (Como toda a faixa é analisada, isso deve sempre ser 0.) | `0`              |
| `window_seconds`     | integer | O comprimento da região da faixa analisada, se um subconjunto da faixa foi analisado. (Como toda a faixa é analisada, isso deve sempre ser 0.) | `0`              |
| `analysis_sample_rate` | integer | A taxa de amostragem usada para decodificar e analisar esta faixa. Pode diferir da taxa de amostragem real dessa faixa disponível no Spotify. | `22050`          |
| `analysis_channels`  | integer | O número de canais usados para análise. Se 1, todos os canais são somados em mono antes da análise.        | `1`              |
| `end_of_fade_in`     | number  | O tempo, em segundos, em que o período de fade-in da faixa termina. Se a faixa não tiver fade-in, será 0.0. | `0`              |
| `start_of_fade_out`  | number  | O tempo, em segundos, em que o período de fade-out da faixa começa. Se a faixa não tiver fade-out, isso deve corresponder à duração da faixa. | `201.13705`      |
| `loudness`           | number  | A intensidade geral de uma faixa em decibéis (dB). Valores de intensidade são geralmente úteis para comparar a intensidade relativa de faixas. Valores normalmente variam entre -60 e 0 dB. | `-5.883`         |
| `tempo`              | number  | O ritmo geral estimado de uma faixa em batidas por minuto (BPM).                                          | `118.211`        |
| `tempo_confidence`   | number  | A confiança, de 0.0 a 1.0, da confiabilidade do ritmo.                                                     | `0.73`           |
| `time_signature`     | integer | Uma assinatura de tempo estimada. A assinatura de tempo (compasso) especifica quantas batidas há em cada compasso (ou medida). A assinatura de tempo varia de 3 a 7, indicando assinaturas de tempo de "3/4" a "7/4". | `4`              |
| `time_signature_confidence` | number | A confiança, de 0.0 a 1.0, da confiabilidade da assinatura de tempo.                                   | `0.994`          |
| `key`                | integer | A chave em que a faixa está. Inteiros mapeiam para tons usando a notação de Classe de Tons padrão. Por exemplo, 0 = C, 1 = C♯/D♭, 2 = D, e assim por diante. Se nenhuma chave foi detectada, o valor é -1. | `9`              |
| `key_confidence`     | number  | A confiança, de 0.0 a 1.0, da confiabilidade da chave.                                                     | `0.408`          |
| `mode`               | integer | O modo indica a modalidade (maior ou menor) de uma faixa, o tipo de escala de onde deriva seu conteúdo melódico. Maior é representado por 1 e menor por 0. | `0`              |
| `mode_confidence`    | number  | A confiança, de 0.0 a 1.0, da confiabilidade do modo.                                                     | `0.485`          |

A assinatura de tempo varia de 3 a 7, indicando assinaturas de tempo de "3/4" a "7/4". | `4` |
| `time_signature_confidence` | number | A confiança, de 0.0 a 1.0, da confiabilidade da assinatura de tempo. Seções com mudanças de assinatura de tempo podem corresponder a baixos valores neste campo. | `1` |

| Termo      | Descrição                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| Seções     | São as maiores divisões de uma música, como introdução, verso, refrão, ponte, etc. Essas seções organizam a música em blocos reconhecíveis e dão uma visão geral da estrutura. |
| Compassos  | Dentro de cada seção, a música é dividida em compassos, que agrupam um certo número de batidas e organizam o tempo da música. |
| Batidas    | Cada compasso contém um número específico de batidas (como 4 em um compasso 4/4). As batidas marcam o ritmo básico da música, determinando seu tempo. |
| Tatums     | Tatums são as subdivisões mais rápidas dentro das batidas. Eles representam as menores unidades rítmicas percebidas. Pense neles como subdivisões detalhadas de cada batida. |
| Pitches    | Os pitches se referem à altura das notas que estão sendo tocadas ou cantadas. Eles definem a melodia e a harmonia dentro de cada batida ou compasso. |
| Segmentos  | Segmentos são pequenos trechos de uma música que podem capturar mudanças perceptíveis em várias características, como altura (pitch), intensidade ou timbre. Eles são uma subdivisão mais detalhada e técnica da análise musical. |
| Timbre     | O timbre refere-se à qualidade do som em termos de sua textura ou "cor". É o que diferencia, por exemplo, o som de um violino do som de uma guitarra, mesmo se estiverem tocando a mesma nota. |


""")

#==> Exibe dados da musica
st.header('Veja a seguir os dados do link da música fornecido.')

if st.session_state.features:
    st.json(st.session_state.features)