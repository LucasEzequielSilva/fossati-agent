# fossati-agent

Agente especialista de Claude Code entrenado sobre el corpus completo del canal de YouTube
de **Luis Fossati** (@Luisfossatidrop) — 248 videos sobre dropshipping/ecommerce.

## Qué incluye

- `data/transcripts/` — 248 transcripciones completas en texto plano (producto final, lo que
  usa el agente).
- `data/index.json` — metadata de cada video (título, fecha, duración, url).
- `data/video_list.txt` — listado crudo de videos del canal.
- `scripts/` — pipeline usado para generar el corpus (`fetch_transcripts.py`,
  `fix_index.py`, `vtt_to_text.py`), por si hace falta actualizarlo con videos nuevos.
- `.claude/agents/fossati-dropshipping.md` — la definición del subagente.

## Cómo usarlo

1. Cloná este repo.
2. Abrí Claude Code con esta carpeta como working directory.
3. El agente `fossati-dropshipping` queda disponible automáticamente (es un agente
   project-scoped, no hace falta instalar nada global). Invocalo desde el Agent tool o
   pedile a Claude que lo use.

## Actualizar el corpus con videos nuevos

```
python scripts/fetch_transcripts.py   # descarga subs de videos nuevos (salta los que ya están "ok")
python scripts/vtt_to_text.py         # regenera data/transcripts/*.txt
```

Requiere `yt-dlp` instalado (`pip install yt-dlp`).
