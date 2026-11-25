# Stack de produção — seleção por missão e qualidade
Revisão 25/11/2026. Esta é a lista ativa e substitui qualquer prioridade histórica (incluindo HyperFrames-first para todo launch). Capacidade documentada não é benchmark de qualidade nem disponibilidade local. Não instalar tudo; escolher um motor principal por shot, um compositor/encoder e especialistas necessários. [Direção espacial e movimento](spatial-motion-direction.md) e [pacing](pacing-timing-editing.md) são gates independentes. [Auditoria das tecnologias](../docs/motion-technology-audit.md) contém evidências e exclusões.

## 1. Núcleo recomendado para agentes
| Tecnologia | Papel e missão ideal | Limite / decisão operacional |
|---|---|---|
| [Blender](https://www.blender.org/) + [bpy](https://docs.blender.org/api/current/info_quickstart.html) + Geometry Nodes + Cycles/EEVEE | **Primeira opção para launch premium 3D local e automatizável**: geometria real, instâncias, deformações, câmera, rigs, materiais, iluminação, passes | EEVEE para iteração quando compatível; Cycles para lookdev/final conforme custo e aparência. CPU/GPU e versão testados. Exportar .blend, script e sequência. Não prometer instalação. |
| [Three.js](https://threejs.org/) + [React Three Fiber](https://r3f.docs.pmnd.rs/) | 3D de produto code-driven, câmera, instancing, morph targets, PBR, shaders e pós-processamento; UI híbrida | Exige backend WebGL2/WebGPU efetivamente funcional no ambiente de render; testar readback e determinismo. Não confundir CSS perspective com geometria real. |
| [HyperFrames](https://github.com/heygen-com/hyperframes) + [GSAP](https://gsap.com/docs/v3/) | composição HTML determinística, UI, tipografia cinética, captura de produto, timeline e exportação; pode integrar 3D via adapter Three.js | Ótimo para lançamento UI-first ou compor passes 3D, não substitui motor 3D. Ler skills oficiais da versão e verificar CLI/telemetria. |
| [Remotion](https://www.remotion.dev/docs/) + [@remotion/three](https://www.remotion.dev/docs/three) | React/frame-driven, variantes multilíngues e programáticas, composição, integração R3F | Conferir licença e backend antes de usar; uma única fonte de tempo via frame, sem loops em relógio real. |
| [GSAP](https://gsap.com/docs/v3/Plugins/) | timeline, MotionPath, MorphSVG, Flip, SplitText, CustomEase, stagger e sobreposição | Biblioteca de animação, não renderer/encoder. Seek por frame; plugins conforme licença atual, não enfeitar toda palavra. |
| [DaVinci Resolve/Fusion](https://www.blackmagicdesign.com/products/davinciresolve/fusion) | montagem, composição node-based 2D/3D, color, tracking, Fairlight; alternativa de acabamento profissional | Escolher recursos conforme edição/OS/licença e automação disponível. Usar GUI ou API real, nunca inventar execução. |
| [FFmpeg/FFprobe](https://ffmpeg.org/) | ingestão, mux, transcode, composição simples, proxies, análise, áudio e exportação | **Auxiliar**, não motor criativo principal; não usar zoompan/fade como substituto de direção de animação. |
| [Playwright](https://playwright.dev/) | capturar e verificar UI real, estados, fontes e render determinístico de composições web | **Auxiliar**, não motion engine por si só. Capturas são prova ou textura, não filme inteiro. |

## 2. Stack de estúdio profissional (quando acesso e licença existirem)
| Tecnologia | Usar quando | Limite |
|---|---|---|
| [Cinema 4D + Redshift](https://www.maxon.net/en/solutions/3d-motion-design) | MoGraph Cloner, Fields, Effectors, extrusão, arrays, procedural e render GPU de campanha | Comercial; exigir licença/hardware, projeto e export testados. Não assumir acesso remoto. |
| [Adobe After Effects](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/animation-basics/animation-basics.html) | animação gráfica premium, shapes, máscaras, tipografia, Graph Editor, expressions, composição 2.5D e Advanced 3D | Comercial; não tratar camadas planas como malhas volumétricas. Para simulações complexas preferir 3D dedicado. |
| [Houdini + Solaris/Karma](https://www.sidefx.com/industries/motion-graphics/) | simulações, VFX, procedural complexo, instancing, deformações, USD, lookdev | Alto custo de aprendizagem/hardware; verificar edição e restrições comerciais/formatos. Só quando efeito justifica. |
| [Unreal Engine Motion Design + Sequencer/MRQ](https://dev.epicgames.com/documentation/en-us/unreal-engine/motion-design-quickstart-guide-in-unreal-engine) | ambientes real-time, cloners/effectors, virtual cameras, materiais e grandes cenas | GPU/driver, plugins e versão testados; conferir licença; MRQ para sequência e subamostragem temporal. |
| [Fusion](https://www.blackmagicdesign.com/products/fusion/) | composição, integração de passes 3D, máscaras, tracking e acabamento | Usar se disponível, não exigir suíte paga. |

## 3. Especialistas — não motores universais
- [Cavalry](https://cavalry.studio/docs/): motion 2D procedural, padrões, sistemas de design e tipografia; ótima alternativa 2D deliberada em macOS/Windows. Conferir versão/automação/licença.
- [Rive](https://rive.app/editor): rig vetorial, state machines, atuação de Tato e personagens, export/render conforme versão. Para vídeo usar captura determinística ou export suportado, não reimplementar personagem com slides.
- [Motion Canvas](https://motioncanvas.io/docs/): explicadores, diagramas e visualização matemática em TypeScript; não substituir composição 3D.
- [PixiJS](https://pixijs.com/8.x/guides/components/renderers): sprites, filtros, sistemas gráficos acelerados, efeitos 2D; não padrão de launch. Validar backend e necessidade.
- Lottie: reprodução de animação vetorial existente (verificar recursos suportados); não autorar filme principal com catálogo de presets.
- [VTK](https://examples.vtk.org/site/Cxx/Rendering/PBR_Materials/) / PyVista: 3D programático de contingência técnica (geometria, PBR, câmera). Principalmente visualização científica, sem pipeline criativo completo equivalente a Blender. Somente se prova de 2–5s demonstrar acabamento suficiente; nunca usar esfera isolada como prova de filme completo.
- Modelos generativos de vídeo/imagem (Veo, Seedance e outros): footage/lifestyle ou plano específico sob licença, autorização de custo e controle de consistência. Não gerar UI, números, copy ou prova de produto por pixels. Não recomendar modelo por hype nem inventar benchmark; consultar fontes atuais e testar caso específico.
- Python/NumPy/Pillow: análise, máscaras utilitárias, pré-processamento, automação, atlas/texturas e comp auxiliar. **Não** motor de filme premium se resultado for screenshot + crop + escala + sombra simulada. Python com bpy é outra categoria (controle de motor 3D real).

## 4. Roteador que manda na escolha
| Missão | Principal | Complemento |
|---|---|---|
| Filme de lançamento premium / hero CGI / metáfora física | Blender+bpy (ou C4D/Houdini/Unreal se realmente disponíveis e adequados); Three.js para 3D code-native se prova aprovada | GSAP/HyperFrames/Remotion para UI e tipografia, composição e FFmpeg |
| Launch exclusivamente UI-first com motivo editorial | HyperFrames+GSAP ou Remotion; 3D real quando o conceito pede | Captura Playwright e câmera 2.5D, Three.js ou passes Blender |
| Motion gráfico abstrato | Blender Geometry Nodes/C4D MoGraph/Houdini; Cavalry/GSAP se estética 2D comprovada | Composição e sound design |
| Personagem / humor | Rive, Blender rig, After Effects conforme assets | edição e lip sync validado |
| Educação/diagrama | Motion Canvas, GSAP ou Remotion | 3D somente quando explica |
| UGC / entrevista / tutorial filmado | Resolve/Fusion ou edição programática FFmpeg/HyperFrames | Captions, áudio, prova real |
| Variantes em escala | Remotion ou HyperFrames + reutilização de passes 3D | Localização, QA por versão |

2D deliberado de alta qualidade é legítimo. 3D não é selo automático de qualidade. Para pedido de alto impacto cinematográfico, plano 3D hero + interação híbrida + transição espacial é default editorial, não cota. Se referência/conceito justificar 2D, documentar como alcançará a mesma sofisticação.

## 5. Preflight e política de fallback
1. Checar OS, CPU, GPU/VRAM, drivers, espaço, binários, versão estável/LTS e permissões. Checar licenças, termos, custos e telemetria. Não instalar em sistema do dono, chamar API paga ou enviar dados sem autorização.
2. Blender: verificar `blender --version`, API bpy correspondente à versão, render offline com `blender -b <scene.blend> -a` ou `blender -b -t <n> --python <script.py>`. Usar scene.frame_set, seed, keyframes/curvas, frames consistentes. Não usar comandos de edição não autorizados.
3. Browser 3D: confirmar WebGL2/WebGPU, shader compile, texturas, câmera, captura de frames; teste em backend real do render, não só navegador interativo. Usar seek determinístico, fontes/ativos prontos.
4. Renderizar prova curta representativa com dois materiais, sombra/oclusão, objeto de volume, câmera em movimento, gesto complexo, UI legível e áudio guia se aplicável. Validar custo de render e orçamento: medir tempo real por frame, extrapolar como estimativa com margem, não sacrificar imagem às cegas.
5. Se motor primário indisponível, avaliar alternativa da mesma categoria. Se nenhuma passar, entregar estudo/animatic rotulado ou pedir autorização específica para ambiente capaz. **Não** degradar silenciosamente 3D premium para Pillow ou pan/zoom e chamar final profissional.
6. Sequência PNG/EXR por shot, cache, rerender frames defeituosos, master com cores consistentes, encode e verificação. Guardar fonte, assets/licenças, versão, comandos, logs, tempo e limitações. Não inventar 4K nativo por upscale.

## 6. Skills selecionadas e descarte de catálogo
Ler SKILL.md oficial relevante, aplicar 2–5 regras, não baixar cegamente dezenas. Rotas ativas:
- HyperFrames: https://github.com/heygen-com/hyperframes (skills oficiais de core/animação/motion graphics, captura, reverse-any-video e style-sampling conforme versão).
- Remotion: https://github.com/remotion-dev/skills
- GSAP: https://github.com/greensock/gsap-skills
- Stewdio: https://github.com/StewdioAI/stewdio-skills (referência e screens-to-video; não requisito de serviço).
- LottieFiles: https://github.com/LottieFiles/motion-design-skill (princípios de movimento, não imposição de renderer).
- Claude Motion: https://github.com/whaleyxbt/claude-motion (review-loop e timing; complementar, screenshots insuficientes).
- Video Shotcraft: https://github.com/Vincentwei1021/video-shotcraft (captura real), Marketing Skills: https://github.com/coreyhaines31/marketingskills (estratégia), FFmpeg docs (engenharia).
- Blender, C4D, Houdini, AE, Fusion e Unreal: documentação oficial/API antes de skills comunitárias. Skills próprias Best-Designer e skill-ceo somente quando pertinentes.
As demais referências históricas não são dependências ativas; consulte upstream-audit apenas como histórico de evidência. Removidos da rota principal catálogos de estilos/presets, geradores de template redundantes e receitas HTML+Pillow de baixa sofisticação. Não atribuir inferioridade universal sem teste. A qualidade é avaliada pela cena renderizada, não pelo nome do software.
