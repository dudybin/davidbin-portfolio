# DIRECTIONS — for whoever picks this up next

Read this before changing anything. It records what the project is, how it is
built, the decisions that are deliberate, the mistakes that cost the most time,
and how to verify your own work.

- **Live:** https://dudybin.github.io/davidbin-portfolio/
- **Repo:** https://github.com/dudybin/davidbin-portfolio (public, GitHub Pages, `main` branch, root)
- **Local:** `/Users/davidbi/Work/Dudy_Unity/Claude/davidbin-portfolio`
- **Owner:** David Bin — dudybin@gmail.com, GitHub `dudybin`

---

## 1. What this is

A static, hand-built reproduction of David's Wix portfolio at
`https://dudybin8.wixsite.com/davidbin`, moved onto free hosting he controls.

**The brief was "exactly the same site."** That is the standard the work was held
to, and it was enforced strictly — the user repeatedly rejected output that was
merely close. Assume that standard still applies unless he says otherwise.

The original Wix site is still live. **It is the reference.** Do not guess at the
design; measure it (see §5).

---

## 2. Current state

Complete and deployed. Eleven pages, all measured against the original:

| Page | File | Original URL |
|---|---|---|
| Home (5 scrolling panels) | `index.html` | `/davidbin` |
| Show Reel 2020 | `showreel.html` | `/showreel-2020` |
| Walmart AR | `walmart-ar.html` | `/copy-of-amdocs-cloud-services-2` |
| APS Support | `aps-support.html` | `/copy-of-amdocs-cloud-services` |
| Architecture | `architecture.html` | `/copy-of-amdocs-aps-support-communit-1` |
| Cloud Services | `cloud-services.html` | `/1` |
| Post-Production | `post-production.html` | `/projects` |
| Unity | `unity.html` | `/copy-of-projects-1` |
| Unreal for VP | `unreal-for-vp.html` | `/copy-of-unity` |
| About | `about.html` | `/about` |
| Contact | `contact.html` | `/contact-page` |

**Fully self-hosted.** No asset, link or reference points at `wixsite.com`,
`wixstatic.com` or `filesusr.com`. Remaining third parties are only: Vimeo and
YouTube (embedded videos), Google Fonts, FormSubmit (contact form).

Verified at the last commit: all 11 pages and all 80 tracked assets return 200
live; `build.py` reproduces the committed HTML byte-for-byte.

---

## 3. How it is built

No framework, no build toolchain beyond Python 3 and the standard library.

```
build.py        generates all 11 HTML pages — THE source of truth for content
_menu.html      shared nav overlay, injected into every page
_footer.html    shared footer, injected into every page
style.css       hand-written; desktop first, mobile in @media blocks
site.js         menu, lightbox, mobile image swap, dot nav
assets/         desktop artwork, videos, CV
assets/m/       phone-sized copies of every background (900px wide)
assets/pages/   per-page backgrounds, gallery stills, CV
```

To rebuild:

```bash
python3 build.py        # rewrites all 11 .html files
```

**Never hand-edit the generated `.html` files.** A rebuild silently overwrites
them. Content lives in the `PANELS`, `PROJECTS` and `GALLERIES` lists in
`build.py`; shared chrome lives in `_menu.html` / `_footer.html`.

### Local preview

```bash
python3 -m http.server 8777     # then open http://localhost:8777
```

### Deploy

```bash
git add -A && git commit -m "…" && git push origin main
```

GitHub Pages rebuilds in roughly a minute. If `gh` asks for auth, the account is
`dudybin` (`gh auth switch --user dudybin`). Commits are made as
`dudybin <dudybin@gmail.com>`.

---

## 4. Decisions that are deliberate — do not "fix" these

- **Desktop is a fixed-pixel reproduction.** 840px panels, 86px gutters, a 940px
  content column, titles at hard-coded offsets. This is not sloppiness — the
  original is a fixed Wix desktop layout and matching it was the requirement.
