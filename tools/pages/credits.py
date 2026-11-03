"""Photo credits / licensing page."""
from rvsite import page_hero, INSTAGRAM, INSTAGRAM_HANDLE

TITLE = "Photo credits | River Valley Robotics"
DESCRIPTION = "Photography, illustration, and font credits for the River Valley Robotics website."
ACTIVE = ""
FILENAME = "credits.html"

BODY = f"""
<section class="page-hero">
  <div class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Home</a> <span>/</span> <span aria-current="page">Photo credits</span></nav>
    <div class="page-hero-grid">
      <div>
        <p class="kicker">Credits</p>
        <h1>Where the images<br>come from.</h1>
        <p class="lead">The site uses the team's own photos and flyers from Instagram, plus original graphics made for this site.</p>
      </div>
      <div class="page-hero-aside">
        <strong>Team archive</strong>
        <p>Send new photos to <a href="mailto:rvrobotics@ycusd.org" style="color:var(--gold)">rvrobotics@ycusd.org</a> or tag us on Instagram.</p>
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
        <dt>The shop</dt>
        <dd>Workbench, tools, and current build in Room 408. <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</dd>
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

    <h3 style="margin-top:3rem">Fonts &amp; illustration</h3>
    <div class="info-list" style="margin-top:1rem">
      <div class="info-row">
        <dt>Typefaces</dt>
        <dd><strong>Barlow Condensed</strong> and <strong>Inter</strong>, licensed under the <a href="https://openfontlicense.org/" target="_blank" rel="noopener">SIL Open Font License 1.1</a>. Self-hosted for performance and privacy.</dd>
      </div>
      <div class="info-row">
        <dt>Illustrations</dt>
        <dd>Brand mark, icons, the robot concept drawing, and page graphics are original SVG work created for this site.</dd>
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
