# Produção, revisão e entrega
## Estrutura de job
brief.md, evidence.md, refs/manifest.json, storyboard.md, timeline.json, assets/, src/, drafts/, qa/, final/. Timeline única com fps, dimensões, duração, seed, beats, áudio e legendas. Eventos com id, start, end, role, asset e texto quando pertinente. Validar tempos, continuidade e duração; não duplicar timing em arquivos diferentes. Sem relógio real ou aleatoriedade não semeada. Preferir render offline com fontes/ativos carregados.
 
## Gate temporal (obrigatório)
Leia [pacing-timing-editing.md](pacing-timing-editing.md) e use [pacing-review.md](../templates/pacing-review.md). Animatic antes do acabamento; análise de atividade por quadro no animatic/draft/final, inspeção linear e de janelas suspeitas, mapa de novidade, primeiro payoff, holds, timing em frames e frases sonoras. Nenhuma folha de frames, LUFS ou contador de pixels substitui a revisão editorial. Rubrica temporal separada 21/25, nenhum critério abaixo de 3, evidências e zero P0/P1; não avaliado impede alegar aprovação integral. Sem audição, som subjetivo pendente de revisão humana.

## Render e review-loop
Draft 540x960 para 9:16, fps do final. FFmpeg/ffprobe com scripts/inspect-video.py, sheets 2 fps, beats +0,3s e cortes ±2 frames (ajustar ao fps); inspeção micro a fps nativo. Captura do site real, texto HTML/SVG/React por cima, nunca gerar texto em imagem. Testar leitura 360px, safe zones atuais por canal, thumbnail, sem som, com som, sincronia, foco, velocidade, crop, clipping, flicker, freeze, preto, colisão, tipografia e CTA. Verificar determinismo e comandos check/lint específicos do motor. Não confundir saída automática com aprovação visual.
 
Crítica em duas passagens: leigo descreve o que entendeu sem roteiro; especialista compara com referência e objetivo. Registrar timestamp, severidade, causa, reparo, before/after e resultado. Se não há agentes, não inventar opiniões. Renderizar nova versão e revisar novamente. Priorizar causa, não maquiagem.
 
P0 bloqueia: mentira, preço/CTA falso, dados pessoais, asset sem direitos, idioma errado, tela fake apresentada como real, vídeo inválido, áudio clipado. P1 bloqueia: visual genérico, ausência de prova em anúncio, narrativa incoerente, texto ilegível, ritmo morto, redundância narrativa, gesto artificialmente lento, hold não justificado, transição ociosa, aceleração ilegível, falta de animatic revisado, lip sync falso, legenda ruim, efeitos sem intenção, sinalização IA faltante quando necessária. Se não resolver, marcar rascunho não aprovado.
 
Rubrica 0–5: verdade/estratégia, hook, narrativa/prova, direção/brand, motion/atuação, copy/localização, som/legendas, QA/entrega. Alvo 34/40, nenhum abaixo de 3 e zero P0/P1 aberto. Critério interno, não teste de usuário.
 
## Som e export
Selecione voz por teste curto de naturalidade, identidade, pronúncia, sotaque e custo. Não fixar fornecedor antigo. Sem clonagem não autorizada. Lip sync por visemas alinhados ao áudio quando disponível; se não convincente, evite close em boca. Medir loudness, BPM/beat quando possível; alvo inicial -14 a -16 LUFS integrado, true peak <= -1 dBTP, validar destino. Não alegar ouvir se não puder; pedir revisão humana antes de publicação. Música com licença comercial e SFX funcionais. Vídeo compreensível mudo.
 
Social base 1080x1920, 30fps, H.264/yuv420p, AAC 48kHz e Rec.709 conforme fonte. 60fps se movimento justificar. 16:9 e 1:1 com layout próprio, não crop cego. Legendas editáveis SRT/VTT e/ou queimadas; revisar texto e timing. Arquivo limpo sem watermark indevida. Entregar MP4, projeto, assets permitidos, timeline, roteiro, captions, thumbnail, relatório QA, licenças e copy; nunca declarar render inexistente.
 
## Medição e eficiência
Teste 3 hooks e manter oferta/corpo constantes. Registrar UTMs, placement, público, período, denominador, custo e hipótese. Separar métricas de alcance, intenção e prática/compra. Cachear referências/sheets, avaliar poucas cenas por vez, render barato antes de final, evitar múltiplos motores e agentes desnecessários. Sem métricas reais, entregar plano de medição. Sem publicação automática.

## Ferramentas testadas e gates automatizados
Antes do build: `python scripts/validate-timeline.py timeline.json`. Beats narrativos cobrem toda a duração sem lacunas ou sobreposição; faixas audiovisuais secundárias podem sobrepor. Para biblioteca local: `python scripts/analyze-library.py <pasta> --out <qa> --expect <n> --samples 12`. Manifest indica frames extraídos, não revisados. Para draft e final: `python scripts/inspect-video.py <mp4> --out <qa> --beat <s>`; abrir todas as sheets e inspecionar pontos suspeitos. A segunda prova de marca encontrou colisão entre texto e órbita e corrigiu por layout, timing e re-renderização. Transformação deve ser visualmente causal e leitura final precisa manter espaço próprio. Nunca aprovar uma peça comercial apenas por passar no script.
