# Stack e especialistas sob demanda
Recomendação de engenharia, não benchmark testado. Verifique documentação, licença, versão, custos, telemetria e disponibilidade antes de executar. Não instalar todos os módulos. Registrar comando real, origem e versão. Se faltar acesso, usar fallback e declarar. Não redistribuir skill sem licença explícita.
 
## Motores
- HyperFrames / HeyGen: padrão inicial para motion ads, launch films, texto e UI, HTML/CSS/GSAP → MP4 determinístico. https://github.com/heygen-com/hyperframes . Guia relata claude plugin marketplace add heygen-com/hyperframes e claude plugin install hyperframes@hyperframes; verificar comandos atuais. Consultar capture, registry, reverse-any-video, style-sampling, media-use, check, render, Studio. Opt-out de telemetria se possível. Não confundir com mídias/serviços pagos.
- Remotion: React, templates repetíveis, dados e versões em escala. https://github.com/remotion-dev/skills ; https://www.remotion.dev/docs/license/pricing . Guia relata gratuidade comercial condicionada a equipe de até 3; verificar termos atuais, não assumir licença da skill. npx skills add remotion-dev/skills ou npx remotion skills add conforme docs atuais.
- HTML + Playwright + FFmpeg: fallback determinístico local, controle por frame, composição e exportação. https://ffmpeg.org/
- Motion Canvas: explicadores, diagramas code-driven. https://github.com/motion-canvas/motion-canvas
- Motion (Motiondivision) e GSAP: UI, springs, layout e timelines; não são por si só encoder. https://github.com/motiondivision ; https://github.com/greensock/gsap-skills
- Blender: 3D, câmera, material e rig quando justificável. https://github.com/EL4CTEO/blender-skills
- Rive / Lottie: interação e personagem; usar rig real existente, captura/export apropriada. https://rive.app/ ; https://lottiefiles.com/
- Modelos generativos (Veo/Seedance/outros) e footage: UGC/lifestyle, somente quando sentido, licença e custo aprovado; não gerar UI/texto por pixels.
 
## Skills por função (fontes do guia e prints)
| Skill / fonte | Usar para |
|---|---|
| https://github.com/StewdioAI/stewdio-skills | blank-page e screens-to-video; MIT; referências e storyboard, câmera, recorte de UI e timeline. Instalação npx skills add StewdioAI/stewdio-skills --skill blank-page ou screens-to-video. Stewdio/Revyl podem exigir conta, limite e watermark; preferir fallback local se necessário. |
| https://aiforui.dev/skills ; https://github.com/emilkowalski/skills | UI motion, springs, easing, gesto e timing |
| https://designbookmark.com/motion | referências e componentes; verificar licença antes de copiar |
| https://github.com/LottieFiles/motion-design-skill | gosto, 12 princípios de animação, easing, coreografia |
| https://github.com/whaleyxbt/claude-motion | timing, sound design e review-loop por contact sheets |
| https://github.com/Vincentwei1021/video-shotcraft | shots e capturas de produto real |
| https://github.com/AbubakrChan/product-launch-motion | launch film, storyboard, HTML/Playwright |
| https://github.com/charlie947/motion-graphics-skills | launch, reels, gráficos, kinetic typography, referências |
| https://github.com/howseen-ai/claude-motion-design | pipeline local HTML + Playwright + FFmpeg |
| https://github.com/coreyhaines31/marketingskills/tree/main/skills/video | estratégia, roteiro, CRO, copy |
| https://github.com/Nutlope/hallmark | anti-slop e crítica visual |
| https://github.com/browser-use/video-use | edição de footage, remoção de filler, transcrição |
| https://github.com/kajisho5/ffmpeg-skill | edição, conversão e diagnóstico técnico |
| https://github.com/nateherkai/hyperframes-student-kit | exemplos e footage |
| https://github.com/showheyohtaki/motion-prompt | catálogo de movimentos e vocabulário |
| https://github.com/Vincentwei1021/mg-styles-15 | estilos e código de referência |
| https://github.com/iart-ai/motion-skills | social, explicadores e motion |
| https://github.com/heygen-com/hyperframes-launches | composições reais de lançamento |
| https://github.com/Gabriel-Luis-Pacheco/Best-Designer-in-the-World.- | direção e crítica complementar se instalada |
| https://github.com/Gabriel-Luis-Pacheco/skill-ceo | estratégia e experimentos se instalada |
 
Instalação por projeto com npx skills add OWNER/REPO após conferir README/licença. Não importar tudo, não copiar textos sem direitos. OpenMontage AGPL-3.0 relatada pelo guia: não integrar sem análise. Conteúdo de X copiado/repostado não é comprovação de origem; ir à fonte. Popularidade e estrelas não medem qualidade.
 
## Gramática de movimento
Heurísticas iniciais de claude-motion: entrada cubic-bezier(0.16,1,0.3,1), saída cubic-bezier(0.6,0,0.9,0.35), saída ~metade da entrada, stagger palavras ~90ms e itens ~200ms; um gesto elástico forte pode bastar. Ajustar por intenção e referência. Antecipação, arcos, follow-through, peso, staging, timing, squash/stretch quando adequado; continuidade de layout e foco. Usar câmera e transição para revelar informação, não enfeite. Som alinhado à ação e timeline; sem CSS time real/Math.random sem seed em render determinístico.