- **Mobile is a separate design, not a shrunk desktop.** The original serves a
  **320px-wide mobile design scaled to the device**. The mobile CSS therefore
  uses `vw` units derived from that 320 canvas (e.g. panel height `66.5vw` =
  213/320). Do not replace these with "sensible" breakpoints.
- **Fonts are substitutes.** The original uses **Lulo Clean** (titles) and
  **Helvetica Light** (body), both licensed to Wix and not redistributable.
  We use **Poppins** and **Roboto Light**. Poppins is narrower than Lulo Clean,
  so titles are **sized up and tracked out** to match the original's *block
  width*, not its nominal font-size. If a title looks the wrong size, check the
  rendered text width against the original before changing the font-size.
- **The header bar is black (`#000`).** The header element computes `#2f2e2e`,
  but that is a base layer the original covers with black strips. Sample what
  actually paints.
- **The bar scrolls away; the hamburger stays pinned.** Two different behaviours
  in one header — matching the original.
- **On mobile the hamburger becomes the close button.** The pinned hamburger sits
  exactly where the menu's X would, so the X is hidden below 900px.
- **The gallery Back button is centred** — a deliberate departure, requested by
  the user. The original anchors it 875px from the left.
- **The "Do not hesitate…" footer intro is hidden on mobile.** The original omits
  it there; the mobile footer is a different composition (copyright first on
  white, then contact/social in a grey band).
- **GIFs were re-encoded to muted looping MP4.** Visually identical, ~95%
  smaller (the contact background was 6.3MB of GIF → 134KB of MP4).

---

## 5. How to find the truth about the original

This is the most valuable thing in this document. Several rounds were wasted
reading the rendered page instead of the underlying data.

### Page content and galleries: use the page-data JSON

The original's HTML contains a `pagesMap` giving each page's data file. Fetch:

```
https://pages.parastorage.com/sites/<pageJsonFileName>.json.z?v=3
```

| Page | pageJsonFileName |
|---|---|
| HOME | `28d79f_0c5a932140d44d614ca0c33dfe9d3ecd_708` |
| REEL | `28d79f_cafdf25cea3dcfe9e2ea41addefb3ba6_702` |
| Walmart AR | `28d79f_076213f350bc2326eb4307263df51293_702` |
| APS Support | `28d79f_fa77e31dad98c81fb6ac8437dc5b7054_702` |
| Architecture | `28d79f_87fad7d0689abebb5c89c5d869b941a2_702` |
| Cloud Services | `28d79f_91eefc0933d68d1d86483b5fa821b12f_702` |
| POST-PRODUCTION | `28d79f_7e4a472c6d311f6871efe3db67b0da10_702` |
| UNITY | `28d79f_0ac1bcf5c2b7d36f22f248a1f08b5aa6_702` |
| UNREAL FOR VP | `28d79f_cf0e0525d18b6369a108e4ae3038cd09_702` |
| ABOUT | `28d79f_4536c0a31d837152803bf74eb1c4cb26_702` |
| CONTACT | `28d79f_0186057de675ce01f8133b529e9a4736_702` |

In that JSON, `data.document_data` holds every text block (`StyledText`),
image (`Image`), gallery (`ImageList`) and button. **This is authoritative.**
Three description paragraphs were wrong for several rounds because they were
transcribed from the rendered page instead — one truncated, one missing
entirely, one misworded.

Gallery images live inside a **cross-origin iframe** and are invisible to any
DOM query on the parent page. They can only be found this way.

### Layout: measure, do not eyeball

Open the original in a browser at a known viewport and read
`getBoundingClientRect()` plus `getComputedStyle()` for the element you care
about. Then measure the same element in the rebuild and compare numbers.
Every layout fix in this project came from that; every regression came from
skipping it.

For mobile, measure the original at a phone viewport — Wix serves its 320px
design, and the values you read are in that 320 canvas. Convert to `vw` by
`value / 320 * 100`.

### Images: Wix crops server-side

An image URL like `.../v1/fill/w_725,h_311,al_t/...` is **already cropped**.
`al_t` = align top, `al_c` = align centre. Download the cropped variant and the
framing matches; download the master and let CSS crop it and it will not. The
About portrait was wrong for a round because of this.

