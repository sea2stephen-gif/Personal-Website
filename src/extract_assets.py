#!/usr/bin/env python3
"""One-time extraction of binary assets (fonts, JS) from the bundled HTML
into real files under src/assets/, rewriting UUID references in
src/head.html and src/styles.css to real relative paths."""
from pathlib import Path
import re
import json
import base64
import gzip

BUNDLE = Path('Stephen To - Portfolio.html')
HEAD = Path('src/head.html')
CSS = Path('src/styles.css')
OUT_DIR = Path('src/assets')

MIME_EXT = {
    'font/woff2': 'woff2',
    'text/javascript': 'js',
}


def extract_assets():
    content = BUNDLE.read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'<script type="__bundler/manifest">(.*?)</script>', content, re.S)
    if not m:
        raise ValueError('Could not find bundler manifest')
    manifest = json.loads(m.group(1))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    uuid_to_path = {}

    for uuid, entry in manifest.items():
        ext = MIME_EXT.get(entry['mime'])
        if not ext:
            print(f'Skipping unknown mime {entry["mime"]} for {uuid}')
            continue
        raw = base64.b64decode(entry['data'])
        if entry.get('compressed'):
            raw = gzip.decompress(raw)
        out_path = OUT_DIR / f'{uuid}.{ext}'
        out_path.write_bytes(raw)
        uuid_to_path[uuid] = f'assets/{uuid}.{ext}'
        print(f'Wrote {out_path} ({len(raw)} bytes)')

    for target in (HEAD, CSS):
        text = target.read_text(encoding='utf-8')
        for uuid, rel_path in uuid_to_path.items():
            text = text.replace(uuid, rel_path)
        target.write_text(text, encoding='utf-8')
        print(f'Rewrote references in {target}')


if __name__ == '__main__':
    extract_assets()
