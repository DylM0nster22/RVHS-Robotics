"""Gallery page."""
from rvsite import icon, page_hero, cta_band, INSTAGRAM, INSTAGRAM_HANDLE

TITLE = "Gallery | River Valley Robotics"
DESCRIPTION = "Photos from River Valley Robotics: the shop, the CAD model, the build, and the first assembled combat robot at River Valley High School in Yuba City."
ACTIVE = "gallery"
FILENAME = "gallery.html"

ITEMS = [
    ("team-shop-portrait", 1000, 1250, "The shop", "Tools, 3D-printed parts, and the current build in Room 408.", "The team's workbench in Room 408 with drills, tools, and robot parts"),
    ("robot-floor", 1000, 1250, "The robot", "The assembled combat robot on the shop floor.", "The assembled combat robot with white armor, blue wheels, and a black drum on a shop floor"),
    ("cad-chassis-top", 1000, 1250, "CAD", "The chassis model with the top plate on.", "CAD model of the robot chassis with the top plate on"),
    ("cad-chassis", 1000, 1250, "CAD, first revision", "The same chassis without the top plate.", "CAD model of the robot chassis without the top plate"),
    ("chassis-electronics", 1000, 1250, "Test fit", "A printed chassis with the electronics inside.", "A printed robot chassis held in a hand with the electronics test-fit inside"),
    ("electronics-bench", 1000, 1250, "Electronics", "Wiring and a printed chassis on the bench.", "A printed robot chassis with wiring and a screwdriver on a workbench"),
    ("soldering-arm", 1000, 1250, "Soldering", "A student soldering a wire on a printed arm.", "A student soldering a wire on a printed robot arm at a workbench"),
    ("soldering-closeup", 1000, 1250, "Power", "A speed controller and battery connector, mid-wire.", "A speed controller and battery connector with wires on a workbench"),
    ("parts-homework", 1000, 1250, "After school", "Robot parts on top of a math assignment.", "Printed robot parts and motors sitting on top of a math assignment"),
    ("armor-part", 1000, 1250, "Armor", "A printed armor piece for the robot.", "A white 3D-printed armor piece for the combat robot"),
    ("meeting-flyer", 1000, 1331, "First meeting", "The flyer for the first meeting, September 2025.", "Flyer for the first robotics meeting on September 22, 2025"),
    ("club-update", 1000, 1333, "Club update", "The 2026&ndash;27 meeting announcement.", "Flyer announcing Thursday and Friday meetings in Room 408"),
]

items_html = ""
for idx, (name, width, height, title, caption, alt) in enumerate(ITEMS):
    items_html += f"""
    <button class="gallery-item gallery-item--tall" type="button" data-full="assets/img/{name}.webp" data-caption="{title} — {caption}" aria-label="View larger: {title}">
      <img src="assets/img/{name}.webp" width="{width}" height="{height}" alt="{alt}" loading="lazy">
      <span class="gallery-caption">{title}</span>
      <span class="gallery-zoom" aria-hidden="true">{icon("zoom")}</span>
    </button>
    """

FEED_LINK = f'Follow <a href="{INSTAGRAM}" target="_blank" rel="noopener" style="color:var(--accent)">{INSTAGRAM_HANDLE}</a> for build updates and match news.'

BODY = f"""
{page_hero(
    "Gallery",
    "From the shop.",
    "Tools on the bench, CAD on the screen, and the first assembled robot. Most of these photos are from the team's Instagram.",
    "The feed",
    FEED_LINK,
    "Gallery",
)}

<section class="section section--paper" aria-labelledby="photos">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">The season in frames</p>
        <h2 id="photos">Inside the build.</h2>
      </div>
      <a class="text-link" href="{INSTAGRAM}" target="_blank" rel="noopener">Follow on Instagram {icon("external")}</a>
    </div>
    <div class="gallery-grid">
      {items_html}
    </div>
    <p class="photo-credit">All photos and flyers from <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>. More will be added as the season goes. Match footage is on the <a href="watch.html">watch page</a>.</p>
  </div>
</section>

<dialog class="lightbox" id="lightbox" aria-labelledby="lightbox-caption">
  <img class="lightbox-img" id="lightbox-img" src="" alt="">
  <div class="lightbox-bar">
    <div>
      <p class="lightbox-caption" id="lightbox-caption"></p>
      <p class="mono-label" id="lightbox-counter" style="color:rgba(255,255,255,.45);margin-top:.25rem"></p>
    </div>
    <div class="lightbox-actions">
      <button class="lightbox-btn" type="button" data-lightbox-prev aria-label="Previous photo">{icon("prev")}</button>
      <button class="lightbox-btn" type="button" data-lightbox-next aria-label="Next photo">{icon("next")}</button>
      <button class="lightbox-btn" type="button" data-lightbox-close aria-label="Close photo viewer">{icon("close")}</button>
    </div>
  </div>
</dialog>

{cta_band(
    "Come see it in person.",
    "Stop by the shop, come to a meeting, or invite us to your business for a demo.",
    "contact.html",
    "Get in touch",
    "sponsors.html#tiers",
    "Sponsor the team",
)}
"""
