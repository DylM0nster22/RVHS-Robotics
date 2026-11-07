"""Shared layout, navigation and icon helpers for the RV Robotics site build."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = "https://rvrobotics.ycusd.org"
ASSET_VERSION = "20261107-5"
EMAIL = "rvrobotics@ycusd.org"
INSTAGRAM = "https://www.instagram.com/rv.robotics/"
INSTAGRAM_HANDLE = "@rv.robotics"
YOUTUBE = "https://www.youtube.com/@BadPlants1"
YOUTUBE_HANDLE = "@BadPlants1"
PHONE = "(530) 822-2500"
ROOM = "Room 408"
MEETINGS = "Thursdays &amp; Fridays"
CLASSROOM = "gftqhxdh"
ADDRESS_1 = "801 El Margarita Rd."
ADDRESS_2 = "Yuba City, CA 95993"

ICONS = {
    "arrow": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
    "arrow-up": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20V5M6 11l6-6 6 6"/></svg>',
    "check": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m4 12 5 5L20 6"/></svg>',
    "gear": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M18.7 5.3l-2.1 2.1M7.4 16.6l-2.1 2.1"/></svg>',
    "bolt": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4.5 13.5H11L10 22l8.5-11.5H12L13 2Z"/></svg>',
    "code": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m8 7-5 5 5 5M16 7l5 5-5 5M13.5 4 10.5 20"/></svg>',
    "megaphone": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 10v4a1 1 0 0 0 1 1h2l5 4V5L6 9H4a1 1 0 0 0-1 1Z"/><path d="M15 8.5a5 5 0 0 1 0 7M18 6a8.5 8.5 0 0 1 0 12"/></svg>',
    "chip": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5" rx=".5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/></svg>',
    "wrench": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.7 6.3a4 4 0 0 1-5.4 5.4L4 17l3 3 5.3-5.3a4 4 0 0 1 5.4-5.4l-2.6 2.6-2.4-2.4 2-2.6Z"/></svg>',
    "users": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.2 6.2 0 0 1 12.4 0"/><path d="M16 5.2a3.2 3.2 0 0 1 0 5.9M17.8 14.2A5.6 5.6 0 0 1 21.5 19"/></svg>',
    "shield": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 4.5 5.5v6c0 5 3.2 8.2 7.5 10 4.3-1.8 7.5-5 7.5-10v-6L12 2.5Z"/><path d="m8.5 12 2.3 2.3 4.7-4.8"/></svg>',
    "spark": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 14 9l6.5 2-6.5 2-2 6.5-2-6.5L3.5 11 10 9l2-6.5Z"/></svg>',
    "pin": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.6"/></svg>',
    "mail": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="5" width="19" height="14" rx="1.5"/><path d="m3 6.5 9 6.5 9-6.5"/></svg>',
    "phone": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3.5h3.5l1.5 4-2 1.5a13 13 0 0 0 5.5 5.5l1.5-2 4 1.5V18a2.5 2.5 0 0 1-2.7 2.5C9 19.6 4.4 15 3.5 7.2A2.5 2.5 0 0 1 5 3.5Z"/></svg>',
    "trophy": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 4h10v4a5 5 0 0 1-10 0V4Z"/><path d="M7 6H4.5a2.5 2.5 0 0 0 0 5H7M17 6h2.5a2.5 2.5 0 0 1 0 5H17M12 13v4M8 21h8M10 17h4"/></svg>',
    "book": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 5.5A2.5 2.5 0 0 1 5.5 3H11v18H5.5A2.5 2.5 0 0 1 3 18.5v-13Z"/><path d="M21 5.5A2.5 2.5 0 0 0 18.5 3H13v18h5.5a2.5 2.5 0 0 0 2.5-2.5v-13Z"/></svg>',
    "calendar": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="17" rx="1.5"/><path d="M8 2.5v4M16 2.5v4M3 9.5h18M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01"/></svg>',
    "download": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M7 10l5 5 5-5M4 20h16"/></svg>',
    "instagram": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none"/></svg>',
    "youtube": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.5v5l4.5-2.5L10 9.5Z" fill="currentColor" stroke="none"/></svg>',
    "play": '<svg class="{cls}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.2v13.6L19 12 8 5.2Z"/></svg>',
    "link": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13.5a4.5 4.5 0 0 0 6.4 0l2.4-2.4a4.5 4.5 0 0 0-6.4-6.4L11 6"/><path d="M14 10.5a4.5 4.5 0 0 0-6.4 0l-2.4 2.4a4.5 4.5 0 0 0 6.4 6.4L13 18"/></svg>',
    "close": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M5 5l14 14M19 5 5 19"/></svg>',
    "prev": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>',
    "next": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>',
    "zoom": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m15.5 15.5 5 5M10.5 7.5v6M7.5 10.5h6"/></svg>',
    "external": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 4h6v6M20 4l-9 9M19 14v4.5A1.5 1.5 0 0 1 17.5 20h-12A1.5 1.5 0 0 1 4 18.5v-12A1.5 1.5 0 0 1 5.5 5H10"/></svg>',
    "rotate": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 12a8.5 8.5 0 1 1-2.9-6.4"/><path d="M20.5 4v5h-5"/></svg>',
    "wireframe": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 2.5 8 4.5v10l-8 4.5-8-4.5v-10l8-4.5Z"/><path d="m4 7 8 4.5L20 7M12 11.5V21.5M4 17l8-5.5M20 17l-8-5.5"/></svg>',
    "grid": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="1"/><path d="M3.5 9h17M3.5 15h17M9 3.5v17M15 3.5v17"/></svg>',
    "fullscreen": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3H3v5M16 3h5v5M8 21H3v-5M16 21h5v-5"/></svg>',
    "collapse": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8h5V3M21 8h-5V3M3 16h5v5M21 16h-5v5"/></svg>',
    "reset": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 10a8 8 0 1 1 .6 6.5"/><path d="M4.5 4v6h6"/><circle cx="12" cy="12" r="1.2" fill="currentColor" stroke="none"/></svg>',
    "cube": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m12 2.5 8.5 4.75v9.5L12 21.5l-8.5-4.75v-9.5L12 2.5Z"/><path d="m3.5 7.25 8.5 4.75 8.5-4.75M12 12v9.5"/></svg>',
    "robot": '<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="7.5" width="16" height="12" rx="2"/><path d="M12 3.5V7.5M9 3.5h6M8.5 12h.01M15.5 12h.01M9 16h6M1.5 11v5M22.5 11v5"/></svg>',
}

BRAND_MARK = """<img class="brand-logo" src="assets/img/logo-mark.webp" width="300" height="229" alt="" aria-hidden="true" decoding="async">"""

NAV = [
    ("about.html", "About", "about"),
    ("robots.html", "Build", "robots"),
    ("cad.html", "CAD", "cad"),
    ("sponsors.html", "Sponsors", "sponsors"),
    ("watch.html", "Watch", "watch"),
    ("gallery.html", "Gallery", "gallery"),
    ("join.html", "Join", "join"),
    ("contact.html", "Contact", "contact"),
]


def icon(name, cls=""):
    return ICONS[name].format(cls=cls)


def header(active):
    def current(key):
        return ' aria-current="page"' if key == active else ""

    links = "\n".join(
        f'<a href="{href}"{current(key)}>{label}</a>'
        for href, label, key in NAV
    )
    mobile_links = "\n".join(
        f'<li><a href="{href}"{current(key)}>{label}<span>{idx:02d}</span></a></li>'
        for idx, (href, label, key) in enumerate(NAV, start=1)
    )
    return f"""<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="River Valley Robotics — home">
      {BRAND_MARK}
      <span class="brand-type">River Valley <em>Robotics</em></span>
    </a>
    <nav class="nav" aria-label="Primary">
      {links}
    </nav>
    <div class="header-actions">
      <a class="btn btn--primary" href="sponsors.html#tiers">Sponsor the team {icon("arrow", "btn-arrow")}</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">
        <span class="nav-toggle-bars" aria-hidden="true"><span></span><span></span><span></span></span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav" aria-hidden="true">
  <nav aria-label="Mobile">
    <ul>
      {mobile_links}
    </ul>
  </nav>
  <div class="mobile-nav-footer">
    <a class="btn btn--primary" href="sponsors.html#tiers">Sponsor the team</a>
    <a class="btn btn--ghost" href="join.html">Join the team</a>
  </div>