Also: `naturalWidth` may report a tiny placeholder (e.g. 123×92) until the real
image lazy-loads. Scroll it into view and wait before trusting any measurement.

---

## 6. Traps that cost real time

- **Cache.** `style.css` and `site.js` are versioned via `ASSET_VER` in
  `build.py` (currently `36`). **Bump it after your last CSS/JS edit, not
  before** — editing CSS after bumping means the browser reuses the old file
  under the same version, and your change appears not to work. The About
  portrait and the CV are versioned the same way, because their filenames never
  change.
- **Lazy-load deadlock.** An `<img loading="lazy">` with no `width`/`height`
  collapses to zero height, never intersects the viewport, and therefore never
  loads — the page silently comes up short. All gallery stills carry intrinsic
  dimensions (`_dims()` in `build.py` reads them at build time). Keep that.
- **The browser pane cannot render Wix's gallery iframes** and often shows them
  blank or white. That is a tooling limitation, not evidence the gallery is
  empty.
- **Vimeo embeds are blocked inside claude.ai artifact previews** and on some
  networks (`player.vimeo.com` specifically). A grey video box in a preview is
  usually not a site bug. Test on the real host.
- **The CV PDF on Wix is hotlink-protected** and returns Forbidden to anything
  off that domain. It is now hosted locally; do not point back at Wix.

---

## 7. Known gaps and possible next steps

Nothing is broken. These are open items, roughly in the order worth doing:

1. **The site still ends at 2020.** This is the biggest substantive gap. David's
   recent work — the MobileVFX Unity package, the URP shader work, Vector Tool —
   is stronger than anything currently shown. Adding a panel means one entry in
   `PANELS` plus a project page entry in `PROJECTS` in `build.py`. He has been
   told this twice and has not asked for it yet; **do not do it unprompted.**
2. **Shorter URL.** Renaming the repo to `dudybin.github.io` would give
   `https://dudybin.github.io` with no path. A custom domain also works.
3. **Contact form depends on FormSubmit**, a free third-party relay, already
   activated against dudybin@gmail.com. It works. If it ever stops, the
   alternatives are Formspree or a plain `mailto:`.
4. **Lulo Clean licence.** If David ever buys a webfont licence, dropping the
   files in and swapping the `font-family` makes the titles exact. The
   compensating size/tracking in `.kicker`, `.proj__big` and `.page__title`
   should then be reverted to the original's literal values.
5. **The mobile hamburger is white on every page**, matching the original, so it
   has low contrast over the pale APS panel and the white footer. The original
   shares this trait. Only change it if asked.

---

## 8. Working agreement with this user

Learned over the project; following it will save you rounds.

- **He checks the result against his original, carefully, and sends screenshots.**
  Assume anything you did not measure will be spotted.
- **Do not claim something matches unless you measured it.** Give the numbers.
- **Verify on the live site, not just locally** — cache and deploy lag have both
  produced false "it's broken" and false "it's fixed" readings.
- **Desktop must not regress when touching mobile.** After any CSS change,
  re-check: home page height **4502px**, panel title offsets
  **270 / 345 / 345 / 345 / 345**, gallery tiles **404px at x=86/510/934**.
  Those five numbers catch almost every regression.
- He is a technical artist — precise, visual, and fluent in layout. Plain
  explanation of cause is welcomed; hand-waving is not.

---

## 9. Quick regression check

After any change, before pushing:

```bash
python3 build.py
git status --porcelain     # must be empty except your intended edits
python3 -m http.server 8777
```

Then in a browser:

- **1440×900** — home `document.documentElement.scrollHeight` is **4502**
- **412×915** — home panel height **274**, title at **58** from panel top
- Any gallery page — stills have non-zero height and actually load
- Menu opens and closes; a project page video plays
- No horizontal scrollbar at **320px** wide

Deploy, then confirm on `https://dudybin.github.io/davidbin-portfolio/` with a
cache-busting query before reporting it done.
