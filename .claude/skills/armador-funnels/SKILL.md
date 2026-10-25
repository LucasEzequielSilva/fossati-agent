---
name: armador-funnels
description: Arma un funnel de producto ganador premium (página de producto + checkout Shopify) para dropshipping desde Amazon a Argentina, de punta a punta - elegir producto, sacar datos y fotos/videos de Amazon, construir la página desde la plantilla, verificarla en el navegador, hacerla juzgar por fossati-juez y desplegar un link de vista previa. Usalo cuando pidan "armame un funnel", "funnel ganador", "armá la página de este producto" o pasen un link/post/nicho para vender.
---

# Armador de funnels de producto ganador

Salida: una página de un solo archivo (`index.html`, Tailwind CDN, config en el objeto `P`) lista para pegar en Shopify, con link de vista previa en Vercel. Modelo de referencia: `ejemplos/botas-compresion/` (funnel completo, branding Elevate oscuro). Plantilla vacía: `templates/funnel-producto/`.

## Reglas del estudio

1. **Capital:** lo único que se gasta es el testeo de pauta del producto. Nada de stock, muestras ni herramientas pagas. La compra en Amazon sale de la plata del cliente cuando ya pagó.
2. **Una sola oferta en el anuncio:** el producto de ticket alto (> US$300 a ~2× costo puesto). Lo barato queda como downsell en la tienda, sin anuncios.
3. **Nada inventado:** specs, cajas, talles y claims salen del listing; lo que no se confirma queda marcado como "CONFIRMAR". Reseñas y precios son de ejemplo (`sample_mode: true`) hasta que Lucas los cambie.
4. **Salud:** "ayuda a aliviar la sensación de…", nunca "cura/trata". Sin "antes y después" ni claims médicos.
5. **Video siempre:** Fossati insiste en que sin video no se vende. Si no hay videos propios, usar los clips de uso del listing de Amazon recortados a 9:16 y avisar que son provisorios.

## Pasos

### 1. Producto
Si no hay producto definido, corré el skill `buscar-producto`. Si ya hay link de Amazon, validá igual el costo puesto (con cargos de importación) y el margen. Si el post/nicho viene de Instagram, abrilo en Chrome (carrusel y perfil) para entender el ángulo.

### 2. Datos y assets
- Página `/dp/<ASIN>` con `curl -s -L -A "<UA de Chrome>" -H "Accept-Language: es-AR,es;q=0.9"`; ASIN por talle/color, bullets, caja, medidas, fotos `hiRes`, devolución/garantía.
- Videos: `…/default.jobtemplate.mp4.480.mp4` del HTML. Usá `ffmpeg` para recortar clips de 7–10 s a 9:16 (`-vf "crop=270:480:292:0,fps=24" -an -c:v libx264 -crf 28 -movflags +faststart`) y un póster `.jpg` por clip. Evitá los que traen marca de agua de Amazon.
- Fotos y videos en `funnels/<slug>/assets/`. Chequeá las fotos con una hoja de contacto antes de elegirlas.
- Si hay un dashboard o sitio de marca (por ejemplo `https://elevatefit.tech/dashboard`), extraé tokens: variables CSS (`--background`, `--primary`, fuente) y el SVG del logo con `javascript_tool`.

### 3. Construcción
Copiá `templates/funnel-producto/index.html` a `funnels/<slug>/index.html` y editá solo el objeto `P` y los textos de copy:
- Modelo anunciado primero en `P.models` (se preselecciona); downsell segundo.
- `sizes[]` con `variant: 'VARIANT_ID_*'` (placeholders hasta tener Shopify); el botón obliga a elegir talle si hay más de uno.
- Prueba social: reseñas de ejemplo marcadas; la fila de "opiniones en Amazon" solo con números reales atribuidos.
- Precio sugerido = costo puesto × 2–2,2 (`price`), el "equivale a $X por día" se calcula solo.
- Secciones: hero + checks + oferta + talle + "cómo llega tu pedido" · números · **videos de uso** · dolores · features con foto · pasos · talles · comparativa · "¿es para vos?" · opiniones · ficha · FAQ · cierre · footer legal · barra sticky mobile.
- Branding: tokens en el `<script>` de Tailwind y en el bloque `<style>` (fondo `#0D0D0D`, naranja `#FF4D00`, Inter). Cambiar tokens para otra marca; no tocar la estructura.

### 4. Verificación en el navegador (obligatoria)
`python -m http.server <puerto>` en la carpeta y Chrome:
- Totales por modelo y talle; botón sin talle; toast "Maqueta".
- Sin imágenes ni videos rotos; los videos reproducen.
- Sin desborde horizontal en 360 y 375 px: abrí la página dentro de un `<iframe>` de ese ancho y medí `scrollWidth`. Lección: un hijo de grid con tabla o fila con scroll necesita `min-w-0`.
- Capturas de hero, comparativa, talles y FAQ.

### 5. Juicio de Fossati (obligatorio antes de entregar)
Invocá el agente `fossati-juez` con la ruta del funnel, el costo puesto y el precio. Iterá los arreglos hasta que dé "Listo, flaquito, ya estás hecho" o explicá por qué quedan bloqueantes que dependen de Lucas (precios reales, reseñas, variantes).

### 6. Vista previa
Con `.vercelignore` (excluir `README.md`, `docs`, notas de costos) y `<meta name="robots" content="noindex">`:
`vercel link --yes --project <slug> --scope <team>` y `vercel deploy --prod --yes --scope <team>`. Verificá 200 en la página y en un video. Nunca publiques márgenes ni costos.

### 7. Entrega y checklist
Entregá: link, qué falta de su lado y los riesgos (cargos de importación, voltaje/enchufe si es eléctrico, DNI/CUIL, marca en fotos, claims de salud). Para vender: página en Shopify (plantilla `page.funnel.liquid` con `{% layout none %}`, assets subidos a Archivos) o Vercel con dominio propio y links de carrito en lugar de `/cart/add.js` (el fetch cruzado de dominio lo bloquea Shopify).

### 8. Pauta
Con `docs/fossati-ads.md` y el skill `analizar-anuncio` (estructura: persona hablándole a cámara con el producto en mano + B-roll cada 2–3 s, ver `docs/anuncios-referencia/`): un subnicho y un mensaje; presupuesto de test ≈ 20% del precio repartido en 5+ variantes; validar en orgánico primero; métricas y reglas de apagado/escalado del playbook.

## Qué NO hacer
- No cargar precios, reseñas ni fechas como reales.
- No prometer envío/impuestos/garantía que no estén confirmados.
- No publicar costos ni notas internas.
- No gastar en nada que no sea el testeo de pauta.
