# Validação executada em 25/11/2026
## Resultados
- Drive: 3 ZIPs acessados e extraídos, 25 MP4 identificados.
- FFprobe: 25/25 bem-sucedidos; 12 quadros extraídos por arquivo, 300/300, sheets abertas visualmente.
- Sheets adicionais a 2 fps geradas para 01, 02, 08, 12, 13, 20, 22; abertas em detalhe para 02, 12, 20.
- Upstream: 15 arquivos SKILL.md consultados via GitHub; extratos, não execução integral. Evidências em references/upstream-audit.md.
- Render local: HTML com seek(t) explícito, Playwright/Chromium e FFmpeg; 120 frames, MP4 H.264 540×960 a 24fps, duração medida 5.000s, sem áudio. A primeira tentativa de carregar file:// falhou com ERR_BLOCKED_BY_ADMINISTRATOR; usar HTML local já conhecido via page.set_content funcionou. Não requer serviço externo.
- Inspeção: versão do scripts/inspect-video.py reproduzida localmente e executada com sucesso no protótipo silencioso e vídeo 12 com áudio. Gerou probe, sheets, frames de 3 beats e logs de black/freeze; no vídeo 12, também ebur128 e true peak medido -3.9 dBFS no log. Sem análise auditiva.
- A prova foi examinada em 10 frames (2fps). Resultado técnico PASS. Resultado criativo NÃO APROVADO para publicação: composição simples, grade parece template, pouco movimento de transformação, nenhum ativo real, nenhum produto real, nenhuma assinatura sonora. É estudo tipográfico, não anúncio ou benchmark de qualidade. Essa distinção é obrigatória.
 
## Correção derivada
O próximo protótipo de launch deve ter uma unidade protagonista contínua (ref. 12), consequência visual real e crop demonstrável (13/08); não fazer apenas troca de palavra e cards. Primeiro frame já deve mostrar a mensagem, não fade vazio. O test harness só certifica o que mede, não estética.
 
## Não validado
- Não instalamos/rodamos HyperFrames, Remotion, Stewdio ou todas as outras skills; acesso a pacotes externos indisponível no ambiente.
- Não revisamos todos os quadros nativos de cada vídeo, não ouvimos trilha, não inferimos BPM exato.
- Os cenários de evals/scenarios.json são especificações, não execuções de um agente.
- Não houve anúncio aprovado, teste de audiência ou resultado de conversão.

## Segunda rodada: reparo real e scripts reutilizáveis
- V2: símbolo de marca atual obtido do asset assets/brand/simbolo-pequeno.svg do produto; cores do símbolo e da palavra-marca. O vídeo é conceito de marca, não UI. HTML determinístico, Chromium/Playwright + FFmpeg. MP4 540×960, 30fps, 6.000s, 180 frames, H.264, sem áudio. Primeira passagem: colisão de palavras orbitais com end copy e sobreposição da fala com símbolo. Reparo: recentralizar órbita, descer o texto final, escalonar opacidade do balão e símbolo. Rerender e inspeção visual de 12 frames a 2fps: a colisão evidente foi removida. O primeiro frame já tem título, balão e identidade cromática. Ainda não é anúncio aprovado: não contém captura/prova da experiência, voz ou CTA real. Não publicar como campanha pronta.
- Inspeção da skill também executada no V2 antes e depois do reparo, totalizando quatro execuções positivas com os dois testes anteriores.
- Novo scripts/analyze-library.py executado nos 25 MP4: 300 amostras, zero ausências; manifest com SHA-256, tempo, fps, dimensão, áudio e estado de revisão. A extração automática não aprova arte. Comando: python scripts/analyze-library.py /caminho/mp4 --out /caminho/qa --expect 25 --samples 12 --jobs 8. Requer Pillow, Python 3.11+ e FFmpeg/FFprobe.
- Novo scripts/validate-timeline.py: 8/8 asserções locais (template válido e rejeição de gap, overlap, duração fracionária, ID duplicado, dimensão ímpar, tempo fora de faixa, pista ausente). O arquivo tests/test_timeline.py registra os mesmos casos; CI foi configurada, não presumida executada no momento deste relatório.
- MP4 e sheets de terceiros não foram publicados. O protótipo contém ativo do produto e não foi publicado no repositório público; pode ser examinado pelo dono. Os critérios de conversão, som e estética ainda dependem de produção com captura real.
