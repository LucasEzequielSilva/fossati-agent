# Playbook operativo: dropshipping Amazon → Argentina (criterio del estudio)

Esto NO es Fossati: es el flujo que el estudio probó armando funnels (alimentador Petlibro, botas de compresión Elevate Goods). Lo que sí es de Fossati vive en `docs/fossati-ads.md` y `docs/fossati-tienda-funnel.md`, con cita de video.

## Modelo de negocio

1. Tienda Shopify con una página de producto tipo landing (los funnels de este repo).
2. El cliente paga en pesos (Mercado Pago, transferencia). La plata debe llegar al instante.
3. Recién ahí se compra en Amazon.com con tarjeta USD (Dólar App), con la dirección del cliente. El despacho es manual al principio y se automatiza después.
4. Amazon envía por AmazonGlobal y cobra "cargos de importación" en su checkout. Si queda así, el cliente no paga nada al recibir (confirmar con un primer pedido real).
5. **Capital:** el único gasto propio es el testeo de pauta del producto. Cada compra se hace con la plata del cliente que ya pagó, así que no hay stock ni muestras previas. El primer pedido real hace de prueba de envío.

## Costos reales (ejemplo medido el 2026-10-25)

| | Precio Amazon | Importación | Total |
|---|---|---|---|
| Botas QUINEAR 4 cámaras | ARS 428.129 (US$279,96) | ARS 187.486 | ARS 615.615 |
| CINCOM con calor | ARS 152.910 (US$99,99) | ARS 80.087 | ARS 232.997 |

Importación ≈ +44% a +52% sobre la lista. El ARS de Amazon es una conversión: el costo real es USD × el dólar de tu tarjeta + importación. Precio de venta ≈ 2 a 2,2× costo puesto. Dejá colchón por si el dólar sube entre el pago del cliente y la compra.

## Extracción de datos de Amazon

- Búsqueda: `amazon.com/s?k=…` con dirección en Argentina.
- Página: `curl -s -L -A "Mozilla/5.0 … Chrome/130" -H "Accept-Language: es-AR,es;q=0.9" https://www.amazon.com/dp/<ASIN>?th=1&psc=1`.
- Qué sacar: título (`id="productTitle"`), bullets (`id="feature-bullets"`), `dimensionToAsinMap` + `dimensionValuesDisplayData` (talle/color por ASIN), `"hiRes":"…"` (fotos), `…mp4.480.mp4` (videos), "Cargos estimados de importación", "el paquete incluye", medidas, política de devolución.
- Fotos: contact sheet con Pillow antes de elegir. Videos: `ffmpeg` recorte 9:16, sin audio.
- Python en Windows: `PYTHONIOENCODING=utf-8` para no romper con tildes.

## Verificación en Chrome

Servir local, probar con `javascript_tool` (clicks y lecturas del DOM), medir overflow con un iframe de 360/375 px, mirar consola. El mismo problema aparece siempre: un hijo de `grid` con scroll horizontal necesita `min-w-0`.

## Vista previa y publicación

- Vista previa: Vercel (`vercel deploy --prod --yes --scope <team>`), `noindex`, `.vercelignore` con README, docs y notas de costos.
- Para vender: Shopify. Opción 1: plantilla de página sin tema (`{% layout none %}`) con el HTML pegado y los assets en Archivos. Opción 2: Vercel con dominio propio y el botón apuntando a un link de carrito de Shopify (`/cart/<variante>:1`), porque `fetch('/cart/add.js')` entre dominios lo bloquea CORS.
- Medio de pago: conectar Mercado Pago y configurar acreditación inmediata. Verificar qué pasarela habilita Shopify en la cuenta.
- DNI/CUIL obligatorio en el checkout si Amazon lo pide para la aduana.

## Postventa

- Mensajes: pago confirmado → comprado y en camino (con tracking) → llega en X días → llegó, cómo usarlo.
- Amazon: devolución a 30 días con reintegro o reemplazo, pero "no elegible para devoluciones gratuitas" desde Argentina. Reservá 5–10% de costo para cambios y fallas y no prometas más de lo que podés hacer.
- Garantía del fabricante: en inglés y sin servicio local; la garantía de la tienda es propia y corta.
- Dos compras de Amazon llegan por separado: evitá bundles de dos productos.

## Riesgos conocidos

- Margen fino y exposición al dólar.
- Fotos y videos del listing con logo de terceros: sirven para maqueta, no para vender.
- Claims de salud en Meta: lenguaje de bienestar, sin promesas de cura.
- Políticas de Amazon sobre envíos a terceros.
- Productos eléctricos: voltaje y ficha (220 V / tipo I) sin confirmar en el listing: probar con un pedido real.

## Cómo se usa el repo

1. `buscar-producto` → producto base + downsell, con costo puesto.
2. `armador-funnels` → funnel desde la plantilla, verificado.
3. `fossati-juez` → veredicto antes de lanzar.
4. `docs/fossati-ads.md` → plan de testeo de pauta (único gasto).

## Despacho cuando entra el pago (≈10 minutos por pedido)

Se despacha apenas Mercado Pago acredita. La tarea propia es cargar el pedido en Amazon; el envío real lo hace Amazon/AmazonGlobal directo desde EE. UU. a la puerta del cliente (el paquete nunca pasa por nosotros).

1. **Shopify avisa el pedido pagado** con: nombre completo, DNI/CUIL, teléfono, dirección completa (calle, número, piso/depto, localidad, provincia, código postal) y la variante (talle).
2. **En Amazon:** agregar como dirección de entrega *la que llenó el cliente* (no la nuestra). Elegir el ASIN del talle correcto, revisar el "total" con cargos de importación y pagar con la tarjeta USD. Opciones de regalo para que no lleve el precio.
3. **Registrar:** copiar número de pedido y tracking en la orden de Shopify.
4. **Avisarle al cliente por WhatsApp:** "pedido en camino" con el tracking y la fecha estimada.
5. **Convertir el dólar el mismo día:** el riesgo es el tipo de cambio entre el cobro y la compra.

Para que alcance con 10 minutos, el checkout de Shopify tiene que exigir **DNI/CUIL, teléfono y dirección completa con código postal**: son los datos que piden Amazon y el courier. Tiempo de envío después de la compra: ~10 días hasta la puerta (Amazon marcó 4–5 de noviembre al 25 de octubre).
