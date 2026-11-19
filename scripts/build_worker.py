#!/usr/bin/env python3
"""Packs the app into one _worker.js for Cloudflare Pages.

Usage:  python3 scripts/build_worker.py > _worker.js
Deploy: POST /accounts/<ACCOUNT_ID>/pages/projects/uhrzeit-sync/deployments
        multipart fields: manifest={} , branch=main , _worker.js=@_worker.js
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TYPES = {
    "index.html": "text/html; charset=utf-8",
    "manifest.json": "application/manifest+json",
    "icon.svg": "image/svg+xml",
    "sw.js": "text/javascript; charset=utf-8",
}
files = {"/" + n: {"body": (ROOT / n).read_text(encoding="utf-8"), "type": t} for n, t in TYPES.items()}
files["/"] = files["/index.html"]

print("const FILES = " + json.dumps(files) + ";")
print("""export default {
  async fetch(request) {
    const f = FILES[new URL(request.url).pathname];
    if (!f) return new Response('Nicht gefunden', { status: 404 });
    return new Response(f.body, { headers: { 'content-type': f.type, 'cache-control': 'no-cache' } });
  }
};""")
