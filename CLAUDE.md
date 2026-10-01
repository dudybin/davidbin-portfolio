# CLAUDE.md

**Read `DIRECTIONS.md` first** — it is the full handover: what the site is, how it
is built, deliberate decisions not to "fix", how to measure the original Wix site,
traps, open items, and how this user works.

Essentials:

- Static rebuild of David Bin's Wix portfolio, hosted on GitHub Pages
  (https://dudybin.github.io/davidbin-portfolio/, `main` branch, repo root).
- Brief: **exactly the same site** as https://dudybin8.wixsite.com/davidbin.
  Measure the original; never eyeball. Give numbers when claiming a match.
- `build.py` is the source of truth. Edit `PANELS` / `PROJECTS` / `GALLERIES`
  there or `_menu.html` / `_footer.html`, then `python3 build.py`. Never hand-edit
  the generated `.html`. Stdlib only — runs on macOS and Linux.
- After the last CSS/JS edit, bump `ASSET_VER` in `build.py`.
- Regression numbers (desktop 1440×900): home scrollHeight **4502**, panel title
  offsets **270/345/345/345/345**, gallery tiles **404px at x=86/510/934**.
- Preview: `python3 -m http.server 8777`.

## Where we stopped (keep this section current)

- Latest: MOBILE GAMES menu item → https://davidbin-private.pages.dev (a separate,
  password-gated Cloudflare Pages site; not in this repo).
- Site is complete and deployed; no known bugs. Open items are in
  `DIRECTIONS.md` §7 (biggest: portfolio ends at 2020 — don't add new work
  unprompted).
