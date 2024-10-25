#==> Exibe a descricao dos dados
def dicionario():
    tabela = """
| Campo                     | Tipo    | Descrição                                                                                                               | Exemplo     |
|---------------------------|---------|-------------------------------------------------------------------------------------------------------------------------|-------------|
| `num_samples`             | integer | O número exato de amostras de áudio analisadas dessa faixa. Veja também `analysis_sample_rate`.                         | `4585515`   |
| `duration`                | number  | Duração da faixa em segundos.                                                                                           | `207.95985` |
| `sample_md5`              | string  | Este campo sempre conterá uma string vazia.                                                                             | `""`        |
| `offset_seconds`          | integer | Um deslocamento para o início da região da faixa que foi analisada. (Como toda a faixa é analisada, isso deve ser 0.)   | `0`         |
| `window_seconds`          | integer | O comprimento da região da faixa analisada, se um subconjunto da faixa foi analisado. (Como toda a faixa é analisada, isso deve ser 0.) | `0`         |
| `analysis_sample_rate`    | integer | A taxa de amostragem usada para decodificar e analisar esta faixa. Pode diferir da taxa de amostragem real dessa faixa disponível no Spotify. | `22050`     |
| `analysis_channels`       | integer | O número de canais usados para análise. Se 1, todos os canais são somados em mono antes da análise.                     | `1`         |
| `end_of_fade_in`          | number  | O tempo, em segundos, em que o período de fade-in da faixa termina. Se a faixa não tiver fade-in, será 0.0.             | `0.28599`   |
| `start_of_fade_out`       | number  | O tempo, em segundos, em que o período de fade-out da faixa começa. Se a faixa não tiver fade-out, isso deve corresponder à duração da faixa. | `201.13705` |
| `loudness`                | number  | A intensidade geral de uma faixa em decibéis (dB). Valores de intensidade são geralmente úteis para comparar a intensidade relativa de faixas. Valores normalmente variam entre -60 e 0 dB. | `-5.883`    |
| `tempo`                   | number  | O ritmo geral estimado de uma faixa em batidas por minuto (BPM).                                                        | `118.211`   |
| `tempo_confidence`        | number  | A confiança, de 0.0 a 1.0, da confiabilidade do ritmo.                                                                  | `0.73`      |
| `time_signature`          | integer | Uma assinatura de tempo estimada. A assinatura de tempo (compasso) especifica quantas batidas há em cada compasso (ou medida). A assinatura de tempo varia de 3 a 7, indicando assinaturas de tempo de "3/4" a "7/4". | `4`         |
| `time_signature_confidence` | number | A confiança, de 0.0 a 1.0, da confiabilidade da assinatura de tempo.                                                   | `0.994`     |
| `key`                     | integer | A chave em que a faixa está. Inteiros mapeiam para tons usando a notação de Classe de Tons padrão. Por exemplo, 0 = C, 1 = C♯/D♭, 2 = D, e assim por diante. Se nenhuma chave foi detectada, o valor é -1. | `9`         |
| `key_confidence`          | number  | A confiança, de 0.0 a 1.0, da confiabilidade da chave.                                                                  | `0.408`     |
| `mode`                    | integer | O modo indica a modalidade (maior ou menor) de uma faixa, o tipo de escala de onde deriva seu conteúdo melódico. Maior é representado por 1 e menor por 0. | `0`         |
| `mode_confidence`         | number  | A confiança, de 0.0 a 1.0, da confiabilidade do modo.                                                                   | `0.485`     |
    """
    return tabela
