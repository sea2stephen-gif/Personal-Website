#!/usr/bin/env python3
"""Build Stephen To - Portfolio.html from src sources."""
from pathlib import Path
import json
import re

SRC_HEAD = Path('src/head.html')
SRC_BODY = Path('src/index.html')
SRC_CSS = Path('src/styles.css')
BUNDLE = Path('Stephen To - Portfolio.html')


def build():
    head = SRC_HEAD.read_text(encoding='utf-8')
    body = SRC_BODY.read_text(encoding='utf-8')
    css = SRC_CSS.read_text(encoding='utf-8')

    full_html = '<!DOCTYPE html>\n<html><head>\n'
    full_html += head.strip() + '\n'
    full_html += '  <style>' + css.strip() + '</style>\n'
    full_html += '</head>\n<body>\n'
    full_html += body.strip() + '\n'
    full_html += '</body>\n</html>'

    content = BUNDLE.read_text(encoding='utf-8', errors='ignore')
    marker = '<script type="__bundler/template">'
    start = content.find(marker)
    if start == -1:
        raise ValueError('Could not find bundler template marker')

    quote = content.find('"', start + len(marker))
    if quote == -1:
        raise ValueError('Could not find opening quote after marker')

    raw = content[quote:]
    _, idx = json.JSONDecoder().raw_decode(raw)

    new_template = json.dumps(full_html)
    new_content = content[:quote] + new_template + content[quote+idx:]
    BUNDLE.write_text(new_content, encoding='utf-8')

    print(f'Built {BUNDLE} from src/')
    print('Bundle updated successfully')


if __name__ == '__main__':
    build()
