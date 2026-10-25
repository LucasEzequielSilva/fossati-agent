import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBS_DIR = ROOT / "data" / "subs_raw"
OUT_DIR = ROOT / "data" / "transcripts"
INDEX_PATH = ROOT / "data" / "index.json"

LANG_PRIORITY = ["es", "es-419", "es-ES", "en"]

TAG_RE = re.compile(r"<[^>]+>")
TIMESTAMP_LINE_RE = re.compile(r"^\d{2}:\d{2}:\d{2}[.,]\d{3}\s*-->")


def pick_vtt_for(vid):
    candidates = {p.stem.split(".")[-1]: p for p in SUBS_DIR.glob(f"{vid}.*.vtt")}
    for lang in LANG_PRIORITY:
        if lang in candidates:
            return candidates[lang]
    return next(iter(candidates.values()), None)


def vtt_to_lines(path):
    raw = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    lines = []
    for line in raw:
        line = line.strip()
        if not line or line == "WEBVTT":
            continue
        if line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if TIMESTAMP_LINE_RE.match(line):
            continue
        if line.isdigit():
            continue
        line = TAG_RE.sub("", line).strip()
        line = html.unescape(line)
        if line:
            lines.append(line)

    deduped = []
    for line in lines:
        if not deduped or deduped[-1] != line:
            deduped.append(line)
    return deduped


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8")) if INDEX_PATH.exists() else {}

    vids = sorted({p.name.split(".")[0] for p in SUBS_DIR.glob("*.vtt")})
    ok, skipped = 0, 0

    for vid in vids:
        vtt_path = pick_vtt_for(vid)
        if not vtt_path:
            skipped += 1
            continue

        lines = vtt_to_lines(vtt_path)
        if not lines:
            skipped += 1
            continue

        meta = index.get(vid, {})
        header = (
            f"TITLE: {meta.get('title', '')}\n"
            f"UPLOAD_DATE: {meta.get('upload_date', '')}\n"
            f"URL: {meta.get('url', 'https://www.youtube.com/watch?v=' + vid)}\n"
            f"---\n"
        )
        text = header + "\n".join(lines)
        (OUT_DIR / f"{vid}.txt").write_text(text, encoding="utf-8")
        ok += 1

    print(f"Transcripts written: {ok}, skipped (no usable subs): {skipped}")


if __name__ == "__main__":
    main()
