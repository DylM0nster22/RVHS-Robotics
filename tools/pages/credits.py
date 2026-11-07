"""Credits / licensing page."""
from rvsite import page_hero, INSTAGRAM, INSTAGRAM_HANDLE, YOUTUBE, YOUTUBE_HANDLE

TITLE = "Credits | River Valley Robotics"
DESCRIPTION = "Photography, CAD model, illustration, font, and software credits for the River Valley Robotics website."
ACTIVE = ""
FILENAME = "credits.html"

BODY = f"""
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span>/</span> <span aria-current="page">Credits</span></nav>
    <div class="page-hero-grid">
      <div>
        <p class="kicker">Credits</p>
        <h1>Where it all<br>comes from.</h1>
        <p class="lead">The site uses the team's own photos and flyers from Instagram, match video, public CAD models, plus original graphics made for this site.</p>
      </div>
      <div class="page-hero-aside">
        <strong>Team archive</strong>
        <p>Send new photos to <a href="mailto:rvrobotics@ycusd.org" style="color:var(--accent)">rvrobotics@ycusd.org</a> or tag us on Instagram.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Photography</p>
        <h2>Team images.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">All photographs and flyers on this site come from the team's Instagram account and are used with the team's permission.</p>
      </div>
    </div>
    <div class="info-list">
      <div class="info-row">
        <dt>The shop and build</dt>
        <dd>Workbench, CAD, electronics, soldering, and the assembled robot in Room 408. <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</dd>
      </div>
      <div class="info-row">
        <dt>First meeting</dt>
        <dd>Club meeting flyer from the 2025&ndash;26 season. <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</dd>
      </div>
      <div class="info-row">
        <dt>Club update</dt>
        <dd>Meeting and events update for the 2026&ndash;27 season. <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</dd>
      </div>
      <div class="info-row">
        <dt>Team logo</dt>
        <dd>Official River Valley Robotics falcon logo, provided by the team.</dd>
      </div>
      <div class="info-row">
        <dt>School logo</dt>
        <dd>River Valley High School Falcons logo. Property of River Valley High School / Yuba City Unified School District, used here to identify the team's school.</dd>
      </div>
    </div>

    <h3 style="margin-top:3rem">Match video</h3>
    <div class="info-list" style="margin-top:1rem">
      <div class="info-row">
        <dt>Impact Robotics League #1</dt>
        <dd>Overhead match footage from the 2026 event. Event overlays, logos, and sponsor marks belong to Impact Robotics League and its sponsors.</dd>
      </div>
      <div class="info-row">
        <dt>YouTube picks</dt>
        <dd>Newer match videos and thumbnails from the <a href="{YOUTUBE}" target="_blank" rel="noopener">{YOUTUBE_HANDLE}</a> channel. These play through YouTube's privacy-enhanced embed; the site does not host copies.</dd>
      </div>
    </div>

    <h3 style="margin-top:3rem">3D CAD models</h3>
    <div class="info-list" style="margin-top:1rem">
      <div class="info-row">
        <dt>Model sources</dt>
        <dd>The <a href="cad.html">CAD lab</a> uses STEP files from <a href="https://github.com/DylM0nster22" target="_blank" rel="noopener">DylM0nster22's public GitHub repositories</a> and work by the listed collaborators. Models remain the work of their authors; check each repository for license terms before reusing geometry or design files.</dd>
      </div>
      <div class="info-row">
        <dt>Viewer</dt>
        <dd>Three.js and the meshoptimizer decoder, both MIT licensed and self-hosted. Card thumbnails were rendered from the CAD files for this site.</dd>
      </div>
    </div>

    <h3 style="margin-top:3rem">Fonts &amp; graphics</h3>
    <div class="info-list" style="margin-top:1rem">
      <div class="info-row">
        <dt>Typefaces</dt>
        <dd><strong>Barlow Condensed</strong> and <strong>Inter</strong>, licensed under the <a href="https://openfontlicense.org/" target="_blank" rel="noopener">SIL Open Font License 1.1</a>. Self-hosted for performance and privacy.</dd>
      </div>
      <div class="info-row">
        <dt>Graphics</dt>
        <dd>Brand mark, icons, and page graphics are original work created for this site.</dd>
      </div>
      <div class="info-row">
        <dt>Questions</dt>
        <dd>Believe an image is credited incorrectly? <a href="contact.html">Contact the team</a> and we'll fix it.</dd>
      </div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="callout callout--light">
      Have new team photos? Send them to <a href="mailto:rvrobotics@ycusd.org">rvrobotics@ycusd.org</a>. We prefer wide, well-lit shots of students working, the robot in progress, and match day.
    </div>
  </div>
</section>
"""
