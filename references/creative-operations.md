# Operações criativas — da referência ao vídeo publicável
Este módulo traduz o GUIA.md recebido em 25/11/2026 e os prints sobre motion em ações verificáveis. Os 25 MP4 foram inspecionados por amostragem em reference-lab.md; 15 skills consultadas em upstream-audit.md. O fallback local e o script de inspeção foram executados; não houve instalação dos motores externos. Não substituir evidência por texto persuasivo.

## 1. Preflight
Crie um job isolado. Identifique: missão, público, país, língua, produto atual, destino, duração, formato, custo permitido, ativos e direitos, FFmpeg/FFprobe/Node/browser e skills disponíveis. Confira o site e jornada, não extrapole o código. B2C: a landing anuncia cinco idiomas de estudo e apoio em português. B2B: oferta de inglês para turmas de adultos, piloto e relatórios agregados; não fabricar painel. Não publicar informação privada. Se um insumo faltar, escolha fallback e marque a limitação. Não interrompa produção reversível só para pedir aprovação estética; se houver gasto ou transferência de dados, exija autorização.

## 2. Roteador de skills: ação, não catálogo
| Missão | Skill primária | Complementos condicionais | Evidência mínima |
|---|---|---|---|
| Launch film / anúncio de produto | HyperFrames (launch, capture, reverse-any-video, style-sampling) | Stewdio blank-page/screens-to-video, video-shotcraft, GSAP, LottieFiles, claude-motion | captura real, brief medido, timeline, MP4 |
| UI demonstrativa | Emil/AiforUI, Motion ou GSAP | DesignBookmark Motion, Stewdio, HyperFrames | movimento medido, antes/depois e vídeo |
| Motion abstrato | HyperFrames + LottieFiles ou claude-motion | motion-prompt, mg-styles-15, Charlie947 | prova de gesto, sheet, turn |
| Série de versões | Remotion skills oficiais | HyperFrames variáveis, captions | mesmo contrato, variantes renderizadas e QA de cada uma |
| Explicador | Motion Canvas ou HyperFrames | Remotion, SVG, LottieFiles | clareza visual, pedagogia verificada |
| 3D | Blender skills | Three.js, Stewdio câmera | movimento e enquadramento sem deformação |
| Footage/UGC | video-use e FFmpeg | HyperFrames para composição, captions | cortes por palavra, licenças, transcrição e loudness |
| Arte e conversão | Best-Designer-in-the-World.- / Hallmark | marketingskills/video | crítica anti-slop e evidência comercial |
Para cada skill selecionada: localizar arquivo instalado ou fonte oficial, ler SKILL.md e somente referências pertinentes, verificar licença/custo, registrar versão e 2–5 regras concretas a aplicar. Instalar no escopo do job apenas se autorizado; usar fallback documentado se indisponível. Não fingir que leu ou rodou skill por reconhecer o nome. Não enviar capturas privadas a MCPs externos. Referências a comandos no guia são pontos de partida, confirmar sintaxe na versão instalada.

## 3. Laboratório de referência
Para campanha importante, 10 candidatas reais de estúdios ou concorrentes; selecionar cinco stills coerentes (look, composição, material, tipografia, detalhe) e três moves (mecanismo, virada, saída/câmera). Fonte, autor, trecho, direitos e motivo obrigatório. Evitar mistura estética. Referências selecionadas por mérito visual e função, não likes. Um arquivo anexado preenche sua função, não dispensa medição.
Para nova biblioteca inteira, executar inspeção de cada arquivo com scripts/inspect-video.py, agrupar por mecanismo e gerar uma ficha no formato templates/reference-study.json. Identificar cortes reais pela sequência de frames; medir início/fim, distância em px, escala/rotação, ritmo, overlap, timing do texto, movimento da câmera e áudio quando possível. Amostrar 2 fps para mapa geral, aumentar frequência e extrair ±2 frames nos beats críticos; não deduzir easing exato de uma amostra grosseira. Marcar observação vs estimativa vs hipótese. Criar catálogo de gestos reutilizáveis com origem, condições de uso, parâmetros iniciais e comparação visual. Não copiar elementos distintivos sem licença. O storyboard de Bitmap (Grok Bot/Allo) ensina hierarquia e relação mascote/objeto; timing só pode ser analisado no vídeo original.

## 4. Direção e storyboard
Escolher conceito por mensagem/prova, não por efeito. Fazer 3 propostas breves, selecionar uma, montar moodboard, definir visual único e banidos. Aplicar os quatro blocos do guia: inputs, direction, structure, banned; incluir dimensão, fps, paleta/fonte real, timing em segundos/frames, câmera, texto exato, voz/trilha, layout e mecanismo. Medir referência sonora em vez de escrever “música épica”. Planejar a virada que dá sentido ao filme.
Para filme de feature: abrir com resultado/benefício, mostrar 2–3 ações reais com ritmo crescente, variar plano geral do aparelho/tela e detalhe, uma transformação que amplifica o mecanismo, end card. Para esquetes: contexto, causa e reação, timing de comédia; CTA só se fizer sentido. Para aquisição: primeira prova cedo, CTA verificável. Não universalizar duração 34s nem produto em 2s para orgânico.
Feedback delta: timestamp/alvo → problema → mudança específica → magnitude/direção → o que preservar → critério de sucesso. “Mais premium” não é uma instrução válida.
 
## 5. Implementação e protótipo
Timeline única de imagem/som/captions, determinística por frame. Texto em HTML/SVG/React por cima de imagem, sem texto gerado no raster. Capturar ativos reais (HyperFrames capture ou browser local) e usar componentes/tokens atuais do produto. Comparar protótipo de 2–5s contra trecho selecionado: início, meio, fim, trajetória, peso, escala e transição. Escolher motor depois da prova, não antes se houver risco. Preferir poucas composições fortes; render preliminar pequeno. Reutilizar um gesto comprovado, não uma propaganda inteira. Para geração de imagens/vídeo, exigir direitos, consistência, orçamento e sinalização; footage autorizado apenas.

## 6. Critério de aprovação
Gate A: evidence.md com claims e direitos; B: refs/manifest com frames e transfer map; C: storyboard + timeline; D: prova de motion renderizada; E: draft + sheets, logs e crítica comparativa; F: correções rerenderizadas e export final.
Pontuar 0–5 em cada categoria: conceito, composição, hierarquia tipográfica, continuidade e peso do movimento, coreografia, prova real, copy/localização, áudio/legendas, adequação do canal. Não dar nota sem exemplo de frame ou timestamp. Comparar 3 trechos com referências profissionais e identificar o que ainda está inferior. Qualquer P0/P1 do production-qa bloqueia. Revisar sem som e com som quando possível; se não houver audição, reportar a lacuna. Um leigo deve compreender o que aconteceu sem briefing. Não maquiar uma cena ruim com efeitos. Refazer a cena quando conceito falhar.
 
## 7. Aprendizagem acumulativa
Ao fim de um job, registrar decisões, antes/depois, comandos, técnicas medidas, resultados de QA e hipóteses a testar. Ao obter métricas reais, ligar hook à retenção, clique à prática e compra, sem confundir correlação e causa. Atualizar biblioteca só com aprendizado observável, sem reintroduzir regras antigas de produto e estética. Cada novo job carrega fichas relevantes, não toda a biblioteca.