</div>"""


def footer():
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="brand brand--footer" href="index.html" aria-label="River Valley Robotics — home">
          <img class="brand-logo brand-logo--footer" src="assets/img/logo-footer.webp" width="360" height="339" alt="River Valley Robotics">
        </a>
        <p>A student club at River Valley High School. We design, build, and drive combat robots in Room 408.</p>
        <p class="footer-meetings">Meets {MEETINGS} &middot; {ROOM}</p>
        <div class="footer-socials">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="River Valley Robotics on Instagram">{icon("instagram")}</a>
          <a href="{YOUTUBE}" target="_blank" rel="noopener" aria-label="Match videos on YouTube">{icon("youtube")}</a>
          <a href="mailto:{EMAIL}" aria-label="Email River Valley Robotics">{icon("mail")}</a>
          <a href="https://rvhs.ycusd.org/" target="_blank" rel="noopener" aria-label="River Valley High School website">{icon("link")}</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="about.html">About the club</a></li>
          <li><a href="robots.html">The build</a></li>
          <li><a href="cad.html">3D CAD viewer</a></li>
          <li><a href="watch.html">Watch the matches</a></li>
          <li><a href="gallery.html">Gallery</a></li>
          <li><a href="sponsors.html">Sponsorship</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Get involved</h4>
        <ul>
          <li><a href="join.html">Join the club</a></li>
          <li><a href="join.html#mentors">Parents &amp; mentors</a></li>
          <li><a href="sponsors.html#tiers">Sponsor the team</a></li>
          <li><a href="assets/RVRobotics-Sponsorship-Packet.pdf">Sponsorship packet</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <address>
          {ADDRESS_1}<br>
          {ADDRESS_2}<br>
          <a href="tel:+15308222500">{PHONE}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </address>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> River Valley Robotics &middot; River Valley High School</p>
      <div class="footer-legal">
        <a href="https://www.ycusd.org/Non-Discrimination-Policy/index.html" target="_blank" rel="noopener">Non-discrimination policy</a>
        <a href="credits.html">Credits</a>
        <a href="accessibility.html">Accessibility</a>
      </div>
    </div>
    <div class="footer-nondiscrimination">
      <p>Yuba City Unified School District prohibits discrimination, harassment (including sexual harassment), intimidation, and bullying based on actual or perceived race, color, ethnicity, national origin, immigration status, ancestry, age, creed, religion, political affiliation, gender, gender identity, gender expression, genetic information, mental or physical disability, sex, sexual orientation, marital status, pregnancy or parental status, medical information, military veteran status, affiliation with the Boy Scouts of America and other designated youth groups, association with a person or group with one or more of these actual or perceived characteristics, or any other basis protected by law or regulation, in its educational programs or employment.</p>
    </div>
  </div>
</footer>"""


