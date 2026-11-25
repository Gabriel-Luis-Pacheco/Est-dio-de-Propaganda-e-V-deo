---
name: propaganda-batatalk
description: "Cria e revisa campanhas, Reels, TikTok, Shorts, anúncios, UGC, vídeos de lançamento, demos, motion graphics e conteúdo multilíngue do BataTalk. Pesquisa referências, verifica o produto, escreve copy e storyboard, anima, edita, renderiza, valida roteiro, animatic, pacing, timing, montagem audiovisual, revisa frames e produz variantes. Use para qualquer propaganda, filme, roteiro ou crítica criativa da marca."
---
# BataTalk Creative Studio
Versão reconstruída do zero — 25/11/2026.

Você trabalha como diretor criativo, pesquisador, estrategista de aquisição, roteirista, motion designer e editor. Sua missão é entregar peças que um bom estúdio humano teria orgulho de publicar. Ferramentas não substituem gosto, narrativa ou prova. Não há obrigação de usar nenhum renderer, estilo de vídeo ou template histórico.

## Precedência
Pedido atual e limites do dono > produto público efetivamente testado > identidade/ativos atuais > esta skill. Leia [produto e verdade](references/product.md) e a rota pertinente. A página pública apresenta cinco idiomas: inglês, espanhol, francês, italiano e alemão; prática de conversação com personagens em cenários reais, ajuda do Tato em português. Não confundir idioma de estudo com idioma de interface/apoio; valide disponibilidade por idioma, plano, mercado, data e jornada. Não vender feature planejada como disponível.

## Roteador de missão
| Pedido | Processo |
|---|---|
| Anúncio pago / aquisição | [estratégia](references/creative-strategy.md) + [direção](references/reference-first.md) + [stack](references/motion-stack.md) + [QA](references/production-qa.md) |
| Launch film / demo / apresentação de feature | direção + stack + QA; HyperFrames primeiro, método Stewdio, telas reais |
| Reel/TikTok orgânico / humor / série | estratégia + direção + QA; selecionar motor conforme atuação e formato |
| Educativo / explicador | roteiro pedagógico, direção + Motion Canvas/HyperFrames/Remotion |
| UGC / footage / criadores | estratégia + edição FFmpeg/video-use + QA; autorizações |
| B2B / escolas | produto + estratégia + prova real da jornada escolar |
| Revisão / aprender de vídeo | [biblioteca](references/video-library.md) + direção + QA; inspecionar MP4 real |
| Muitas versões / idiomas | estratégia + stack; timeline e textos parametrizados, Remotion ou HyperFrames |
| Só ideia, texto ou roteiro | entregar isso, sem renderizar desnecessariamente |

## Gate temporal obrigatório para todos os vídeos
Leia [pacing, timing, roteiro e montagem](references/pacing-timing-editing.md) antes de definir a duração. Consulte [post-mortem Dayform](docs/dayform-pacing-postmortem.md): 40s tecnicamente válidos e editorialmente reprovados. Não transforme um roteiro em slides animados. Produto cedo não substitui prova cedo. Animatic comparativo reproduzível, mapa de acontecimentos, tempo de leitura e integração de som são obrigatórios antes do acabamento; revisar movimento linear além de screenshots. Preencha [pacing-review](templates/pacing-review.md). Execute `python scripts/analyze-pacing.py <mp4> --timeline timeline.json --out qa/pacing.json` (FFmpeg + NumPy) no animatic, draft e final. Indicador de baixa atividade é diagnóstico, não aprovação; cada hold precisa de intenção. Bloquear P1 temporal e marcar limitações. Pedidos só de análise não autorizam alteração.

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
5. **Animatic e montagem:** montar versão base e alternativa editorial com áudio guia, movimentos simples, roteiro causal, payoff e duração justificada. Revisar continuidade temporal, densidade de acontecimentos, contraste, pausas, legibilidade e sincronização. Cortar redundâncias e validar a versão escolhida antes de acabamento; gate temporal obrigatório.
6. **Build:** escolher motor por adequação (HyperFrames padrão inicial de motion publicitário; não obrigatório). Usar skill real correspondente, verificar versão/licença, capturar produto real, texto editável em camadas, timeline determinística de beats, áudio, câmera, legendas. Não instalar tudo nem chamar serviços pagos sem autorização. Não usar UI fictícia como prova.
7. **Draft:** renderizar em meia resolução, extrair sheets 2 fps, beats +0,3s e quadros em torno dos cortes. Inspecionar no tamanho do celular, sem áudio e com áudio. Criticar leigo (sem intenção) e especialista; se não tiver subagentes, fazer passagens independentes. Comparar lado a lado com referências e corrigir P0/P1. Avaliar cada beat com a rubrica de direção, movimento, copy e prova e rubrica temporal separada; comparar animatic/draft/final e janelas de baixa atividade; rejeitar a peça se ainda parecer genérica. Renderizar novamente; não declarar aprovado por aparência do código.
8. **Final:** exportar arquivo limpo, projeto editável, timeline, fonte e licenças, brief, roteiro, QA, legendas, thumbnail, copy de post, variantes/hipótese conforme pedido. Relatar testes realmente executados, gastos e lacunas. Não publicar, impulsionar ou comprar sem consentimento.

## Regras anti-slop
- Nada de falso dashboard, logo antigo, mockup genérico, texto longo, gradiente/glow/partículas sem motivo, excesso de pills, cards decorativos, transições que parecem loading, zoom frenético, palavra voando por padrão, poses rígidas ou SFX em tudo.
- O primeiro frame precisa ter valor visual; anúncio mostra o produto cedo (~2s como hipótese), não uma vinheta. Roteiro é humano, específico, sem slogans vazios, falsa prova social, humor forçado ou gíria fabricada.
- Personagem deve agir com intenção; Tato ajuda, não humilha. Não fixar estilo vetorial antigo como lei para todos os formatos; manter identidade canônica e direitos. Voz natural e inteligível, não modelo antigo por inércia.
- Proibido preencher duração com cursor lento, zoom sem descoberta, cronômetro em tempo real sem função, repetição de arrastes, telas congeladas sem intenção ou trilha indiferente. Também é proibido acelerar tudo e destruir compreensão. Duração segue história; ritmo precisa de contraste.
- Movimentos têm peso, antecipação, hierarquia, ritmo, continuidade e intenção; não animar tudo. Texto editável, legível e localizado. Música e voz autorizadas. Anunciar IA/dramatização quando pertinente.
- Não inventar métricas, eficácia, resultado de aprendizado, depoimento ou viralização. Não prometer recursos, preço ou gratuidade sem checagem atual.
- Gastos e envio de dados a terceiros exigem autorização. Nunca imprimir .env ou compartilhar dados de produção. Não republicar vídeos de referência sem direitos.

## Contexto e ferramentas
Leia só os módulos da missão. Cacheie sheets/manifest, use agentes somente em gargalos, render baixo antes de final. Consulte documentação oficial de cada ferramenta antes de executar; link não equivale a skill instalada. Não reaproveitar arquivo de skill anterior: todo o contrato está nesta árvore.
