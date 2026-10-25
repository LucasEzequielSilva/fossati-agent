import json
import sys
import time
from pathlib import Path

import yt_dlp

ROOT = Path(__file__).resolve().parent.parent
VIDEO_LIST = ROOT / "data" / "video_list.txt"
SUBS_DIR = ROOT / "data" / "subs_raw"
INDEX_PATH = ROOT / "data" / "index.json"
LANGS = ["es", "es-419", "es-ES", "en"]

SUBS_DIR.mkdir(parents=True, exist_ok=True)


def load_video_ids():
    ids = []
    for line in VIDEO_LIST.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        vid = line.split("|", 1)[0].strip()
        ids.append(vid)
    return ids


def load_index():
    if INDEX_PATH.exists():
        return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return {}


def save_index(index):
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ids = load_video_ids()
    index = load_index()

    ydl_opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": LANGS,
        "subtitlesformat": "vtt",
        "outtmpl": str(SUBS_DIR / "%(id)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "sleep_interval": 1,
        "max_sleep_interval": 3,
    }

    total = len(ids)
    for i, vid in enumerate(ids, 1):
        if vid in index and index[vid].get("status") == "ok":
            continue

        url = f"https://www.youtube.com/watch?v={vid}"
        print(f"[{i}/{total}] {vid}", flush=True)

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)

            has_subs = any(SUBS_DIR.glob(f"{vid}.*.vtt"))
            index[vid] = {
                "title": info.get("title"),
                "upload_date": info.get("upload_date"),
                "duration": info.get("duration"),
                "view_count": info.get("view_count"),
                "description": info.get("description"),
                "url": url,
                "status": "ok" if has_subs else "no_subs",
            }
        except Exception as e:
            print(f"  ERROR {vid}: {e}", file=sys.stderr, flush=True)
            index[vid] = {"url": url, "status": "error", "error": str(e)}

        if i % 10 == 0:
            save_index(index)

    save_index(index)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
