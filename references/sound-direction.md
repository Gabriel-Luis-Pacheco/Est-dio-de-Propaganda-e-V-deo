# Direção sonora: som é metade do filme
25/11/2026. Este módulo tem precedência sobre defaults anteriores de áudio. A crítica do dono: trilhas e efeitos genéricos, timing e taste fracos. O objetivo é som de propaganda autoral, não um som por objeto. Não use um loop e uma coleção de blips sintetizados como solução padrão. Não confunda volume com energia.

## 1. Começar pelo som, antes de animar
- Escreva a intenção em uma frase: emoção inicial, transformação, sensação final. Monte 3 direções contrastantes de áudio, por exemplo: foley íntimo + silêncio + resolução curta; percussão orgânica e baixo elástico; eletrônica tátil com textura analógica e crescendo modular. Não imponha essas três estéticas ao produto.
- Buscar 3 trilhas/estruturas reais com licença adequada ou encomendar/compor sob direitos claros; medir duração, frases, BPM se aplicável, entradas, breaks, quedas e resolução. Fazer shortlist de 3–5 takes por evento hero. Ouvir antes de escolher; se não puder ouvir, declarar explicitamente e não aprovar som. Não extrair trilhas/SFX dos vídeos de terceiros.
- Criar animatic com áudio guia e mapa de frases ANTES de bloquear shots finais. Voz e música têm cadência e respiração; retime por frase, não por duração arbitrária. Fazer versão A/B, com contraste real, comparar linearmente.

## 2. Arsenal real (local)
Leia assets/audio/README.md e manifest.json. São 32 arquivos candidatos CC0, não um pacote de sons automaticamente aprovados. Há material físico (madeira, papel, tecido, gaveta, passos), room tone, mouse, UI, impactos leves, transições, whooshes, risers, confirmação e digitação. Use apenas se tiver função e personalidade. Para comerciais premium, procurar masters WAV/FLAC 48kHz quando disponíveis; OGG é candidato de trabalho, converter não restaura qualidade. Não inventar material ou duração a partir do nome. Audição e licença por arquivo antes de uso.
- Foley físico: manipulação realista; gravar materiais próprios e comparar takes; recortar ataque, preservar cauda; pitch ±1–3 semitons apenas se soar natural. Construir gesto a partir de ataque + corpo + cauda/ambiente; evitar camadas redundantes.
- Micro UI: curto e discreto, apenas ações semanticamente importantes. Nunca click em cada palavra ou elemento. Repetição só por motivo rítmico ou motivo de marca. 
- Transições: som antecipado ou prolongado (J/L cut) liga planos; escolher direção, massa, distância, velocidade e material. Whoosh genérico a cada corte e riser em cada reveal são proibidos.
- Hero: uma textura ou impacto distintivo, construído em camadas; preparar contraste, silêncio parcial e resolver junto da transformação. O pico de atenção é um recurso escasso.
- Ambiência: estabelecer espaço, perspectiva e continuidade. Sem pad incessante por conveniência. Se silêncio é mais expressivo, usar silêncio.
- Marca: escolher um vocabulário tímbrico coerente; desenvolver assinatura sonora original, de 0,3–1,5s como hipótese, não imitar sonic logo conhecido. Para BataTalk: calor, curiosidade e confiança; jamais transformar Tato em máquina de beep. Não usar música de referência, vozes imitadas ou áudio sem direitos.