def layout(title, description, active, body, filename="index.html", body_class="", og_image="assets/img/og.jpg", extra_head="", robots="index, follow"):
    canonical = SITE_URL + "/" + ("" if filename == "index.html" else filename)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#173d20">
  <meta name="robots" content="{robots}">
  <script>document.documentElement.classList.add("js");</script>

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="River Valley Robotics">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE_URL}/{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{SITE_URL}/{og_image}">

  <link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="assets/img/icon-192.png" sizes="192x192" type="image/png">
  <link rel="apple-touch-icon" href="assets/img/icon-192.png">
  <link rel="manifest" href="site.webmanifest">
  <link rel="preload" href="assets/fonts/barlow-condensed-800.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/inter-var.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/site.css?v={ASSET_VERSION}">
  {extra_head}
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "EducationalOrganization",
    "name": "River Valley Robotics",
    "alternateName": "RVHS Robotics",
    "url": "{SITE_URL}/",
    "logo": "{SITE_URL}/assets/img/icon-512.png",
    "description": "Student-run combat robotics club at River Valley High School in Yuba City, California.",
    "parentOrganization": {{
      "@type": "HighSchool",
      "name": "River Valley High School",
      "url": "https://rvhs.ycusd.org/"
    }},
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "801 El Margarita Rd.",
      "addressLocality": "Yuba City",
      "addressRegion": "CA",
      "postalCode": "95993",
      "addressCountry": "US"
    }},
    "email": "{EMAIL}",
    "sameAs": ["{INSTAGRAM}"]
  }}
  </script>
</head>
<body class="{body_class}">
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="js/site.js?v={ASSET_VERSION}" defer></script>
</body>
</html>
"""


# Reusable section fragments -------------------------------------------------

def page_hero(kicker, heading, lead, aside_title="", aside_body="", breadcrumb=""):
    crumbs = ""
    if breadcrumb:
        crumbs = f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span>/</span> <span aria-current="page">{breadcrumb}</span></nav>'
    aside = ""
    if aside_title:
        aside = f'<div class="page-hero-aside"><strong>{aside_title}</strong><p>{aside_body}</p></div>'
    return f"""<section class="page-hero">
  <div class="container">
    {crumbs}
    <div class="page-hero-grid">
      <div>
        <p class="kicker">{kicker}</p>
        <h1>{heading}</h1>
        <p class="lead">{lead}</p>
      </div>
      {aside}
    </div>
  </div>
</section>"""


def cta_band(heading, text, primary_href="join.html", primary_label="Join the club", secondary_href="sponsors.html#tiers", secondary_label="Sponsor the team"):
    return f"""<section class="cta-band">
  <div class="container cta-band-inner">
    <div>
      <p class="kicker">Get involved</p>
      <h2>{heading}</h2>
      <p>{text}</p>
    </div>
    <div class="cta-band-actions">
      <a class="btn btn--primary" href="{primary_href}">{primary_label} {icon("arrow", "btn-arrow")}</a>
      <a class="btn btn--ghost" href="{secondary_href}">{secondary_label}</a>
    </div>
  </div>
</section>"""


def sponsor_cta():
    return f"""<section class="section section--paper">
  <div class="container">
    <div class="sponsor-cta reveal">
      <div>
        <p class="kicker">Sponsorship</p>
        <h2>Help us buy parts.</h2>
        <p>Motors, batteries, filament, entry fees, and tools add up. Local sponsors cover the difference and can get their name on the robot, the shirts, and the site.</p>
        <div class="tag-row" style="margin-top:1.2rem">
          <span class="tag tag--dark">$100 Supporter</span>
          <span class="tag tag--dark">$250 Partner</span>
          <span class="tag tag--dark">$500 Builder</span>
          <span class="tag tag--dark">$1,000 Champion</span>
        </div>
      </div>
      <div class="sponsor-cta-actions">
        <a class="btn btn--dark" href="sponsors.html#tiers">See the levels {icon("arrow", "btn-arrow")}</a>
        <a class="btn btn--ghost" href="assets/RVRobotics-Sponsorship-Packet.pdf">Sponsor packet</a>
      </div>
    </div>
  </div>
</section>"""
