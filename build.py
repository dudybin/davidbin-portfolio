#!/usr/bin/env python3
"""Builds index.html + the five project pages from the shared partials."""
import pathlib

HERE = pathlib.Path(__file__).parent
MENU = (HERE / "_menu.html").read_text()
FOOTER = (HERE / "_footer.html").read_text()

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
<link rel="stylesheet" href="style.css">
</head>
<body>
{MENU}
{body}
{FOOTER}
<script src="site.js"></script>
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
  <div class="panel__bg" style="background-image:url('{img}')"></div>
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
  <div class="proj__wash" style="background-image:url('{p["bg"]}')"></div>
  <div class="stage">
    <h1 class="proj__big">{p["h1"]}</h1>
  </div>
{stage}
</main>"""
    else:
        lead = f'    <p class="proj__lead">{p["lead"]}</p>\n' if p["lead"] else ""
        credits = f'    <p class="proj__credits">{p["credits"]}</p>\n' if p["credits"] else ""
        body = f"""<main class="proj proj--hero">
  <div class="proj__banner" style="background-image:url('{p["bg"]}')"></div>
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
        items=[f"assets/pages/pp{i}.jpg" for i in (1, 2, 3, 4)]
              + ["assets/pages/pp-png.jpg"]
              + [f"assets/pages/pp{i}.jpg" for i in (5, 6, 7, 8, 9, 10)],
    ),
    dict(
        file="unity.html",
        title="UNITY | David Bin",
        h1="UNITY",
        desc="Realtime work in Unity by David Bin.",
        cols=3, tile=(533, 300), gap=(20, 90),
        items=[f"assets/pages/un{i}.jpg" for i in range(1, 7)],
    ),
    dict(
        file="unreal-for-vp.html",
        title="UNREAL FOR VP | David Bin",
        h1="VIRTUAL PRODUCTION",
        desc="Virtual production work in Unreal by David Bin.",
        cols=3, tile=(533, 300), gap=(20, 90),
        items=["assets/pages/vp1.mp4", "assets/pages/vp2.mp4", "assets/pages/vp3.mp4",
               "assets/pages/vp5.jpg", "assets/pages/vp4.mp4", "assets/pages/vp6.jpg"],
    ),
]


def build_gallery(g):
    tiles = []
    for src in g["items"]:
        if src.endswith(".mp4"):
            tiles.append(
                f'      <li><video src="{src}" autoplay loop muted playsinline '
                f'preload="metadata"></video></li>'
            )
        else:
            tiles.append(f'      <li><img src="{src}" alt="" loading="lazy"></li>')
    w, h = g["tile"]
    cg, rg = g["gap"]
    body = f"""<main class="page">
  <div class="page__wash" style="background-image:url('assets/pages/pages-bg.jpg')"></div>
  <div class="page__body">
    <h1 class="page__title">{g["h1"]}</h1>
    <ul class="grid" style="--tile-w:{w}px;--tile-h:{h}px;--col-gap:{cg}px;--row-gap:{rg}px;--cols:{g["cols"]}">
{chr(10).join(tiles)}
    </ul>
  </div>
</main>"""
    return shell(g["title"], body, g["desc"])


ABOUT = """<main class="page">
  <div class="page__wash" style="background-image:url('assets/pages/pages-bg.jpg')"></div>
  <div class="page__body">
    <h1 class="page__title">ABOUT ME</h1>
    <div class="about">
      <img class="about__portrait" src="assets/pages/about.jpg" alt="David Bin">
      <div class="about__text">
        <p>Hi my name is David and I am a Technical Artist.</p>
        <p>I work with 2D and 3D software's for Realtime engines like Unity and
        Unreal to produce emissive content or interactive experience.</p>
      </div>
    </div>
  </div>
</main>"""

CONTACT = """<main class="page">
  <div class="page__wash" style="background-image:url('assets/pages/pages-bg.jpg')"></div>
  <div class="page__body">
    <h1 class="page__title">HI THERE</h1>
    <form class="contact" action="https://formsubmit.co/Dudybin@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <label>Name<input type="text" name="name" autocomplete="name"></label>
      <label>Email<input type="email" name="email" autocomplete="email" required></label>
      <label>Subject<input type="text" name="subject"></label>
      <label>Message<textarea name="message" rows="6"></textarea></label>
      <button type="submit">Send</button>
    </form>
  </div>
</main>"""

for g in GALLERIES:
    (HERE / g["file"]).write_text(build_gallery(g))
(HERE / "about.html").write_text(shell("ABOUT | David Bin", ABOUT, "About David Bin, Technical Artist."))
(HERE / "contact.html").write_text(shell("CONTACT | David Bin", CONTACT, "Get in touch with David Bin."))
print("built: " + ", ".join([g["file"] for g in GALLERIES] + ["about.html", "contact.html"]))