## 3. Curadoria externa (não redistribuir arquivos restritos)
- Sonniss GDC: https://sonniss.com/gameaudiogdc/ ; https://sonniss.com/gdc-bundle-license/ — acervo profissional para sincronização, revisar termos na data do download; sem redistribuição bruta nem treinamento de IA.
- Freesound: https://freesound.org/help/faq/ — buscar por ação/material/textura + duração; CC0 preferencial, CC-BY com crédito e licença verificável, não usar NC em anúncios; origem e autoria por arquivo.
- Mixkit: https://mixkit.co/free-sound-effects/ e https://mixkit.co/license/modal/sfxFree/ — conferir licença específica, uso final e restrição de redistribuição. Não incorporar standalone ao Git.
- Adobe Audition: https://www.adobe.com/products/audition/free-sound-effects.html — verificar EULA e permissão no uso específico.
- Artlist: https://help.artlist.io/hc/en-us/articles/29559573229725-Artlist-s-Music-and-SFX-plans-explained e Epidemic Sound: https://www.epidemicsound.com/our-plans/ — trilhas e SFX conforme licença de mídia paga, empresa, território e plano; não comprar sem autorização.
- FoleySet: https://zenodo.org/records/20735877 — conjunto descrito como CC0, selecionar gravações reais por categoria, verificar proveniência. Não usar como justificativa para treinamento.
- DAW: Reaper, Audition, Fairlight, Ableton ou equivalente realmente disponível; FFmpeg auxilia decode, alinhamento, filtros, medição e mux, não é substituto do ouvido. TTS/SFX generativo pode entrar somente com direitos, custo e avaliação aprovados.

## 4. Sound editorial e cue sheet
Use templates/sound-cue-sheet.md. Por cue: beat visual, frame de ataque/contato, ponto de saída, função, 3 candidatos quando hero, fonte/direitos, trim/offset, gain, EQ, pan, fade, bus, razão do som e razão de silêncio. Alinhar ataque real do arquivo, não começo do arquivo: se transiente a 95ms e contato em 2s, iniciar a 1,905s. Converter com FPS real, usar precisão de amostra para áudio. Conferir hit/contato em ±1–2 frames como diagnóstico, não forçar som antecipatório a coincidir. Evitar quantizar toda a ação em batida; usar síncope, contraponto, silêncio e frases. Música edita junto do filme.
- Stems separados: VO/dialogue, music, foley, UI, transitions, hero, ambience. Ganho e ducking por contexto, sem master compensar uma mix ruim. VO inteligível, removendo competição em regiões úteis e reduzindo música sob fala por automação. Impacto precisa de médios audíveis em celular, não só subgrave; stereo compatível mono, sem harshness.
- Preservar dinâmica. Não normalizar cada clip para mesmo nível. Tails e fades curtos evitando clicks; evitar limitador esmagando transientes. Medir mix e MP4 pós AAC por ebur128/true peak; -14 a -16 LUFS e <=-1 dBTP são ponto de partida social, não padrão universal. Não forçar mix silenciosa a -14.
- Check auditivo: ouvir mix em volume baixo, celular/mono, fone e sem imagem. Verificar ruído, repetição, espacialidade, timbre, harmonia, tensão/liberação e inteligibilidade. Depois ver com imagem e mudo; avaliar os dois. Se não houver audição real, relatório AUDIO NÃO APROVADO.

## 5. Gates
P0: áudio sem licença, clipping/artefatos, voz enganosa. P1: loop indiferente à história, timbres genéricos repetidos, sons mascarando locução, silêncio acidental, impacto fora do contato, energia plana, efeitos sem intenção, falta de animatic sonoro ou aprovação por métrica apenas. Rubrica 0–5 por intenção/identidade, seleção/timbre, construção de ritmo e contraste, sincronismo, mix/inteligibilidade e acabamento. Alvo editorial 25/30, nenhuma abaixo de 3, sem P0/P1; sem ouvido não avaliar rubrica subjetiva. Entregar mix + stems quando autorizados e relatório. Nenhum score automático certifica taste.

## 6. Fontes profissionais
- Antfood: https://www.antfood.com/work/youtube-sonic-brand e https://www.antfood.com/labs/audio-and-wellness — identidade sonora como sistema e áudio desde a concepção.
- Frame.io: https://workflow.frame.io/guide e https://blog.frame.io/2023/03/16/essential-editing-techniques-for-any-editor/ — diálogo, edição musical, dinâmica e ducking.
- School of Motion: https://schoolofmotion.com/blog/guide-completing-motion-design-project — animatic antes de acabamento.
- A skill claude-motion sound-design foi consultada; preservamos timeline única, cue sheet e stems, rejeitamos sintetizador procedural universal e presets como padrão. Escolha real, curadoria e sound editorial têm precedência.
