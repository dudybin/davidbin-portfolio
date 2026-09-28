#!/usr/bin/env python3
"""Builds index.html + the five project pages from the shared partials."""
import pathlib

HERE = pathlib.Path(__file__).parent
MENU = (HERE / "_menu.html").read_text()
FOOTER = (HERE / "_footer.html").read_text()

ASSET_VER = "22"   # bump when style.css or site.js change, to beat caches

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&'
    'family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">'
)


def shell(title, body, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
{FONTS}
<link rel="stylesheet" href="style.css?v={ASSET_VER}">
</head>
<body>
{MENU}
{body}
{FOOTER}
<script src="site.js?v={ASSET_VER}"></script>
</body>
</html>
"""


# id, slug, image, kicker, subtitle, title colour, subtitle colour, dark-ink button, cta
PANELS = [
    ("showreel", "showreel.html", "assets/showreel.jpg", "Previous Work", "Show Reel 2020",
     "#141414", "#141414", True, "Watch"),
    ("walmart", "walmart-ar.html", "assets/walmart.jpg", "Walmart AR", "Augmented Reality application",
     "#f2f2f2", "#f2f2f2", False, "View"),
    ("aps", "aps-support.html", "assets/aps.jpg", "APS Support", "Promotion Teaser for Amdocs",
     "#141414", "#2f2e2e", True, "View"),
    ("architecture", "architecture.html", "assets/architecture.jpg", "Architecture", "Architecture visualization Design",
     "#ffffff", "#ffffff", False, "View"),
    ("cloud", "cloud-services.html", "assets/cloud.jpg", "Cloud Services", "A Teaser for MWC",
     "#f2f2f2", "#f2f2f2", False, "View"),
]


def build_index():
    dots = "\n".join(
        f'    <li><a href="#{p[0]}" aria-label="{p[3]}"></a></li>' for p in PANELS
    )
    sections = []
    for pid, href, img, kicker, sub, tcol, scol, dark_btn, cta in PANELS:
        cls = "panel panel--light" if dark_btn else "panel"
        if pid == PANELS[0][0]:
            cls += " panel--hero"
        sections.append(f"""<section class="{cls}" id="{pid}" style="--t:{tcol};--s:{scol}">
  <div class="panel__bg" style="--bg:url('{img}');--bg-m:url('{img.replace("assets/","assets/m/")}')"></div>
  <div class="panel__copy">
    <h2 class="kicker">{kicker}</h2>
    <p class="sub">{sub}</p>
    <a class="btn" href="{href}">{cta}</a>
  </div>
</section>""")

    body = (
        f'<ul class="dots">\n{dots}\n</ul>\n<main>\n'
        + "\n".join(sections)
        + "\n</main>"
    )
    return shell(
        "HOME | David Bin",
        body,
        "David Bin — art direction, animation, rendering and compositing. Selected previous work.",
    )


PROJECTS = [
    dict(
        file="showreel.html",
        template="reel",                       # full-bleed page background
        title="REEL | David Bin",
        h1="REEL 2020",
        lead="",
        credits="",
        vimeo="479598104",
        poster="assets/poster-showreel.jpg",
        bg="assets/bg-showreel.jpg",
        desc="Show Reel 2020 by David Bin.",
    ),
    dict(
        file="walmart-ar.html",
        template="hero",                       # 489px hero, then a black page
        title="Walmart AR | David Bin",
        h1="Walmart Sam's Club AR",
        lead="An app for kids to take photos and experience Augmented 3d animations.",
        credits="Technical Artist | Texture baking | Animations | Optimization",
        local="assets/walmart-ar.mp4",
        poster="assets/walmart-poster.jpg",
        bg="assets/bg-walmart.jpg",
        desc="Walmart Sam's Club AR — an app for kids to take photos and experience augmented 3D animations.",
    ),
    dict(
        file="aps-support.html",
        template="hero",
        title="Amdocs APS Support Community | David Bin",
        h1="Amdocs APS Support Community",
        lead="",
        credits="Art Direction | Animation | Rendering | Compositing",
        vimeo="28478897",
        poster="assets/poster-aps.jpg",
        bg="assets/bg-aps.jpg",
        desc="Amdocs APS Support Community — promotion teaser.",
    ),
    dict(
        file="architecture.html",
        template="hero",
        title="Architecture | David Bin",
        h1="Architecture Projects",
        lead="Some of my Architecture 3D design frames and renders.",
        credits="Art Direction | Compositing | Animation | Rendering",
        vimeo="479600777",
        poster="assets/poster-architecture.jpg",
        bg="assets/bg-architecture.jpg",
        desc="Architecture visualization design.",
    ),
    dict(
        file="cloud-services.html",
        template="hero",
        title="Amdocs Cloud Services | David Bin",
        h1="Amdocs Cloud Services",
        lead="A short teaser for Amdocs Cloud Services.",
        credits="Art Direction | Animation | Rendering | Compositing",
        vimeo="41475388",
        poster="assets/poster-cloud.jpg",
        bg="assets/bg-cloud.jpg",
        desc="A short teaser for Amdocs Cloud Services, made for MWC.",
    ),
]


def build_project(p):
    if "vimeo" in p:
        vid = p["vimeo"]
        # Facade: the poster loads instantly and the Vimeo iframe is only
        # inserted on click, so a blocked embed degrades to the link below.
        player = (
            f'    <button class="facade" type="button" data-vimeo="{vid}"\n'
            f'      style="background-image:url(\'{p["poster"]}\')"\n'
            f'      aria-label="Play {p["h1"]}">\n'
            f'      <span class="facade__play" aria-hidden="true"></span>\n'
            f'    </button>'
        )
    else:
        player = (
            f'    <video controls preload="metadata" playsinline poster="{p["poster"]}">\n'
            f'      <source src="{p["local"]}" type="video/mp4">\n'
            f'      Your browser does not support the video tag.\n'
            f'    </video>'
        )

    stage = f"""  <div class="stage">
    <div class="player">
{player}
    </div>
    <a class="back" href="index.html">Back</a>
  </div>"""

    if p["template"] == "reel":
        body = f"""<main class="proj proj--reel">
  <div class="proj__wash" style="--bg:url('{p["bg"]}');--bg-m:url('{p["bg"].replace("assets/","assets/m/")}')"></div>
  <div class="stage">
    <h1 class="proj__big">{p["h1"]}</h1>
  </div>
{stage}
</main>"""
    else:
        lead = f'    <p class="proj__lead">{p["lead"]}</p>\n' if p["lead"] else ""
        credits = f'    <p class="proj__credits">{p["credits"]}</p>\n' if p["credits"] else ""
        body = f"""<main class="proj proj--hero">
  <div class="proj__banner" style="--bg:url('{p["bg"]}');--bg-m:url('{p["bg"].replace("assets/","assets/m/")}')"></div>
  <div class="stage">
    <h1 class="proj__title">{p["h1"]}</h1>
{lead}{credits}  </div>
{stage}
</main>"""

    return shell(p["title"], body, p["desc"])


(HERE / "index.html").write_text(build_index())
for p in PROJECTS:
    (HERE / p["file"]).write_text(build_project(p))

print("built: index.html + " + ", ".join(p["file"] for p in PROJECTS))


# ---------------------------------------------------------------- gallery +
# text pages reached from the menu. All share one full-bleed background
# (projects_we_BG) with a 60px light title at x=86 / y=131, then a grid.

GALLERIES = [
    dict(
        file="post-production.html",
        title="POST-PRODUCTION | David Bin",
        h1="POST-PRODUCTION",
        desc="Post-production work by David Bin.",
        cols=3, tile=(403, 227), gap=(20, 90),
        # each tile opens its Vimeo video in a lightbox, as the original does
        items=[
            ("assets/pages/pp1.jpg", "Amdocs APS Community", "vm:28478897"),
            ("assets/pages/pp2.jpg", "Amdocs CES9 Launch", "vm:20839390"),
            ("assets/pages/pp3.jpg", "Amdocs Cloud Services", "vm:41475388"),
            ("assets/pages/pp4.jpg", "Amdocs Prepaid Solutions", "vm:41490826"),
            ("assets/pages/pp-png.jpg", "Hagag Salame", "vm:482241338"),
            ("assets/pages/pp5.jpg", "Lilien 8", "vm:479600777"),
            ("assets/pages/pp6.jpg", "Nature-Valley", "vm:76411105"),
            ("assets/pages/pp7.jpg", "Netivei Israel", "vm:182375656"),
            ("assets/pages/pp8.jpg", "Opel MOKKA", "vm:95156760"),
            ("assets/pages/pp9.jpg", "Pop Star", "vm:482240633"),
            ("assets/pages/pp10.jpg", "Reshet 13", "vm:479737472"),
        ],
    ),
    dict(
        file="unity.html",
        title="UNITY | David Bin",
        h1="UNITY",
        desc="Realtime work in Unity by David Bin.",
        cols=3, tile=(533, 300), gap=(20, 90),
        # every Unity tile opens a YouTube video
        items=[
            ("assets/pages/un1.jpg", "Reel AR", "yt:1E8qq7zrl3g"),
            ("assets/pages/un2.jpg", "Butterflies AR", "yt:hu5f1qUypMU"),
            ("assets/pages/un3.jpg", "Drone AR flight", "yt:kCsdNVtXLe8"),
            ("assets/pages/un4.jpg", "States machine", "yt:JzNqLDqmxFU"),
            ("assets/pages/un5.jpg", "Walmart AR", "yt:jwTDw3qDkQ4"),
            ("assets/pages/un6.jpg", "Game Platform", "yt:LI9PAQDbXns"),
        ],
    ),
    dict(
        file="unreal-for-vp.html",
        title="UNREAL FOR VP | David Bin",
        h1="VIRTUAL PRODUCTION",
        desc="Virtual production work in Unreal by David Bin.",
        cols=3, tile=(533, 300), gap=(20, 90),
        # two tiles hold YouTube videos; the rest enlarge their animation
        items=[
            ("assets/pages/vp1.mp4", "Dynamic Graphs Blue Print", "media"),
            ("assets/pages/vp2.mp4", "Aximmtery\\Unreal", "media"),
            ("assets/pages/vp3.mp4", "Multi-Virtual cameras output for VP", "media"),
            ("assets/pages/vp5.jpg", "Pilot ONE", "yt:wePkh3OXigs"),
            ("assets/pages/vp4.mp4", "Shooting day", "media"),
            ("assets/pages/vp6.jpg", "Amdocs session CEO", "yt:3mklm2gUIHE"),
        ],
    ),
]


def build_gallery(g):
    tiles = []
    for src, caption, kind in g["items"]:
        if src.endswith(".mp4"):
            media = (f'<video src="{src}" autoplay loop muted playsinline '
                     f'preload="metadata"></video>')
        else:
            media = f'<img src="{src}" alt="{caption}" loading="lazy">'
        if kind:
            if kind.startswith("vm:"):
                attr = f'data-vimeo="{kind[3:]}"'
                play = '<span class="tile__play" aria-hidden="true"></span>'
            elif kind.startswith("yt:"):
                attr = f'data-youtube="{kind[3:]}"'
                play = '<span class="tile__play" aria-hidden="true"></span>'
            else:
                attr = f'data-media="{src}"'
                play = ''
            media = (f'<button class="tile__open" type="button" {attr}\n'
                     f'          aria-label="Play {caption}">{media}{play}</button>')
        tiles.append(
            f'      <li class="tile">\n'
            f'        {media}\n'
            f'        <p class="tile__cap">{caption}</p>\n'
            f'      </li>'
        )
    w, h = g["tile"]
    cg, rg = g["gap"]
    body = f"""<main class="page">
  <div class="page__wash" style="--bg:url('assets/pages/pages-bg.jpg');--bg-m:url('assets/m/pages-bg.jpg')"></div>
  <div class="page__body">
    <h1 class="page__title">{g["h1"]}</h1>
    <ul class="grid" style="--tile-w:{w}px;--tile-h:{h}px;--col-gap:{cg}px;--row-gap:{rg}px;--cols:{g["cols"]}">
{chr(10).join(tiles)}
    </ul>
  </div>
  <div class="lightbox" id="lightbox" aria-hidden="true">
    <button class="lightbox__close" type="button" aria-label="Close video">
      <svg viewBox="0 0 31 31" aria-hidden="true"><path d="M2 2 L29 29 M29 2 L2 29" stroke="currentColor" stroke-width="1.6" fill="none"/></svg>
    </button>
    <div class="lightbox__frame"></div>
  </div>
</main>"""
    return shell(g["title"], body, g["desc"])


ABOUT = """<main class="about-page">
  <div class="about-page__portrait" style="--bg:url('assets/pages/about.jpg?v={ASSET_VER}');--bg-m:url('assets/m/about.jpg?v={ASSET_VER}')"></div>
  <div class="about-page__body">
    <h1 class="page__title">ABOUT ME</h1>
    <p class="about-page__text">Hi my name is David and I am a Technical Artist.</p>
    <p class="about-page__text">I work with 2D and 3D software's for Realtime engines
    like Unity and Unreal to produce emissive content or interactive experience.</p>
    <a class="about-page__cv"
       href="https://6ecf9047-5770-44af-b7c8-99aaaaf030a5.filesusr.com/ugd/28d79f_c11fb3165442404bbb110c5ff58b774f.pdf"
       target="_blank" rel="noopener">Download CV</a>
  </div>
</main>"""

CONTACT = """<main class="contact-page">
  <video class="contact-page__bg" src="assets/pages/contact-bg.mp4?v={ASSET_VER}"
         poster="assets/pages/contact-poster.jpg?v={ASSET_VER}"
         autoplay loop muted playsinline preload="metadata"></video>
  <div class="contact-page__body">
    <h1 class="page__title">HI THERE</h1>
    <p class="contact__thanks" id="thanks" hidden>Thanks for submitting!</p>
    <form class="contact" action="https://formsubmit.co/Dudybin@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_subject" value="New message from davidbin portfolio">
      <input type="hidden" name="_next" value="https://dudybin.github.io/davidbin-portfolio/contact.html?sent=1">
      <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
      <label class="contact__label" for="c-name">Your Name</label>
      <input id="c-name" type="text" name="name" autocomplete="name">
      <label class="contact__label" for="c-mail">Your Mail</label>
      <input id="c-mail" type="email" name="email" autocomplete="email" required>
      <textarea name="message" rows="6" placeholder="Message" aria-label="Message"></textarea>
      <button type="submit">Send</button>
    </form>
  </div>
</main>"""

for g in GALLERIES:
    (HERE / g["file"]).write_text(build_gallery(g))
(HERE / "about.html").write_text(shell("ABOUT | David Bin", ABOUT.replace("{ASSET_VER}", ASSET_VER), "About David Bin, Technical Artist."))
(HERE / "contact.html").write_text(shell("CONTACT | David Bin", CONTACT.replace("{ASSET_VER}", ASSET_VER), "Get in touch with David Bin."))
print("built: " + ", ".join([g["file"] for g in GALLERIES] + ["about.html", "contact.html"]))
