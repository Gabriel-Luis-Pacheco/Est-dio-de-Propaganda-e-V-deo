# BataTalk Creative Studio
Skill reconstruída do zero em 25/11/2026 para Claude Code, Codex e agentes compatíveis com SKILL.md. Abrange direção criativa, pesquisa de motion, publicidade, entretenimento, lançamento, aquisição, educação e B2B. Não depende de um pipeline legado.

## Instalação
```bash
git clone https://github.com/Gabriel-Luis-Pacheco/skill-propaganda-batatalk.git .claude/skills/propaganda-batatalk
```
Se já instalou via clone, faça git pull; se houver mudanças locais, faça backup antes de sincronizar. Para Codex, use a pasta de skills configurada pelo seu ambiente. Comece em [SKILL.md](SKILL.md).

## Estrutura
- references/reference-lab.md — 25 MP4 estudados por amostragem visual, mecanismos e recomendações.
- references/upstream-audit.md — regras concretas de 15 SKILL.md oficiais consultados.
- docs/validation-2026-11-25.md — testes reais, limites e reprovação criativa da prova técnica.
- references/creative-operations.md — roteamento operacional de especialistas, laboratório de referências e gates com evidência.
- templates/reference-study.json — ficha de análise por vídeo/beat.
- references/product.md — produto real, claims, identidade e localização.
- references/creative-strategy.md — estratégia, roteiro, copy, formatos, testes.
- references/reference-first.md — direção de arte e engenharia reversa por frames.
- references/motion-stack.md — motor e skills especialistas, incluindo Stewdio.
- references/video-library.md — 25 referências fornecidas e método de estudo.
- references/production-qa.md — produção, áudio, revisão e medição.
- templates/brief.md e timeline.json — contratos editáveis.
- scripts/inspect-video.py — inspeção local de MP4 com FFmpeg.
- evals/scenarios.json — cenários de regressão propostos.

Os vídeos de terceiros e links privados do Drive não fazem parte do repositório público; use as cópias autorizadas localmente. Recomendações do guia recebido são insumos, não benchmarks executados. Nenhum vídeo é prometido como renderizado nesta mudança.

## Ferramentas e testes locais
- `scripts/analyze-library.py`: FFmpeg + Pillow, 25 MP4 e 300 frames extraídos sem falha no laboratório.
- `scripts/validate-timeline.py`: valida estrutura da timeline; `python tests/test_timeline.py` cobre oito casos positivos/negativos.
- `scripts/inspect-video.py`: quatro execuções verificadas em vídeos de referência e protótipos.
- `.github/workflows/validate.yml`: regressões estruturais no push/PR; não substituem QA de render e arte.

## Atualização — direção temporal (25/11/2026)
- [Pacing, timing, roteiro, montagem e som](references/pacing-timing-editing.md): animatic-first obrigatório e gate de qualidade temporal.
- [Post-mortem Dayform](docs/dayform-pacing-postmortem.md): regressão editorial, evidências e causa raiz.
- [Template de auditoria temporal](templates/pacing-review.md).
- Analisador de baixa atividade (diagnóstico, não julgamento de ritmo): instale NumPy no ambiente isolado e FFmpeg local; `python scripts/analyze-pacing.py video.mp4 --timeline timeline.json --out qa/pacing.json`. Rode `python tests/test_pacing.py`. Testes unitários usam frames sintéticos; não representam teste de audiência ou validação artística. O workflow inclui essas regressões; verificar execução CI.

## Atualização — motion cinematográfico e stack curada (25/11/2026)
- [Stack ativa e roteador](references/motion-stack.md): Blender+bpy como rota 3D local, C4D/Redshift, Houdini/Karma, Unreal e AE/Fusion condicionais; HyperFrames/Remotion/GSAP para UI/híbrido. Ferramentas auxiliares não substituem motor artístico.
- [Direção espacial e animação](references/spatial-motion-direction.md): styleframes, blocking, câmera, geometria, materiais, curvas, transformações, composição e gate espacial.
- [Auditoria tecnológica](docs/motion-technology-audit.md) e [Dayform V3 post-mortem](docs/dayform-motion-postmortem.md): capacidades documentadas, limitações e decisões; sem alegar benchmarks ou instalação.
- [Shot plan](templates/motion-shot-plan.md): contrato de produção por shot. Não há vídeo novo neste commit.

## Atualização — taste, sound design e arsenal real
- [Direção de propaganda](references/advertising-taste.md): gates de conceito, styleframes, montagem, coreografia, timing, surpresa e contraste.
- [Direção sonora](references/sound-direction.md), [32 candidatos CC0](assets/audio/README.md), [manifesto](assets/audio/manifest.json) e [cue sheet](templates/sound-cue-sheet.md).
- [Análise computacional de áudio das 25 referências](docs/reference-audio-audit.md): energia por trecho; não equivale a audição, BPM ou qualidade.

## Creative Studio OS — nova base prática
- [Motion Arsenal](arsenal/motion/README.md): 24 estudos SVG próprios, galeria animada, código, export de frames, 124 shot cards upstream indexados.
- [Audio Studio](arsenal/audio/README.md): 2357 candidatos Foley indexados; 32 assets locais prévios. Não foram ouvidos nesta rodada.
- [Arsenal visual](arsenal/visual/README.md), [diretor criativo](references/creative-director.md), [orquestração](references/studio-orchestration.md).
- [12 briefs de benchmark](evals/creative-benchmark/README.md), [status e limites](docs/creative-os-status.md).

### Laboratório operacional
- [Motion DNA](docs/motion-dna-lab.md): optical flow, candidatos de corte/ataque, resultados reais de dois MP4.
- [Dois estudos 3D reais](arsenal/spatial/README.md): geometria, materiais, câmera e luz; VTK/EGL contingência.
- `scripts/render-motion-preview.py`: export de estudos SVG para MP4 (CairoSVG + Node + FFmpeg), smoke CI ainda não confirmado.
- `scripts/score-blind-benchmark.py`: sumariza votos reais cegos, sem fabricar dados.

## Trava de pré-produção (segunda regressão AbacatePay)
- [Protocolo G0–G5](references/creative-preproduction-lock.md), [18 regressões](docs/abacatepay-v2-regression.md), [12 drills](references/motion-craft-drills.md).
- `python scripts/stage-gate.py JOB --through G0` e repetir até G4 antes de render completo; G5 após draft. [Manifesto](templates/stage-manifest.json), SHA256 de evidências, predecessor e master. Release CLI exige histórico G0–G5. `python tests/test_stage_gate.py` testa estrutura; fixture sintética não valida arte. Não há novo vídeo ou benchmark artístico nesta mudança.
