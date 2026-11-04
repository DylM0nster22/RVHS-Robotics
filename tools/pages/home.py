"""Home page."""
from rvsite import icon, sponsor_cta, cta_band, INSTAGRAM, INSTAGRAM_HANDLE

TITLE = "River Valley Robotics | Combat robotics at River Valley High School"
DESCRIPTION = "River Valley Robotics is a student club at River Valley High School in Yuba City, California. We meet Thursdays and Fridays in Room 408 to design, build, and drive combat robots."
ACTIVE = "home"
FILENAME = "index.html"

BODY = f"""
<section class="hero">
  <div class="hero-media" aria-hidden="true">
    <img src="assets/img/team-shop-hero.webp" width="1400" height="933" alt="" fetchpriority="high">
  </div>
  <div class="container hero-inner">
    <div class="hero-main">
      <p class="hero-eyebrow"><span class="dot" aria-hidden="true"></span> River Valley High School &middot; Yuba City, CA</p>
      <h1>
        <span class="line">We build</span>
        <span class="line accent">combat robots.</span>
      </h1>
      <p class="hero-sub">River Valley Robotics is a student club at River Valley High School. We meet in Room 408 to design, build, and drive small combat robots. You don't need experience to start.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="robots.html">See the build {icon("arrow", "btn-arrow")}</a>
        <a class="btn btn--ghost" href="sponsors.html#tiers">Sponsor the team</a>
      </div>
    </div>
    <aside class="hero-aside" aria-label="Meetings and location">
      <div class="hero-aside-label"><span>2026&ndash;27</span><i aria-hidden="true"></i></div>
      <dl>
        <div><dt>Meets</dt><dd>Thu &amp; Fri</dd></div>
        <div><dt>Room</dt><dd>408</dd></div>
        <div><dt>Open to</dt><dd>Grades 9&ndash;12</dd></div>
        <div><dt>Experience</dt><dd>None needed</dd></div>
      </dl>
    </aside>
  </div>
</section>

<section class="section section--paper section--grid-light" aria-labelledby="what">
  <div class="container">
    <div class="feature-split">
      <div class="reveal">
        <p class="kicker">What we do</p>
        <h2 id="what">The whole build.</h2>
        <p class="lead" style="margin-top:1.4rem">Students handle the CAD, the 3D printing, the wiring, and the driving. We learn the tools as we need them, then fix what breaks.</p>
        <p>This is our second year as a club. The robot is small, the shop is one room, and the chassis and armor were designed and printed by students.</p>
        <a class="text-link" href="about.html">About the club {icon("arrow")}</a>
      </div>
      <figure class="feature-media reveal" style="--d:100ms; margin:0">
        <img src="assets/img/students-workshop-wide.webp" width="1200" height="900" alt="Two River Valley Robotics students at a workbench with a soldering iron and robot parts" loading="lazy">
        <figcaption class="media-tag">Room 408</figcaption>
      </figure>
    </div>
    <div class="grid-3" style="margin-top:clamp(2rem,4vw,3rem)">
      <article class="card reveal">
        <div class="card-icon">{icon("gear")}</div>
        <h3>Design</h3>
        <p>Model the chassis, weapon, and armor in CAD, then print a version you can hold.</p>
      </article>
      <article class="card reveal" style="--d:70ms">
        <div class="card-icon">{icon("bolt")}</div>
        <h3>Build</h3>
        <p>Solder the electronics, assemble the drive, and test-fit the parts until they stop fighting each other.</p>
      </article>
      <article class="card reveal" style="--d:140ms">
        <div class="card-icon">{icon("trophy")}</div>
        <h3>Compete</h3>
        <p>Practice driving, make repairs, and take the robot to competition. Dates go on Instagram.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="shop">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">From the shop</p>
        <h2 id="shop">What it looks like.</h2>
      </div>
      <a class="text-link" href="gallery.html">All photos {icon("arrow")}</a>
    </div>
    <div class="photo-grid">
      <a href="gallery.html"><img src="assets/img/robot-floor.webp" width="1000" height="1250" alt="The assembled combat robot on a shop floor" loading="lazy"><span>The robot</span></a>
      <a href="gallery.html"><img src="assets/img/cad-chassis-top.webp" width="1000" height="1250" alt="CAD model of the robot chassis with the top plate on" loading="lazy"><span>CAD</span></a>
      <a href="gallery.html"><img src="assets/img/soldering-arm.webp" width="1000" height="1250" alt="A student soldering a wire on a printed robot arm" loading="lazy"><span>Wiring</span></a>
      <a href="gallery.html"><img src="assets/img/team-shop.webp" width="1100" height="1100" alt="The team's workbench in Room 408 with tools and robot parts" loading="lazy"><span>The shop</span></a>
    </div>
    <p class="photo-credit">Photos from the team's Instagram, <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</p>
  </div>
</section>

{sponsor_cta()}

{cta_band(
    "Come to a meeting.",
    "Room 408. Grades 9&ndash;12. No experience needed. See what we're working on.",
    "join.html",
    "How to join",
    "contact.html",
    "Ask a question",
)}
"""
