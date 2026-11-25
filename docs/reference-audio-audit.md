# Auditoria sonora das 25 referências fornecidas — 25/11/2026
Amostragem computacional realizada agora: FFmpeg decodificou primeira faixa em mono float32 8 kHz. RMS em janelas de 100ms, percentis 10 e 90, medianas por quartil e fração RMS abaixo de -45 dBFS. Não é análise perceptual, LUFS, BPM, true peak ou audição. Downmix/resampling podem alterar picos; não inferir clipping com esses dados. 21 faixas não silenciosas; 13 e 21 não têm faixa; 14 e 22 têm faixa silenciosa. Não extraímos/reutilizamos samples de referência no arsenal.

| ID | P10 / P90 RMS dBFS | Mediana por quartil dBFS | % abaixo -45 |
|---|---|---|---:|
|01|-22.0 / -11.3|-16.9, -18.4, -14.3, -16.5|0.0|
|02|-28.8 / -12.1|-14.6, -14.6, -14.7, -23.0|1.4|
|03|-28.5 / -12.1|-16.0, -17.3, -17.6, -17.3|0.8|
|04|-23.8 / -10.8|-12.9, -16.1, -14.6, -19.9|2.0|
|05|-14.8 / -6.3|-10.8, -11.1, -7.5, -8.5|0.0|
|06|-24.8 / -11.1|-18.3, -15.6, -16.4, -16.3|2.7|
|07|-25.4 / -15.9|-19.8, -19.5, -20.4, -21.0|0.0|
|08|-26.4 / -10.4|-14.4, -16.9, -15.7, -17.3|1.9|
|09|-32.1 / -10.5|-24.0, -18.4, -19.3, -12.3|2.9|
|10|-39.0 / -8.2|-11.6, -12.8, -19.9, -24.6|4.4|
|11|-24.5 / -5.4|-12.9, -7.8, -7.9, -9.7|4.4|
|12|-31.0 / -10.9|-13.5, -18.5, -14.1, -16.2|4.8|
|13|sem faixa|—|—|
|14|silenciosa|—|100|
|15|-20.2 / -5.9|-16.1, -12.1, -12.5, -11.4|0.0|
|16|-20.4 / -8.3|-15.9, -14.5, -15.2, -16.8|0.5|
|17|-18.4 / -11.6|-13.9, -13.7, -13.8, -14.1|0.0|
|18|-54.7 / -18.2|-25.6, -24.5, -24.3, -24.1|14.9|
|19|-33.7 / -10.5|-15.4, -16.9, -16.8, -14.9|1.9|
|20|-10.6 / -2.2|-10.0, -2.5, -2.5, -2.6|0.7|
|21|sem faixa|—|—|
|22|silenciosa|—|100|
|23|-31.0 / -4.9|-8.7, -19.5, -10.1, -9.7|4.4|
|24|-35.8 / -19.8|-28.9, -27.4, -25.6, -29.7|2.8|
|25|-31.5 / -14.7|-28.1, -19.9, -18.3, -20.4|2.2|

Inferências prudentes: 09 tem crescimento de energia de início a fim; 02 e 10 reduzem energia no final; 12 e 23 variam significativamente entre quartis; 17 tem distribuição mais uniforme. Não sabemos timbre, instrumentos, beat, qualidade ou intenção sem ouvir. Usar como exemplo de que não existe uma curva universal, e que silêncio e contraste são opções narrativas. Comparar trechos com vídeo e música quando houver acesso auditivo. Os 32 sons adicionados vieram de fontes CC0 externas, não dos 25 MP4.
