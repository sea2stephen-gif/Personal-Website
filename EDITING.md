# Edit Workflow

This repo now supports a clean source workflow:

- `src/head.html` — head contents (meta, scripts, fonts)
- `src/index.html` — main page body content
- `src/styles.css` — all styling

## Extract from existing bundle
If you need to generate the source files from the current `Stephen To - Portfolio.html`, run:

```bash
python src/extract.py
```

## Edit

1. Edit `src/index.html` for content changes.
2. Edit `src/styles.css` for styling changes.
3. Edit `src/head.html` only if you need meta or head-level changes.

## Build

After edits, rebuild the bundle with:

```bash
python build.py
```

This updates `Stephen To - Portfolio.html` from the `src/` files.

## Publish for deployment

If your hosting server just serves files from the repo root, run:

```bash
python src/publish.py
```

That copies:

- `src/index.html` -> `index.html`
- `src/styles.css` -> `styles.css`

Then push the repo as normal.
