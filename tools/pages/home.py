"""Home page."""
from rvsite import icon, stat_block, sponsor_cta, cta_band, blueprint, INSTAGRAM, INSTAGRAM_HANDLE

TITLE = "River Valley Robotics | Combat robotics at River Valley High School"
DESCRIPTION = "River Valley Robotics is the student combat robotics club at River Valley High School in Yuba City, California. We design, build, and drive fighting robots — and we're looking for sponsors and new teammates."
ACTIVE = "home"
FILENAME = "index.html"

BLUEPRINT = blueprint()

BODY = f"""
<section class="hero">
  <div class="hero-media" aria-hidden="true">
    <img src="assets/img/team-shop-hero.webp" width="1400" height="933" alt="" fetchpriority="high">
  </div>
  <div class="container hero-inner">
    <div class="hero-main">
      <p class="hero-eyebrow"><span class="dot" aria-hidden="true"></span> Student-led combat robotics &middot; River Valley High School</p>
      <h1>
        <span class="line">Build.</span>
        <span class="line outline">Code.</span>
        <span class="line gold">Compete.</span>
      </h1>
      <p class="hero-sub">We're a student combat robotics team in Yuba City &mdash; designing, building, and driving machines that have to survive the arena.</p>
      <div class="hero-actions">
        <a class="btn btn--primary" href="sponsors.html#tiers">Sponsor the team {icon("arrow", "btn-arrow")}</a>
        <a class="btn btn--ghost" href="about.html">Explore the team</a>
      </div>
    </div>
    <aside class="hero-aside" aria-label="Team at a glance">
      <div class="hero-aside-label"><span>2026&ndash;27 season</span><i aria-hidden="true"></i></div>
      <dl>
        <div><dt>Program</dt><dd>Combat robotics</dd></div>
        <div><dt>Meets</dt><dd>Thu &amp; Fri</dd></div>
        <div><dt>Room</dt><dd>408</dd></div>
        <div><dt>Open to</dt><dd>Grades 9&ndash;12</dd></div>
      </dl>
    </aside>
  </div>
  <div class="container">
    <div class="hero-meta">
      <div class="hero-meta-item">{icon("users")} Student-led, student-built</div>
      <div class="hero-meta-item">{icon("spark")} No experience required</div>
      <div class="hero-meta-item">{icon("pin")} Second season &middot; building momentum</div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true">
  <div class="marquee-track">
    <div class="marquee-group">
      <span>Design</span><span>Fabricate</span><span>Program</span><span>Test</span><span>Compete</span><span>Give back</span>
    </div>
    <div class="marquee-group">
      <span>Design</span><span>Fabricate</span><span>Program</span><span>Test</span><span>Compete</span><span>Give back</span>
    </div>
  </div>
</div>

<section class="section section--paper section--grid-light" aria-labelledby="who-we-are">
  <div class="container">
    <div class="feature-split">
      <div class="reveal">
        <p class="kicker">Who we are</p>
        <h2 id="who-we-are">More than<br>a robot.</h2>
        <p class="lead" style="margin-top:1.4rem">River Valley Robotics is the combat robotics club at River Valley High School. In our second year, students take an idea from a sketch to a machine that can take a hit &mdash; designing the frame, printing parts, wiring electronics, and learning to fix what breaks.</p>
        <p>We're here for the students who like to know how things work, and for the ones who are still figuring that out. No prior experience needed. What matters is showing up, asking questions, and being willing to try again.</p>
        <div class="tag-row" style="margin:1.4rem 0 1.5rem">
          <span class="tag tag--gold">Combat robotics</span>
          <span class="tag">Student-led</span>
          <span class="tag">All skill levels</span>
        </div>
        <a class="text-link" href="about.html">About the team {icon("arrow")}</a>
      </div>
      <figure class="feature-media reveal" style="--d:100ms; margin:0">
        <img src="assets/img/team-shop.webp" width="1100" height="1100" alt="The team's workbench in Room 408, crowded with tools, 3D-printed robot parts, and electronics" loading="lazy">
        <figcaption class="media-tag">The shop &middot; Room 408</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="stats" aria-label="Team at a glance">
  <div class="container">
    <div class="stats-grid">
      {stat_block(2, "", "Season of club robotics")}
      {stat_block(408, "", "Our shop")}
      <div class="stat reveal">
        <div class="stat-value">9<span class="suffix">&ndash;12</span></div>
        <div class="stat-label">Grades welcome</div>
      </div>
      {stat_block(0, "", "Experience needed")}
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="what-we-do">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">What we do</p>
        <h2 id="what-we-do">Every part of the build.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">A combat robot is a team project. Students choose a subteam, learn the tools, and own a real piece of the machine &mdash; or help tell its story.</p>
      </div>
    </div>
    <div class="grid-4">
      <article class="card reveal">
        <span class="card-number">01</span>
        <div class="card-icon">{icon("gear")}</div>
        <h3>Mechanical</h3>
        <p>Build a frame, armor, and weapon mounts that can take a hit.</p>
        <ul>
          <li>CAD &amp; prototyping</li>
          <li>Drills, saws, 3D printers</li>
          <li>Armor &amp; assembly</li>
        </ul>
      </article>
      <article class="card reveal" style="--d:80ms">
        <span class="card-number">02</span>
        <div class="card-icon">{icon("bolt")}</div>
        <h3>Electrical</h3>
        <p>Power, wiring, and motor control that keep the robot moving.</p>
        <ul>
          <li>Motors &amp; speed controllers</li>
          <li>Battery &amp; power</li>
          <li>Wiring &amp; troubleshooting</li>
        </ul>
      </article>
      <article class="card reveal" style="--d:160ms">
        <span class="card-number">03</span>
        <div class="card-icon">{icon("code")}</div>
        <h3>Software &amp; drive</h3>
        <p>Make the machine move exactly how the driver expects, every match.</p>
        <ul>
          <li>Robot controls</li>
          <li>Match strategy</li>
          <li>Testing &amp; practice</li>
        </ul>
      </article>
      <article class="card reveal" style="--d:240ms">
        <span class="card-number">04</span>
        <div class="card-icon">{icon("megaphone")}</div>
        <h3>Business &amp; outreach</h3>
        <p>Keep the team funded, organized, and connected to the community.</p>
        <ul>
          <li>Sponsorships &amp; grants</li>
          <li>Social media &amp; media</li>
          <li>Events &amp; STEM outreach</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark section--grid" aria-labelledby="season">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">How a season works</p>
        <h2 id="season">From idea<br>to the arena.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">The calendar changes every year, but the rhythm is the same: learn the rules, design hard, build fast, test often, and compete with everything you've got.</p>
      </div>
    </div>
    <div class="process">
      <div class="process-step reveal">
        <span class="process-num">01 / THE CHALLENGE</span>
        <h3>Learn the rules</h3>
        <p>Read the competition rules, study other bots, and decide what the team can build and drive well.</p>
      </div>
      <div class="process-step reveal" style="--d:70ms">
        <span class="process-num">02 / DESIGN</span>
        <h3>Sketch &amp; prototype</h3>
        <p>Trade ideas, build quick mock-ups, and choose a design the whole team can execute.</p>
      </div>
      <div class="process-step reveal" style="--d:140ms">
        <span class="process-num">03 / BUILD</span>
        <h3>Make it real</h3>
        <p>CAD, cut, drill, print, wire, and code. Subteams work in parallel and solve problems together.</p>
      </div>
      <div class="process-step reveal" style="--d:210ms">
        <span class="process-num">04 / TEST</span>
        <h3>Break it, fix it</h3>
        <p>Drive practice, stress tests, and late-night debugging. The robot gets better every run.</p>
      </div>
      <div class="process-step reveal" style="--d:280ms">
        <span class="process-num">05 / COMPETE</span>
        <h3>Take the arena</h3>
        <p>Pass safety, make weight, and compete. Then come home and make the next one better.</p>
      </div>
    </div>
    <div style="margin-top:2.5rem">
      <a class="text-link" href="robots.html">See how we build {icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="machine">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        {BLUEPRINT}
      </div>
      <div class="reveal" style="--d:100ms">
        <p class="kicker">The machine</p>
        <h2 id="machine">Engineered<br>from the frame up.</h2>
        <p class="lead" style="margin-top:1.4rem">Every robot starts as a drawing and a pile of parts. Students own the details: the drivetrain, the weapon, the armor, the wiring, and the checklist that gets it through safety.</p>
        <div class="spec-grid spec-grid--light">
          <div class="spec"><dt>Drivetrain</dt><dd>Student-designed</dd></div>
          <div class="spec"><dt>Weapon system</dt><dd>Student-built</dd></div>
          <div class="spec"><dt>Armor</dt><dd>Replaceable</dd></div>
          <div class="spec"><dt>Controls</dt><dd>Student-coded</dd></div>
          <div class="spec"><dt>Season</dt><dd>2026&ndash;27 build</dd></div>
          <div class="spec"><dt>Safety</dt><dd>Checklist-driven</dd></div>
        </div>
        <div style="margin-top:1.75rem">
          <a class="text-link" href="robots.html">Meet the robot {icon("arrow")}</a>
        </div>
      </div>
    </div>
  </div>
</section>

{sponsor_cta()}

<section class="section section--paper-2" aria-labelledby="gallery-preview">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">From the shop</p>
        <h2 id="gallery-preview">The work looks<br>like this.</h2>
      </div>
      <a class="text-link" href="gallery.html">Open the gallery {icon("arrow")}</a>
    </div>
    <div class="gallery-grid">
      <a class="gallery-item gallery-item--wide" href="gallery.html" aria-label="Open the photo gallery">
        <img src="assets/img/team-shop.webp" width="1100" height="1100" alt="The team's workbench with tools, 3D-printed parts, and electronics" loading="lazy">
        <span class="gallery-caption">The shop &middot; Room 408</span>
        <span class="gallery-zoom" aria-hidden="true">{icon("zoom")}</span>
      </a>
      <a class="gallery-note" href="gallery.html">
        <div>
          <p class="kicker">The gallery</p>
          <h3>Shop progress, flyers, and match days.</h3>
          <p>Follow the build on Instagram at {INSTAGRAM_HANDLE}.</p>
        </div>
        <span class="text-link">See all photos {icon("arrow")}</span>
      </a>
    </div>
    <p class="photo-credit">Photos and flyers from the team's Instagram, <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</p>
  </div>
</section>

{cta_band(
    "There's a place for you on this team.",
    "You don't need to be an engineer yet. You need to be curious, show up, and be willing to learn. Students, parents, and mentors are all part of the build.",
    "join.html",
    "Join the team",
    "join.html#mentors",
    "Become a mentor",
)}
"""
