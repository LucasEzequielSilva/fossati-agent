# Plantilla de funnel de producto

`index.html` es un funnel completo de una sola página (Tailwind CDN 3.4.17 + Inter), con branding Elevate (fondo `#0D0D0D`, naranja `#FF4D00`). Todo el contenido está en el objeto `P` del final del archivo.

## Qué editar en `P`

| Clave | Qué es |
|---|---|
| `brand`, `sample_mode` | Nombre de tienda; `true` muestra carteles de "ejemplo" y de maqueta (poner `false` al publicar) |
| `delivery_days`, `returns_days`, `warranty`, `customs_answer`, `pay_answer`, `power_answer` | Textos que tienen que ser ciertos (marcados CONFIRMAR) |
| `models[]` | Primero el que se anuncia (se preselecciona) y después el downsell. Cada uno: `name`, `sub`, `price`, `badge`, `proof`, `lead`, `img`, `sizes[]` (con `variant` de Shopify), `checks`, `gallery`, `specs`, `box`, `boxNote` |
| `videos[]` | Clips verticales 9:16 sin sonido con póster. Ponelos en `assets/video/` |
| `stats`, `sizeTable`, `compare`, `reviews`, `faq`, `announce`, `guarantees`, `pays`, `footLinks` | Contenido de cada sección |
| `addons` | Extras con variante propia. Vacío por defecto (cada producto de Amazon llega separado) |

## Para otra marca
Cambiá los tokens en `tailwind.config` y en el bloque `<style>`, el logo (`LOGO`, SVG) y la fuente. La estructura no se toca.

## Antes de publicar
Reemplazar `VARIANT_ID_*`, precios, reseñas y fotos/videos de ejemplo; confirmar envío, impuestos, garantía y voltaje; `sample_mode: false`; correr el agente `fossati-juez`.
