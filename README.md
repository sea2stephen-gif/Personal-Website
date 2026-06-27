# stephenvanto.com

Personal portfolio site, self-hosted on a home server and auto-deployed on every push to `main`.

## Editing

All source files are in `src/`:

- `src/head.html` — `<head>` contents (meta tags, font links, etc.)
- `src/index.html` — `<body>` content
- `src/styles.css` — styles (inlined into the built page)
- `src/assets/` — fonts and JS referenced by the page

Push changes to `main` and the live site updates automatically within seconds.

## How deployment works

1. A GitHub webhook fires on every push to `main`
2. The server pulls the latest code (`git reset --hard origin/main`)
3. `assemble.py` concatenates `head.html` + `styles.css` + `index.html` into a single `dist/index.html` and copies `src/assets/` to `dist/assets/`
4. Docker rebuilds and restarts the nginx container serving the `dist/` directory
5. Cloudflare Tunnel routes `stephenvanto.com` → the local nginx instance (no open ports on the home network)

A daily cron job also runs the deploy as a fallback in case a webhook delivery is missed.
