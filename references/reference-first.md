# Direção de arte e engenharia reversa de movimento
Base: guia fornecido em 25/11/2026, posts de Meng To e Magdiel Silva, método Stewdio. Não basta instalar skill. Briefing, referência e crítica de frames decidem acabamento.

## Pesquisa visual obrigatória para produção relevante
Pesquisar 10 peças reais (concorrentes e estúdios), inspecionar 5 imagens para look, cor, material, composição e detalhe, 3 vídeos para mecanismo, virada e saída/câmera. Escolher uma estética coerente, não colagem de estilos. Consultar a biblioteca. Ex.: Bitmap storyboard de Grok Bot/Allo: observar enquadramento, mascote, tipografia, transformação do objeto, clareza e contraste. Imagem estática não prova timing. Estudar filmes reais de lançamento de produtos, não só seus thumbnails.
 
Para cada referência: autor/URL, timestamp, frame, função, movimento, estado antes/depois, câmera, escala, easing, duração, áudio e beat de destino. Registrar o que rejeitar e direitos. Transferir mecanismo, não copiar assets, logotipo, identidade, personagem, texto ou trilha. Referência sem função é removida.
 
## FFmpeg: aprender com vídeo real
1. Obter MP4 autorizado localmente. Executar ffprobe para duração, fps, codecs e dimensões.
2. python scripts/inspect-video.py refs/video.mp4 --out refs/sheets/video --fps 2 --beat 1.5 --beat 4.2 (tempos reais do vídeo, não estes defaults).
3. Abrir contact sheets na ordem; marcar hook, setup, transições, câmera, gesto, ritmo, turn, CTA.
4. Inspecionar cortes e microgestos no fps nativo com intervalo de poucos frames; não inferir movimento só com uma imagem. Medir onset, duração, overlap e trajetória aproximada por posições; anotar grau de certeza. Para som, medir loudness, BPM/drops quando possível e ouvir se houver capacidade. Não alegar ter ouvido se não ouviu.
5. Produzir motion transfer map: referência, trecho, mecanismo, por que funciona, adaptação própria, cena de destino, teste de fidelidade. Fazer pequena prova técnica antes do vídeo longo.
 
## Briefing em quatro blocos
INPUTS: público, objetivo, evidência de produto, assets reais, formato, fps, prazo, orçamento, refs com trechos.
DIRECTION: uma estética, tokens e fonte do produto, câmera, material, luz, coreografia, ritmo e áudio. Nomear o que não é. Evitar adjetivos vazios.
STRUCTURE: beats numerados, tempo de início/fim, ação, estado antes/depois, texto exato, som, prova e intenção; primeiro frame, turn, end card.
BANNED: fake UI, texto gerado na imagem, efeitos decorativos, assets sem direitos, longos holds sem intenção, excesso de zoom/blur, voz robótica, produto invisível em anúncio.
 
Método Stewdio blank-page: 5 referências visuais de uma estética, 3 de movimento, um turn, beats com função e assets reais; editar feedback com alvo, mudança, magnitude e manter-cláusula. Método screens-to-video: feature única, recortes reais, planos do telefone/tela/detalhe, ação crescente, turn, end card. Adaptar localmente se MCP não estiver disponível. Um vídeo de 5s comporta uma ideia. Não transformar números em dogmas.
 
## Exemplo de hipótese comercial 20s
0–2s: pergunta real do café e hook; 2–5s: hesitação; 5–10s: dica verificada e tentativa; 10–14s: resposta/resultado real; 14–17s: outra situação ou língua verificada; 17–20s: CTA. Ajustar duração e copy por audiência. Nenhum frame de interface inventada. Mostre valor antes de logo. Não gastar créditos sem aprovação.

## Transferência de ritmo
Além de LOOK/MOVES, mapear first value, eventos, duração de shots/gestos e pausas, energia física/emocional/narrativa, frase musical e consequência. Comparar 3 trechos equivalentes; não confundir amostras de screenshots com ritmo medido. Ver [pacing-timing-editing.md](pacing-timing-editing.md). Use animatic para transferir gramática de edição, não apenas estética.

## LOOK, MOVES e SPACE
Para launch premium estudar também [direção espacial](spatial-motion-direction.md): styleframes, lente e câmera, materiais, luz, oclusão, volume, parallax, transformação, continuidade e coreografia. Comparar um mecanismo renderizado próprio com trechos reais; não atribuir 3D ou timing a referência por thumbnail. Verificar stack ativa antes de decidir motor.
