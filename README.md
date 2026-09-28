# David Bin — portfolio

A static rebuild of the original Wix site (dudybin8.wixsite.com/davidbin).
Plain HTML/CSS/JS — no build step needed to serve it.

## Structure

- `index.html` — the one-page scrolling home, five project panels
- `showreel.html`, `walmart-ar.html`, `aps-support.html`, `architecture.html`, `cloud-services.html`
- `style.css`, `site.js`
- `assets/` — panel stills, plus the self-hosted Walmart AR video
- `_menu.html`, `_footer.html`, `build.py` — the shared header/footer and the generator

## Editing

Change copy or add a project in `build.py` (the `PANELS` and `PROJECTS` lists),
edit the shared chrome in `_menu.html` / `_footer.html`, then regenerate:

```
python3 build.py
```

That rewrites `index.html` and the five project pages. Editing the generated
HTML directly also works — just know `build.py` will overwrite it next run.

## Preview locally

```
python3 -m http.server 8777
```

Then open http://localhost:8777

## Videos

Four projects embed Vimeo. Walmart AR is self-hosted (`assets/walmart-ar.mp4`,
1280x720, ~11 MB) because it was never on Vimeo.
