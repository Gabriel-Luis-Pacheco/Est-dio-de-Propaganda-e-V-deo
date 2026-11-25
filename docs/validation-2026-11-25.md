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
