#!/usr/bin/env python3
"""Publish script to copy src sources to index.html for host deployments."""
from pathlib import Path
import shutil

SRC_INDEX = Path('src/index.html')
SRC_CSS = Path('src/styles.css')
DEST_INDEX = Path('index.html')
DEST_CSS = Path('styles.css')


def publish():
    if not SRC_INDEX.exists():
        raise FileNotFoundError(f'{SRC_INDEX} does not exist')
    if not SRC_CSS.exists():
        raise FileNotFoundError(f'{SRC_CSS} does not exist')

    print('Publishing src/ -> root files...')
    shutil.copyfile(SRC_INDEX, DEST_INDEX)
    shutil.copyfile(SRC_CSS, DEST_CSS)
    print(f'Published {DEST_INDEX} and {DEST_CSS}')


if __name__ == '__main__':
    publish()
