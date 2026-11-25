# Dayform V3 — post-mortem de direção espacial
25/11/2026. V3 melhorou ritmo em relação à V2 (21,3s vs 40s), mas foi rejeitada pelo usuário como travada, 2D e pouco sofisticada. A análise anterior registrou cerca de 9,6s de baixa atividade vs 27s, método diagnóstico; não reproduzido aqui. Pacing sozinho não resolveu a linguagem.
Causa raiz: renderer Python/Pillow de composição raster, capturas planas redimensionadas, interpolação posição/escala, máscaras circulares, sombras simuladas, câmera que era crop/zoom; falta de geometria, materialidade, parallax, iluminação, deformação, coreografia e transformações causais. Interface parecia colada em fundo. Não confundir captura real com motion suficiente.
Notas editoriais anteriores /10: pacing 5,5; timing 5; composição 6; direção de arte 5; coreografia 3; sofisticação 2,5; transições 3; câmera 1; profundidade 1; materialidade 1; transformações 2; cinematografia 2; surpresa 2. Avaliação própria, não teste de público.
Teste de ambiente relatado anteriormente: Blender/Three.js não instalados, WebGL2 falhou no Chromium, VTK/EGL renderizou uma esfera iluminada. Não reexecutado nesta revisão; não comprova disponibilidade futura nem capacidade de filme completo.
## Proposta de reconstrução (ainda não produzida)
Conceito Make Time Yours: tempo tangível, blocos/hora 3D, marfim/verde-floresta/terracota, materiais foscos, bevels e luz de estúdio. 24 blocos representam horas; preservar verdade da UI Dayform e indicar elipses. Usar 3D/2.5D/2D conforme função. Duração inicial 36s a validar pelo animatic, não preencher por obrigação.
| Hipótese de beat | Mecanismo |
|---|---|
| 0–3 | macro de blocos acumulando e disputa espacial |
| 3–6 | reorganização procedural e recuo de câmera, revelar agenda |
| 6–11 | cartão emerge, ganha volume, percorre arco e encaixa no horário; prova real legível |
| 11–16 | decomposição em planos, reação do sistema ao reagendamento |
| 16–21 | simplificar ambiente; anel tridimensional do foco, luz e som contrastam |
| 21–27 | conclusão e reação coreografada do sistema |
| 27–33 | product showcase espacial com UI real, sem repetir demonstrações |
| 33–36 | match/morph do anel para símbolo original da marca; CTA legível |
Não reutilizar composições ou renderer principal das V1–V3 para esse brief. Preservar produto, prova e aprendizados de pacing. Fazer styleframes, blocking, animatic, motion test, revisão comparativa. Se motor não passar, não exportar como aprovado. O vídeo não é alterado por este commit.
