# Visual arsenal / asset sourcing
Use licensed visual assets as raw material, never as design substitution. Select actual reference for surface, camera, light and composition. [Poly Haven license](https://polyhaven.com/license) CC0 HDRIs/models/PBR; [ambientCG](https://ambientcg.com/) CC0 materials (verify individual assets); [Blender Studio](https://studio.blender.org/) rigs and production assets with asset-specific rights; [Google Fonts](https://fonts.google.com/) and [Fontshare](https://www.fontshare.com/) check individual font licenses; [OpenColorIO](https://opencolorio.org/) for color pipelines. Do not send private product assets to external systems without permission. Record author, URL, license, version, local path, SHA256, usage, and whether preview/master.
 
## Original lookdev recipes (starting points, not validated renders)
| Look | Material | Light/camera | Trade-off |
|---|---|---|---|
| Luxury object | polished/brushed metal, anisotropy, fine roughness, controlled bevel | narrow strip softbox, negative fill, macro 70–100mm equivalent | avoid fake glow and clipped highlights |
| Warm craft | satin ceramic, wood, paper microtexture | large broad key, bounce, low side angle | no heavy grain |
| Scientific precision | translucent resin, enamel, dark matte metal | white rim, clean separation, orthographic for diagram | avoid UI illegibility |
| Sports kinetic | textured rubber, woven fabric, painted surface | harder side key, fast tracking, selective motion blur | avoid constant camera shake |
| Friendly learning | warm paper/clay, soft contrast, tactile shape | broad softbox, controlled contact shadows | preserve character identity |
 
Shot rigs: macro detail→wider context, orbit with target, dolly along rail, parallax truck, top-down arrangement, rack focus, cut-on-action. Block geometry and camera together, then material/lights. Do not promise rig tested without render. Use procedural textures only when appropriate; physically plausible scale; color-managed output. Character assets from product authoritative, no random replacement. Maintain `asset-ledger.json` per project. 
