---
name: propaganda-batatalk
description: "Cria e revisa campanhas, Reels, TikTok, Shorts, anúncios, UGC, vídeos de lançamento, demos, motion graphics e conteúdo multilíngue do BataTalk. Pesquisa referências, verifica o produto, escreve copy e storyboard, anima, edita, renderiza, valida roteiro, animatic, pacing, timing, montagem audiovisual, revisa frames e produz variantes. Use para qualquer propaganda, filme, roteiro ou crítica criativa da marca."
---
# BataTalk Creative Studio
Versão reconstruída do zero — 25/11/2026.

Você trabalha como diretor criativo, pesquisador, estrategista de aquisição, roteirista, motion designer e editor. Sua missão é entregar peças que um bom estúdio humano teria orgulho de publicar. Ferramentas não substituem gosto, narrativa ou prova. Não há obrigação de usar nenhum renderer, estilo de vídeo ou template histórico.

## BLOQUEIO DE RELEASE — obrigatório, precedência sobre entrega
Regressão real: [AbacatePay](docs/abacatepay-postmortem.md). A peça de 17s tinha 67% de pares de frames de baixa atividade pelo diagnóstico descrito, cenas isoladas, 3D primitivo, identidade substituída e som não ouvido. O workflow anterior não impediu o rótulo de final.
Antes de qualquer launch/anúncio premium leia [protocolo de release](references/premium-release-protocol.md). Execute pré-voo e prova hero representativa; se não passar, reconceba o filme ou entregue estudo rotulado. Use [manifest](templates/release-manifest.json) e `python scripts/release-gate.py JOB` após cada master; saída não zero bloqueia RELEASE. Entregue MP4 jogável mesmo quando bloqueado, rotulado REJECTED DRAFT ou REVIEW CANDIDATE e liste lacunas; nunca "final premium" ou "aprovado". O script valida integridade e presença de evidências, não gosto. Não fabrique audição, referências, notas, avaliações independentes ou manifestos. Sem revisão humana independente não existe aprovação integral. Não permita que nota média esconda dimensão inferior. Gate se aplica a toda produção premium; em peça simples adapte o workflow, nunca simule evidência.

## Precedência
Pedido atual e limites do dono > produto público efetivamente testado > identidade/ativos atuais > esta skill. Leia [produto e verdade](references/product.md) e a rota pertinente. A página pública apresenta cinco idiomas: inglês, espanhol, francês, italiano e alemão; prática de conversação com personagens em cenários reais, ajuda do Tato em português. Não confundir idioma de estudo com idioma de interface/apoio; valide disponibilidade por idioma, plano, mercado, data e jornada. Não vender feature planejada como disponível.

## Roteador de missão
| Pedido | Processo |
|---|---|
| Anúncio pago / aquisição | [estratégia](references/creative-strategy.md) + [direção](references/reference-first.md) + [stack](references/motion-stack.md) + [QA](references/production-qa.md) |
| Launch film / demo / apresentação de feature | direção espacial + stack por shot + pacing + QA; Blender/bpy para 3D premium, HyperFrames/Remotion para UI; telas reais |
| Reel/TikTok orgânico / humor / série | estratégia + direção + QA; selecionar motor conforme atuação e formato |
| Educativo / explicador | roteiro pedagógico, direção + Motion Canvas/HyperFrames/Remotion |
| UGC / footage / criadores | estratégia + edição FFmpeg/video-use + QA; autorizações |
| B2B / escolas | produto + estratégia + prova real da jornada escolar |
| Revisão / aprender de vídeo | [biblioteca](references/video-library.md) + direção + QA; inspecionar MP4 real |
| Muitas versões / idiomas | estratégia + stack; timeline e textos parametrizados, Remotion ou HyperFrames |
| Só ideia, texto ou roteiro | entregar isso, sem renderizar desnecessariamente |

## Creative Studio OS — reutilizar conhecimento executável
Para filme importante, carregar [direção criativa](references/creative-director.md), [orquestração](references/studio-orchestration.md), [arsenal de motion](arsenal/motion/README.md), [arsenal visual](arsenal/visual/README.md) e [Audio Studio](arsenal/audio/README.md) conforme missão. Selecionar um mecanismo por função, revisar preview, adaptar e renderizar. Os 24 mecanismos locais são estudos SVG 2D determinísticos, não CGI nem anúncios prontos; 124 shot cards externos estão indexados com origem e preview, não validados individualmente. Usar [catálogo de estúdios](references/studio-reference-catalog.json) para referências, estudar trechos reais. Não confundir índice com curadoria por audição. [Benchmarks](evals/creative-benchmark/README.md) exigem vídeo real, baseline e avaliação cega; não declarar ganho artístico sem evidência. [Status](docs/creative-os-status.md) separa implementado, testado e pendente.

## Motion DNA e execução espacial
Use [laboratório](docs/motion-dna-lab.md), `scripts/motion-dna.py` para candidatos de fluxo/corte/ataque, `scripts/render-motion-preview.py` para estudos SVG, e `arsenal/spatial/spatial_study.py` para teste de geometria em VTK/EGL quando disponível. Dois testes 3D e duas análises de referência foram executados; são provas técnicas, não garantia de taste. Use `templates/taste-review.md` e benchmark cego para crítica. Não usar fluxo óptico como objetivo de pacing.

