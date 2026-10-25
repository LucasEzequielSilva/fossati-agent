import json
from pathlib import Path

import yt_dlp

ROOT = Path(__file__).resolve().parent.parent
VIDEO_LIST = ROOT / "data" / "video_list.txt"
SUBS_DIR = ROOT / "data" / "subs_raw"
INDEX_PATH = ROOT / "data" / "index.json"


def load_video_ids():
    ids = []
    for line in VIDEO_LIST.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.strip():
            ids.append(line.split("|", 1)[0].strip())
    return ids


def main():
    ids = load_video_ids()
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8")) if INDEX_PATH.exists() else {}

    ydl_opts = {"skip_download": True, "quiet": True, "no_warnings": True}

    for i, vid in enumerate(ids, 1):
        has_vtt = any(SUBS_DIR.glob(f"{vid}.*.vtt"))
        if index.get(vid, {}).get("status") == "ok" and index[vid].get("title"):
            continue

        url = f"https://www.youtube.com/watch?v={vid}"
        print(f"[{i}/{len(ids)}] {vid}", flush=True)
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
            index[vid] = {
                "title": info.get("title"),
                "upload_date": info.get("upload_date"),
                "duration": info.get("duration"),
                "view_count": info.get("view_count"),
                "description": info.get("description"),
                "url": url,
                "status": "ok" if has_vtt else "no_subs",
            }
        except Exception as e:
            index[vid] = {"url": url, "status": "error", "error": str(e)}

        if i % 20 == 0:
            INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")

    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print("DONE")


if __name__ == "__main__":
    main()
