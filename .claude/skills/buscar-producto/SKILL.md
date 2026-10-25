---
name: buscar-producto
description: Busca y valida un producto ganador para dropshipping desde Amazon a Argentina. Usalo cuando pidan "buscame un producto", "qué producto vendo", "validá este producto" o cuando haya un nicho/post de referencia y haga falta elegir qué vender. Aplica los criterios de Fossati (vía el agente fossati-dropshipping), calcula el costo puesto con cargos de importación y devuelve base + downsell con puntaje.
---

# Buscar y validar producto ganador (Amazon → Argentina)

Regla de capital: **lo único que se gasta es el testeo de pauta**. No se compran muestras ni stock para elegir; la primera venta real sirve de prueba.

## 1. Criterios: preguntale a Fossati (no de memoria)

Invocá el agente `fossati-dropshipping` con el nicho o producto y pedile: criterios de producto ganador, planilla de 8 criterios, rango de ticket, margen mínimo, qué descarta. Citá sus respuestas con título y fecha. Los criterios que ya salieron del corpus:
- Ticket de más de US$300 al vender (a ~2× el costo puesto), porque debajo de eso los anuncios no cierran.
- Margen neto sano de 25–35% después de ads (10–15% del precio) y pasarela.
- Problema real, demostrable en video, no vendido en Argentina con entrega rápida (competencia en Mercado Libre).
- Calidad con reseñas masivas, no "porquería" (los reclamos tiran la pasarela o la cuenta de Facebook).
- Planilla de 8 puntajes 1–5: precio del proveedor, calidad, stock, tiempo de envío, costo de envío, venta en cantidad, competencia, potencial de upsell/downsell. ≥ 4,2 fuerte; < 3,5 débil.

## 2. Candidatos en Amazon

Con Claude in Chrome (o `curl` con User-Agent de navegador y `Accept-Language: es-AR`), buscá en `amazon.com/s?k=<término>` con dirección de entrega Argentina. Por candidato registrá: ASIN, título, precio USD, rating, cantidad de reseñas, "comprados el mes pasado", si "se envía a Argentina" y la fecha de entrega.

Filtros duros (criterio del estudio, no de Fossati): se envía a Argentina; 4,2★ o más con 300+ reseñas; "comprados el mes pasado" de 100+; vendido y enviado por Amazon; sin marca premium/registrada que no se pueda revender (Normatec, Apple, etc.); sin batería de litio grande ni líquidos (riesgo aduana: verificar en el checkout).

## 3. Costo puesto (obligatorio)

Abrí la página del producto (`/dp/<ASIN>`) con la dirección en Argentina y leé el bloque de envío: **"Cargos estimados de importación"** + precio + envío AmazonGlobal = **total real**. Ejemplo medido: botas QUINEAR US$279,96 (ARS 428.129) + ARS 187.486 de importación = ARS 615.615 (+44%). Extracción por `curl`: buscá `Cargos estimados de importación` en el HTML sin etiquetas.

Precio de venta objetivo = costo puesto × 2 a 2,2 (margen neto 25–30% tras ads y pasarela). Convertí con el tipo de cambio de tu tarjeta USD, no el de Amazon, y sumá colchón por variación del dólar.

## 4. Variantes y datos del listing

`dimensionValuesDisplayData` / `dimensionToAsinMap` dan los ASIN por talle/color; `"hiRes":"https://…"` las fotos; los videos del listing están como `…/default.jobtemplate.mp4.480.mp4`; la caja ("el paquete incluye") y las medidas salen del texto de la ficha; la política de devolución y garantía, de las "opciones de devolución".

## 5. Mercado Libre y competencia

Buscá el mismo producto o similares en Mercado Libre Argentina: precio, vendedores, tiempo de entrega. Si hay entrega rápida y precio parecido, el puntaje de competencia baja. Esto define el precio máximo realista.

## 6. Salida

Tabla con los 3 mejores candidatos: ASIN, USD, costo puesto en ARS, precio sugerido, margen estimado, puntaje de la planilla (8 criterios), riesgos. Recomendá **un producto para anunciar (ticket alto) y un downsell** del mismo nicho, y decí cuál descartás y por qué. Después seguí con el skill `armador-funnels`.

## Trampas conocidas

- El precio en ARS que muestra Amazon es solo conversión; el costo real es USD × tu dólar + importación.
- Dos productos en un mismo pedido llegan por separado (DHL y UPS): no armes bundles de dos compras de Amazon.
- Más de 3 cuotas vuelve los impuestos "impagables" (Fossati).
- Productos de salud: no prometas curas; el copy "ayuda a aliviar la sensación de…" es el techo.
