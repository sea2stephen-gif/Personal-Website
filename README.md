# Personal Portfolio Website

This repository contains a bundled portfolio site and now includes a clean source workflow.

## Source workflow

Edit these source files:

- `src/head.html` — head contents
- `src/index.html` — body content
- `src/styles.css` — styling

## Commands

### Extract source files
If you need to generate source files from the existing bundle:
```bash
python src/extract.py
```

### Build bundled portfolio
After editing source files:
```bash
python build.py
```

### Publish root site
If your host serves from repo root:
```bash
python src/publish.py
```

## Notes

- `Stephen To - Portfolio.html` remains the bundle target.
- `index.html` and `styles.css` are created only when you run `python src/publish.py`.
- Keep `src/` files as your working source.