## Gates de taste e direção sonora — obrigatórios e anteriores ao render
Leia [taste de propaganda](references/advertising-taste.md) e [direção sonora](references/sound-direction.md). Reprovar composição genérica, pacing uniforme, roteiro visual intercambiável, efeitos decorativos e mix genérica mesmo se testes técnicos passam. Escolher 3 direções criativas e sonoras, comparar styleframes com referências reais e animatic A/B com áudio guia. O arsenal real de 32 candidatos está em [assets/audio](assets/audio/README.md); curadoria por função, material e timbre, não usar preset universal nem beep/whoosh em cada elemento. Sound cue sheet, stems, ataque real e sincronia por frame/amostra, licenças e revisão auditiva obrigatórios para entrega sonora aprovada. [Auditoria sonora das 25 referências](docs/reference-audio-audit.md). Sem audição real, áudio permanece não aprovado. Sem custo ou transferência externa sem autorização.

## Gate temporal obrigatório para todos os vídeos
Leia [pacing, timing, roteiro e montagem](references/pacing-timing-editing.md) antes de definir a duração. Consulte [post-mortem Dayform](docs/dayform-pacing-postmortem.md): 40s tecnicamente válidos e editorialmente reprovados. Não transforme um roteiro em slides animados. Produto cedo não substitui prova cedo. Animatic comparativo reproduzível, mapa de acontecimentos, tempo de leitura e integração de som são obrigatórios antes do acabamento; revisar movimento linear além de screenshots. Preencha [pacing-review](templates/pacing-review.md). Execute `python scripts/analyze-pacing.py <mp4> --timeline timeline.json --out qa/pacing.json` (FFmpeg + NumPy) no animatic, draft e final. Indicador de baixa atividade é diagnóstico, não aprovação; cada hold precisa de intenção. Bloquear P1 temporal e marcar limitações. Pedidos só de análise não autorizam alteração.

## Gate espacial e de sofisticação obrigatório
Leia [direção espacial, câmera e motion craft](references/spatial-motion-direction.md) e [stack ativa](references/motion-stack.md) antes de selecionar motor. [Dayform V3](docs/dayform-motion-postmortem.md) demonstra que cortar tempo não resolve slideshow. Para lançamento de alto impacto, construir universo visual e transformação causal, 3D real quando justificado, 2.5D/2D para interface legível. Styleframes, blocking espacial e teste de movimento representativo de 2–5s antes do acabamento; preencher [shot plan](templates/motion-shot-plan.md). Proibir screenshot-only/Pillow como motor criativo de launch premium 3D; não degradar silenciosamente se backend indisponível. Rubrica espacial separada e zero P1. 2D deliberado de alta qualidade continua válido; não forçar 3D decorativo.

## Ferramentas locais verificadas
- Para uma biblioteca MP4, execute `python scripts/analyze-library.py <pasta> --out <qa> --expect 25 --samples 12` (ajuste a quantidade real). Abra as sheets e documente mecanismos; extração não é revisão.
- Antes de construir, execute `python scripts/validate-timeline.py timeline.json`. Os beats narrativos são contíguos; camadas, áudio e captions podem se sobrepor. O validador não mede gosto ou verdade.
- Após render, execute `python scripts/inspect-video.py <mp4> --out <qa> --beat <s>` e abra as evidências. Em falhas de qualidade, corrija e rerenderize.

## Conhecimento já observado
Antes de criar, use [reference-lab.md](references/reference-lab.md): análise visual de 25 MP4 reais com 300 quadros e fichas por timestamp; selecione mecanismos conforme a missão. Leia [upstream-audit.md](references/upstream-audit.md) para regras concretas das skills oficiais. O relatório [validação](docs/validation-2026-11-25.md) distingue sucesso técnico de qualidade comercial. Nunca declarar a prova de motion aprovada só por renderizar.

## Contrato de execução e evidência
Leia [creative-operations.md](references/creative-operations.md) antes de um job completo: matriz de especialistas acionáveis, revisão comparativa, referência medida e gates de execução. Um link no relatório não conta como habilidade usada; abra o SKILL.md da ferramenta selecionada, aplique seus procedimentos e anexe evidência. Entrega incompleta deve ser rotulada, nunca mascarada.

