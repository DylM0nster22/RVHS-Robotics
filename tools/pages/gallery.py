"""Gallery page."""
from rvsite import icon, page_hero, cta_band, INSTAGRAM, INSTAGRAM_HANDLE

TITLE = "Gallery | River Valley Robotics"
DESCRIPTION = "Photos and flyers from River Valley Robotics: the shop, the build, meeting announcements, and combat robotics at River Valley High School in Yuba City."
ACTIVE = "gallery"
FILENAME = "gallery.html"

ITEMS = [
    ("team-shop-portrait", 1000, 1250, "The shop", "Tools, 3D-printed parts, and the current build in Room 408."),
    ("meeting-flyer", 1000, 1331, "First meeting", "The flyer that started the 2025&ndash;26 season."),
    ("club-update", 1000, 1333, "Club update", "Meetings Thursday and Friday in Room 408."),
]

items_html = ""
for idx, (name, width, height, title, caption) in enumerate(ITEMS):
    items_html += f"""
    <button class="gallery-item gallery-item--tall" type="button" data-full="assets/img/{name}.webp" data-caption="{title} — {caption}" aria-label="View larger: {title}">
      <img src="assets/img/{name}.webp" width="{width}" height="{height}" alt="{caption}" loading="lazy">
      <span class="gallery-caption">{title}</span>
      <span class="gallery-zoom" aria-hidden="true">{icon("zoom")}</span>
    </button>
    """

BODY = f"""
{page_hero(
    "Gallery",
    "From the shop.",
    "Tools on the bench, flyers on the wall, and the first time a build actually works. This is what the club looks like.",
    "The feed",
    f"Follow <a href=\"{INSTAGRAM}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--gold)\">{INSTAGRAM_HANDLE}</a> for build updates and match news.",
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
    <p class="photo-credit">All photos and flyers from <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>. More coming as the season progresses.</p>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="instagram">
  <div class="container">
    <div class="sponsor-cta" style="background:var(--forest);color:var(--white)">
      <div>
        <p class="kicker" style="color:var(--gold)">Follow the build</p>
        <h2 style="color:var(--white)">The latest is on Instagram.</h2>
        <p style="color:rgba(255,255,255,.72)">Build progress, meeting changes, and match-day photos go up first on the team account. Give us a follow and share the build with someone who should be on the team.</p>
        <p class="mono-label" style="color:var(--gold);margin-top:1rem">{INSTAGRAM_HANDLE}</p>
      </div>
      <div class="sponsor-cta-actions">
        <a class="btn btn--primary" href="{INSTAGRAM}" target="_blank" rel="noopener">Open Instagram {icon("external", "btn-arrow")}</a>
      </div>
    </div>
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
    "Want to see it in person?",
    "Stop by the shop, come to a competition, or invite us to your business for a demo. We love showing people what students can build.",
    "contact.html",
    "Get in touch",
    "sponsors.html#tiers",
    "Sponsor the team",
)}
"""
