"""Build page."""
from rvsite import icon, page_hero, cta_band, INSTAGRAM, INSTAGRAM_HANDLE

TITLE = "The build | River Valley Robotics"
DESCRIPTION = "What River Valley Robotics is building this season: a 3D-printed combat robot with a drum, four wheels, and a lot of test fits."
ACTIVE = "robots"
FILENAME = "robots.html"

BODY = f"""
{page_hero(
    "The build",
    "The robot<br>in Room 408.",
    "We're in the second year of the club. The current robot is a 3D-printed combat bot with a drum, four wheels, and a lot of test fits. Here's what's done and what's still changing.",
    "2026&ndash;27 build",
    f"In progress.<br>Match dates will be posted on <a href=\"{INSTAGRAM}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent)\">{INSTAGRAM_HANDLE}</a>.",
    "Build",
)}

<section class="section section--paper" aria-labelledby="current">
  <div class="container">
    <div class="feature-split feature-split--top">
      <figure class="feature-media feature-media--portrait reveal" style="margin:0">
        <img src="assets/img/cad-chassis-top.webp" width="1000" height="1250" alt="CAD model of the team's combat robot with the top plate on" loading="lazy">
        <figcaption class="media-tag">CAD &middot; current revision</figcaption>
      </figure>
      <div class="reveal" style="--d:100ms">
        <p class="kicker">Current build</p>
        <h2 id="current">Printed, wired,<br>and still changing.</h2>
        <p class="lead" style="margin-top:1.4rem">The robot is built around a 3D-printed chassis with a black drum, four blue wheels, and removable white armor. It fits in your hands, which makes it easy to carry to the test table and easy to take apart when something breaks.</p>
        <div class="spec-grid spec-grid--light">
          <div class="spec"><dt>Chassis</dt><dd>3D-printed</dd></div>
          <div class="spec"><dt>Drive</dt><dd>Four wheels</dd></div>
          <div class="spec"><dt>Weapon</dt><dd>Drum</dd></div>
          <div class="spec"><dt>Armor</dt><dd>Replaceable</dd></div>
          <div class="spec"><dt>Control</dt><dd>Student-built</dd></div>
          <div class="spec"><dt>Status</dt><dd>In progress</dd></div>
        </div>
        <p class="small muted" style="margin-top:1rem">Some of this will change before the next match. That's the point.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="process">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">How it gets built</p>
        <h2 id="process">Design, print,<br>wire, test.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Most of the work happens in small loops. A part gets modeled, printed, checked, and changed again.</p>
      </div>
    </div>
    <div class="grid-3">
      <article class="card reveal">
        <div class="card-icon">{icon("gear")}</div>
        <h3>Start in CAD</h3>
        <p>Model the part, print a prototype, and check the fit before committing to a final version.</p>
      </article>
      <article class="card reveal" style="--d:70ms">
        <div class="card-icon">{icon("bolt")}</div>
        <h3>Wire it</h3>
        <p>Solder the electronics, route the wiring, and test one system at a time.</p>
      </article>
      <article class="card reveal" style="--d:140ms">
        <div class="card-icon">{icon("wrench")}</div>
        <h3>Drive it</h3>
        <p>Practice, find the weak point, print a new part, and go again.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="photos">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">On the bench</p>
        <h2 id="photos">Build photos.</h2>
      </div>
      <a class="text-link" href="gallery.html">See the gallery {icon("arrow")}</a>
    </div>
    <div class="photo-grid">
      <a href="gallery.html"><img src="assets/img/cad-chassis.webp" width="1000" height="1250" alt="CAD model of the robot chassis without the top plate" loading="lazy"><span>CAD</span></a>
      <a href="gallery.html"><img src="assets/img/chassis-electronics.webp" width="1000" height="1250" alt="A printed robot chassis with the electronics test-fit inside" loading="lazy"><span>Test fit</span></a>
      <a href="gallery.html"><img src="assets/img/soldering-arm.webp" width="1000" height="1250" alt="A student soldering a wire on a printed robot arm" loading="lazy"><span>Wiring</span></a>
      <a href="gallery.html"><img src="assets/img/robot-floor.webp" width="1000" height="1250" alt="The assembled combat robot on a shop floor" loading="lazy"><span>Assembled</span></a>
    </div>
  </div>
</section>

<section class="section section--white" aria-label="Shop rules and next steps">
  <div class="container">
    <div class="grid-2">
      <article class="card reveal">
        <div class="card-icon">{icon("shield")}</div>
        <h3>Shop rules</h3>
        <p>Safety glasses on. Training before tools. No powered tests without a check. The robot can wait; nobody gets hurt.</p>
      </article>
      <article class="card reveal" style="--d:100ms">
        <div class="card-icon">{icon("calendar")}</div>
        <h3 id="next">What's next</h3>
        <ul>
          <li>Finish the wiring and clean up the electronics.</li>
          <li>Test drive and tune the controls.</li>
          <li>Enter our next event and post the date on Instagram.</li>
        </ul>
      </article>
    </div>
  </div>
</section>

{cta_band(
    "Help us finish the build.",
    "Parts, tools, and entry fees all cost money. Sponsors make the season possible and can get their name on something students built.",
    "sponsors.html#tiers",
    "Sponsor the team",
    "contact.html",
    "Ask a question",
)}
"""
