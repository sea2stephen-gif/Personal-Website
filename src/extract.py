#!/usr/bin/env python3
"""Extract source files from Stephen To - Portfolio.html."""
from pathlib import Path
import json
import re

BUNDLE = Path('Stephen To - Portfolio.html')
HEAD = Path('src/head.html')
BODY = Path('src/index.html')
CSS = Path('src/styles.css')


def extract():
    content = BUNDLE.read_text(encoding='utf-8', errors='ignore')
    marker = '<script type="__bundler/template">'
    start = content.find(marker)
    if start == -1:
        raise ValueError('Could not find bundler template marker')

    quote = content.find('"', start + len(marker))
    if quote == -1:
        raise ValueError('Could not find opening quote after marker')

    raw = content[quote:]
    html, idx = json.JSONDecoder().raw_decode(raw)

    # Extract head/body
    head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL | re.IGNORECASE)
    body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    if not head_match or not body_match:
        raise ValueError('Could not extract head/body from template')

    head_html = head_match.group(1).strip()
    body_html = body_match.group(1).strip()

    css_chunks = []
    def extract_styles(text):
        def replace(match):
            css_chunks.append(match.group(1).strip())
            return ''
        return re.sub(r'<style[^>]*>(.*?)</style>', replace, text, flags=re.DOTALL | re.IGNORECASE)

    head_html = extract_styles(head_html).strip()
    body_html = extract_styles(body_html).strip()
    css_text = '\n\n'.join(chunk for chunk in css_chunks if chunk).strip()

    HEAD.write_text(head_html + '\n', encoding='utf-8')
    BODY.write_text(body_html + '\n', encoding='utf-8')
    CSS.write_text(css_text + '\n', encoding='utf-8')

    print(f'Extracted head ({len(head_html)} chars)')
    print(f'Extracted body ({len(body_html)} chars)')
    print(f'Extracted CSS ({len(css_text)} chars)')
    print('Source files written to src/')


if __name__ == '__main__':
    extract()
