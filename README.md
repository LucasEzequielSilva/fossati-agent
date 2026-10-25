# fossati-agent · experto en dropshipping, buscador de producto y armador de funnels

Todo lo que enseña **Luis Fossati** (@Luisfossatidrop, 248 videos transcriptos) más las herramientas del estudio para **buscar un producto ganador en Amazon y armar el funnel premium** (página de producto + checkout Shopify) para vender en Argentina.

## Qué hay adentro

| Pieza | Para qué |
|---|---|
| `.claude/agents/fossati-dropshipping.md` | Experto: responde con lo que dice Fossati, citando video y fecha. No inventa |
| `.claude/agents/fossati-juez.md` | **Juez**: evalúa 12 partes del funnel como lo haría Fossati, puntúa 1–5 y da el veredicto ("listo, ya estás hecho" o qué arreglar) |
| `.claude/skills/buscar-producto/` | Busca candidatos en Amazon, calcula costo puesto con cargos de importación, puntúa con la planilla de 8 criterios y propone base + downsell |
| `.claude/skills/armador-funnels/` | Arma el funnel de punta a punta: datos, fotos y videos, página, verificación en Chrome, juicio y link de Vercel |
| `.claude/skills/analizar-anuncio/` | Descompone un anuncio ganador (.mp4 de la biblioteca de anuncios) plano por plano y arma el guion equivalente para tu producto |
| `templates/funnel-producto/` | Plantilla del funnel (editás solo el objeto `P`) |
| `ejemplos/botas-compresion/` | Funnel real de referencia (Elevate Goods, botas de compresión) con assets |
| `docs/anuncios-referencia/` | Anuncios ganadores ya descompuestos (Caffi) y su adaptación a las botas |
| `docs/fossati-ads.md` | Todo lo que sabe Fossati de ads, con citas |
| `docs/fossati-tienda-funnel.md` | Producto, tienda/funnel, oferta, precios y postventa según Fossati, con citas |
| `docs/PLAYBOOK.md` | Flujo operativo del estudio (costos, extracción de Amazon, publicación, postventa, riesgos) |
| `data/` | Corpus: transcripciones (`transcripts/`) e índice (`index.json`) |

## Regla de capital
Lo único que se gasta es el **testeo de pauta del producto**. La compra en Amazon sale de la plata del cliente que ya pagó.

## Cómo usarlo (Claude Code)

1. Cloná el repo y abrí Claude Code en esta carpeta (los agentes y skills quedan activos solos, no se instala nada global).
2. Pedí, por ejemplo:
   - "Buscame un producto ganador de [nicho]" → `buscar-producto`.
   - "Armame el funnel de este producto: [link de Amazon]" → `armador-funnels` (incluye el juez).
   - "Descomponé este anuncio y armame el guion para mi producto" (con un .mp4) → `analizar-anuncio`.
   - "Juzgá este funnel" → `fossati-juez`.
   - "¿Qué dice Fossati de [tema]?" → `fossati-dropshipping`.
3. Opcional para el armado completo: extensión Claude in Chrome (ver Amazon y verificar la página), `ffmpeg` (recortar videos), CLI de `vercel` (link de vista previa), Python 3 con Pillow.

Los agentes leen `data/` con rutas relativas a esta carpeta.

## Actualizar el corpus
```
python scripts/fetch_transcripts.py   # descarga subs de videos nuevos
python scripts/vtt_to_text.py         # regenera data/transcripts/*.txt
```
Requiere `yt-dlp` (`pip install yt-dlp`).
