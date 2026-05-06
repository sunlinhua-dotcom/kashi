#!/usr/bin/env python3
"""Batch-generate 32 images via apiyi.com (gpt-image-2-all) with concurrency."""
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

API_URL = os.environ.get("IMAGE_API_URL", "https://api.apiyi.com/v1/images/generations")
API_KEY = os.environ.get("IMAGE_API_KEY", "")
MODEL = os.environ.get("IMAGE_MODEL", "gpt-image-2-all")
if not API_KEY:
    raise SystemExit("Set IMAGE_API_KEY environment variable")

PROMPTS_FILE = "/Volumes/ProjectEXF/kashi/output/image_prompts.json"
OUTPUT_DIR = "/Volumes/ProjectEXF/kashi/output/images"
LOG_FILE = "/Volumes/ProjectEXF/kashi/output/images/_generation_log.json"

CONCURRENCY = 4
RETRIES = 3
RETRY_BACKOFF = (10, 25, 60)


def generate(item: dict) -> tuple[str, bool, str]:
    """Generate one image. Returns (filename, success, message)."""
    fname = item["filename"]
    out_path = os.path.join(OUTPUT_DIR, fname)
    if os.path.exists(out_path) and os.path.getsize(out_path) > 100_000:
        return fname, True, "SKIP (already exists)"

    body = {
        "model": MODEL,
        "prompt": item["prompt"],
        "n": 1,
        "size": item["size"],
    }
    data = json.dumps(body).encode("utf-8")

    for attempt in range(RETRIES):
        try:
            req = urllib.request.Request(
                API_URL,
                data=data,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=300) as resp:
                payload = json.loads(resp.read())

            if "data" not in payload or not payload["data"]:
                raise ValueError(f"No data in response: {payload}")

            obj = payload["data"][0]
            if "b64_json" in obj:
                img_bytes = base64.b64decode(obj["b64_json"])
            elif "url" in obj:
                with urllib.request.urlopen(obj["url"], timeout=120) as r:
                    img_bytes = r.read()
            else:
                raise ValueError(f"No image in response: {list(obj.keys())}")

            with open(out_path, "wb") as f:
                f.write(img_bytes)
            return fname, True, f"OK ({len(img_bytes)//1024} KB)"

        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", errors="ignore")[:300]
            if attempt < RETRIES - 1:
                time.sleep(RETRY_BACKOFF[attempt])
                continue
            return fname, False, f"HTTP {e.code}: {err}"
        except Exception as e:
            if attempt < RETRIES - 1:
                time.sleep(RETRY_BACKOFF[attempt])
                continue
            return fname, False, f"{type(e).__name__}: {e}"


def main():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    with open(PROMPTS_FILE) as f:
        manifest = json.load(f)
    items = manifest["images"]
    total = len(items)
    print(f"📦 {total} images to generate", file=sys.stderr)

    results = []
    start = time.time()
    with ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
        futures = {pool.submit(generate, it): it for it in items}
        done_count = 0
        for fut in as_completed(futures):
            it = futures[fut]
            fname, ok, msg = fut.result()
            done_count += 1
            elapsed = time.time() - start
            status = "✅" if ok else "❌"
            print(f"[{done_count}/{total}] {status} {it['id']} {fname} — {msg} (t+{elapsed:.0f}s)",
                  file=sys.stderr)
            results.append({"id": it["id"], "filename": fname, "success": ok, "message": msg})

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump({"results": results, "duration_s": time.time() - start}, f, ensure_ascii=False, indent=2)

    ok_count = sum(1 for r in results if r["success"])
    print(f"\n📊 SUMMARY: {ok_count}/{total} succeeded in {time.time()-start:.0f}s", file=sys.stderr)
    if ok_count < total:
        print("Failures:", file=sys.stderr)
        for r in results:
            if not r["success"]:
                print(f"  - {r['id']}: {r['message']}", file=sys.stderr)


if __name__ == "__main__":
    main()