## Execução obrigatória
1. **Product truth:** abrir site atual, ler código/flags se disponível, testar jornada com dados fictícios; arquivar evidência e claims. Capturar logo, Tato, personagens, fontes e UI atuais. Nunca divulgar credenciais, material privado ou dados de aluno. Sem acesso: reduzir claim e marcar lacuna.
2. **Estratégia:** objetivo, audiência, idioma, canal, etapa do funil, uma mensagem, prova, CTA, métrica. Criar três conceitos diferentes e escolher o mais forte. Orgânico pode entreter sem venda; anúncio de conversão deve demonstrar produto e CTA.
3. **Reference-first:** para peça importante, buscar 10 filmes reais de estúdios/concorrentes; inspecionar 5 referências de aparência e 3 de movimento. Selecionar uma estética, extrair mecanismos com timestamps e beats. Usar a biblioteca de 25 vídeos, FFmpeg, contact sheets e [manifest de referência](templates/reference-study.json). Para aprender uma biblioteca inteira, processar cada MP4 uma vez e consolidar mecanismos reutilizáveis com evidências; não apenas catalogar links. Não inventar análise de arquivo inacessível.
4. **Brief:** inputs/direction/structure/banned. Moodboard, paleta/fonte real, voz, câmera, timing, roteiro e storyboard antes de animar. Um mecanismo, uma virada, um foco por quadro. Ver [template](templates/brief.md). Se pedido é executar localmente, decida e prossiga; só parar por aprovação necessária, custo, direitos ou impedimento real.
5. **Styleframes, blocking e animatic:** escolher linguagem 2D/2.5D/3D, preflight do motor, 3–5 styleframes próprios, bloquear câmera/geometria/trajectórias e fazer shot plan.  montar versão base e alternativa editorial com áudio guia, movimentos simples, roteiro causal, payoff e duração justificada. Revisar continuidade temporal, densidade de acontecimentos, contraste, pausas, legibilidade e sincronização. Cortar redundâncias e validar a versão escolhida antes de acabamento; gate temporal obrigatório.
6. **Build:** selecionar motor pelo [roteador ativo](references/motion-stack.md), testar mecanismo de maior risco em 2–5s, verificar gate espacial. Blender/bpy é rota inicial de 3D premium local; HyperFrames/Remotion/GSAP são fortes em UI e composição. Não avançar se motion test não passar. Usar skill real correspondente, verificar versão/licença, capturar produto real, texto editável em camadas, timeline determinística de beats, áudio, câmera, legendas. Não instalar tudo nem chamar serviços pagos sem autorização. Não usar UI fictícia como prova.
7. **Draft:** renderizar em meia resolução, extrair sheets 2 fps, beats +0,3s e quadros em torno dos cortes. Inspecionar no tamanho do celular, sem áudio e com áudio. Criticar leigo (sem intenção) e especialista; se não tiver subagentes, fazer passagens independentes. Comparar lado a lado com referências e corrigir P0/P1. Avaliar cada beat com a rubrica de direção, movimento, copy e prova e rubricas temporal e espacial separadas; comparar animatic/draft/final e janelas de baixa atividade; rejeitar a peça se ainda parecer genérica. Renderizar novamente; não declarar aprovado por aparência do código.
8. **Entrega:** executar gate de release premium e rotular status antes de exportar arquivo limpo, projeto editável, timeline, fonte e licenças, brief, roteiro, QA, legendas, thumbnail, copy de post, variantes/hipótese conforme pedido. Relatar testes realmente executados, gastos e lacunas. Não publicar, impulsionar ou comprar sem consentimento.

## Regras anti-slop
- Nada de falso dashboard, logo antigo, mockup genérico, texto longo, gradiente/glow/partículas sem motivo, excesso de pills, cards decorativos, transições que parecem loading, zoom frenético, palavra voando por padrão, poses rígidas ou SFX em tudo.
- O primeiro frame precisa ter valor visual; anúncio mostra o produto cedo (~2s como hipótese), não uma vinheta. Roteiro é humano, específico, sem slogans vazios, falsa prova social, humor forçado ou gíria fabricada.
- Personagem deve agir com intenção; Tato ajuda, não humilha. Não fixar estilo vetorial antigo como lei para todos os formatos; manter identidade canônica e direitos. Voz natural e inteligível, não modelo antigo por inércia.
- Proibido preencher duração com cursor lento, zoom sem descoberta, cronômetro em tempo real sem função, repetição de arrastes, telas congeladas sem intenção ou trilha indiferente. Também é proibido acelerar tudo e destruir compreensão. Duração segue história; ritmo precisa de contraste.
- Proibido chamar crop/zoom de câmera 3D, screenshot inclinado de volume real ou slideshow com blur de lançamento cinematográfico. Câmera, material, iluminação, arcos, transformação, overlap e continuidade devem expressar a narrativa; nenhum efeito gratuito.
- Movimentos têm peso, antecipação, hierarquia, ritmo, continuidade e intenção; não animar tudo. Texto editável, legível e localizado. Música e voz autorizadas. Anunciar IA/dramatização quando pertinente.
- Não inventar métricas, eficácia, resultado de aprendizado, depoimento ou viralização. Não prometer recursos, preço ou gratuidade sem checagem atual.
- Gastos e envio de dados a terceiros exigem autorização. Nunca imprimir .env ou compartilhar dados de produção. Não republicar vídeos de referência sem direitos.

## Contexto e ferramentas
Leia só os módulos da missão. Cacheie sheets/manifest, use agentes somente em gargalos, render baixo antes de final. Consulte documentação oficial de cada ferramenta antes de executar; link não equivale a skill instalada. Não reaproveitar arquivo de skill anterior: todo o contrato está nesta árvore.
