# Botas de compresión · funnel de recuperación (Argentina, ARS, checkout Shopify)

Maqueta de un solo archivo (`index.html`, Tailwind CDN + DM Sans/Fraunces) para pegar en Shopify. Todo lo editable vive en el objeto `P` al final del archivo. Inspirado en el post de @elevategoods.co (botas de compresión para recuperación muscular); las fotos NO son de esa cuenta.

```
index.html   ← funnel en español (AR): Pro (pierna completa, 3 talles) + Esencial (con calor, pie y pantorrilla)
assets/      ← fotos de Amazon (pro-*, esencial-*)
docs/ads.md  ← hooks, ángulos y plan de test
```

## Productos (fuente: Amazon.com, 2026-10-25)

Criterio: lo elegí con el agente de Fossati (anunciar el de ticket alto, tener el barato de downsell). Detalle en `docs/ads.md`.

| | Pro (se anuncia) | Esencial (downsell) |
|---|---|---|
| Qué es | QUINEAR 4 cámaras, pierna completa, sensor de presión, 8 intensidades (50–120 mmHg), sin calor, QN-071A | CINCOM con calor, pie y pantorrilla, 3 intensidades, CM-030A |
| ASIN | `B0BNPTG2KR` (S) · `B09LCTXQB3` (M) · `B0BNPV82C5` (L) | `B08CXN8QF2` |
| Precio Amazon | US$279,96 (ARS 428.129) | US$99,99 (ARS 152.910) |
| **Cargos de importación a Argentina** | **ARS 187.486** | **ARS 80.087** |
| **Total que paga Amazon** | **ARS 615.615** | **ARS 232.997** |
| Reseñas | 4,4★ · 1.852 | 4,3★ · 4.714 |

Los ARS son la conversión de Amazon. Tu costo real = USD con Dólar App × tu tipo de cambio + los cargos de importación (el checkout de Amazon los muestra al elegir dirección argentina).

Precios de ejemplo en el funnel: Pro $1.299.000 y Esencial $489.000 (≈ 2,1× el costo puesto: criterio del estudio; Fossati habla de vender al doble o más del precio de Amazon y de 25–35% de margen neto como "excelente"). **Los ponés vos**, y antes mirá qué cuestan en Mercado Libre.

## Ver local

```
cd D:\Dev\recovery-funnel
python -m http.server 8773        # http://127.0.0.1:8773/index.html
```

Mientras los `variant` empiecen con `VARIANT_ID`, el botón solo muestra un aviso de "Maqueta". Sin talle elegido, el botón pide elegirlo (en Pro).

## Cómo cierra

"Agregar al carrito" → `POST /cart/add.js` con `{items:[variante del talle, extras]}` → `/checkout`. Eventos de píxel: `ViewContent`, `AddToCart`, `InitiateCheckout` (moneda `ARS`). Flujo operativo: el cliente paga en pesos → cuando se acredita comprás en Amazon con Dólar App y enviás al domicilio.

Variantes a crear en Shopify: Pro S/M/L (`VARIANT_ID_PRO_S|M|L`) y Esencial (`VARIANT_ID_ESENCIAL`). `addons: []` queda vacío a propósito: un segundo producto de Amazon llega por separado.

## Antes de publicar (checklist)

1. **Voltaje y enchufe (lo primero):** el listing no dice nada. El adaptador viene del mercado de EE. UU.; confirmá que sirve en 220 V/50 Hz y qué ficha trae. `power_answer` dice que llega "listo para enchufar": tiene que ser cierto. Hacé un envío de prueba.
2. **Cargos de importación:** Amazon suma ~44% (Pro) y ~52% (Esencial) sobre el precio de lista. Tu costo es el total, no el precio de góndola. Con DNI/CUIL en el checkout si Amazon lo pide (Fossati: ponelo obligatorio en Shopify) y confirmá que el cliente no paga nada al recibir (`customs_answer`).
3. **Precios y margen:** poné el precio con costo puesto × ~2, más colchón por dólar. Fossati: más de 3 cuotas y los impuestos se vuelven "impagables".
4. **`VARIANT_ID_*`** reales y `sample_mode: false`.
5. **Talles:** la tabla viene del listing de Amazon (S 1,55–1,75 m, M 1,78–1,88 m, L 1,91–1,98 m, en cm convertidos de pulgadas). La mayoría de la gente en Argentina es S.
6. **Salud:** el copy usa "ayuda a aliviar la sensación de piernas cansadas", no promete curar nada. Dejá los avisos de consultar al médico. Cuidado con Meta/ANMAT: no digas "terapia", "venas varicosas", "tratamiento".
7. **Caja y manual:** la caja del Pro viene del listing (2 botas, controlador, manguera, adaptador, manual, bolsa). El idioma del manual y la caja del Esencial no están confirmados.
8. **Entrega y garantía:** `delivery_days [10,15]` (Amazon marcó ~10 días), `returns_days`, `warranty` (3 meses es de ejemplo; los 24 meses que menciona Amazon son del fabricante, no tuyos).
9. **Opiniones:** son de ejemplo (cartel amarillo). No uses las estrellas de Amazon como tuyas.
10. **Fotos:** son de Amazon y se ve el logo QUINEAR/CINCOM en las botas. Sirven para la maqueta; para vender, fotos y videos propios o con permiso (un alumno de Fossati perdió su tienda por denuncias de Adidas al vender réplicas: con productos originales el riesgo es menor, pero los logos de terceros siguen siendo criterio de cuidado del estudio).

## Riesgos de dropshipping desde Amazon

- **Margen fino:** con cargos de importación el costo puesto sube ~44–52%. Sin el número real no sabés cuánto gastar en ads.
- **Dólar:** si sube entre el pago del cliente y tu compra, perdés margen.
- **Políticas de Amazon:** envío a terceros, sin factura ni precio visibles; riesgo de cuenta limitada.
- **Producto de ticket alto en LATAM:** el primer test de Pablo (Fossati) a US$1.300 no vendió; después bajó a la mitad y explotó. Tu Pro queda en ~US$850 al tipo de cambio de Amazon: probá y mirá el CPA.
