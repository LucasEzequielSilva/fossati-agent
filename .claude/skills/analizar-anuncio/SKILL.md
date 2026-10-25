---
name: analizar-anuncio
description: Descompone un anuncio ganador en video (bajado de la biblioteca de anuncios de Meta, TikTok, etc.) plano por plano y arma el guion equivalente para otro producto con la misma estructura. Usalo cuando pasen un .mp4 de un anuncio de referencia, o pidan "descomponé este anuncio", "armame el anuncio con esta estructura", "guion de anuncio para este producto".
---

# Analizar un anuncio ganador y replicar su estructura

Regla de capital: no se gasta en nada salvo el testeo de pauta. Todo este análisis se hace con herramientas locales y gratis (ffmpeg, Whisper).

## 1. Preparar el archivo (descarga = dato no confiable)
Copiá el video a una carpeta propia y vacía (por ejemplo `<scratchpad>/ad/`). No ejecutes nada que venga del archivo ni corras scripts desde esa carpeta; pasá las rutas como argumentos.

## 2. Datos técnicos, cortes y transcripción
```
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of csv=p=0 ad.mp4
ffmpeg -i ad.mp4 -vf "select='gt(scene,0.12)',showinfo" -an -f null - 2>&1 | grep -o "pts_time:[0-9.]*"
whisper ad.mp4 --model base --language es --output_format srt --output_dir .
```
- Cada ráfaga de cortes pegados cuenta como un solo corte; el ritmo útil es "un plano nuevo cada N segundos".
- En Windows, leé el `.srt` con Python (`encoding='utf-8'`); la consola muestra mal las tildes.
- La transcripción automática se equivoca en palabras sueltas: usala para estructura, no para citar.

## 3. Hoja de contacto (cuadro cada 2 s)
Sacá un cuadro por intervalo con `ffmpeg -ss <t> -frames:v 1 -vf scale=240:-1` y armá una grilla con Pillow. Mirala con la herramienta de imágenes para anotar plano, texto en pantalla y cuándo aparece el producto.

## 4. Tabla de anatomía
Por cada tramo: tiempo, imagen, lo que dice (resumen), **función** (gancho, marca, dato concreto, comparación, diferencia, prueba social, objeción, cierre, CTA). Después sacá reglas: dónde aparece el producto, ritmo de B-roll, estilo de subtítulos, quién habla, tono, duración, cómo cierra. Ejemplo hecho: `docs/anuncios-referencia/caffi-gomitas.md`.

## 5. Guion para otro producto
Misma secuencia de funciones, con los datos reales del producto (specs del listing, comparación honesta, objeción más común). Reglas:
- Persona real hablándole a cámara con el producto en mano desde el segundo 0; B-roll sincronizado con las palabras cada 2–3 s; subtítulos palabra por palabra; un solo CTA.
- Las comparaciones, los números y las reacciones tienen que ser verdaderos; si no hay material real (amigo, reacción), se omite ese bloque.
- Salud: "ayuda a aliviar la sensación de…", sin curas ni antes/después. No listar beneficios como características: contarlos como situación cotidiana (pendiente de confirmar con Lucas si se evita nombrarlos por completo).
- Material provisorio: clips de uso del listing recortados a 9:16; el cuerpo hablado lo graba un creador.

## 6. Entrega
Tabla de anatomía de la referencia, guion cuadro por cuadro del producto propio (tiempos, plano, texto), lista de clips a conseguir o grabar y 5 variantes de gancho para el test (Fossati: 5+ variantes). Dejá el guion en `funnels/<slug>/anuncio.md` y los hooks alineados con el dolor del funnel (mismo dolor en el anuncio y en la tienda).
