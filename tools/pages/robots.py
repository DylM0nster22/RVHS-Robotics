"""Robots page."""
from rvsite import icon, page_hero, blueprint, cta_band

TITLE = "Our robots | River Valley Robotics"
DESCRIPTION = "How River Valley Robotics designs, builds, wires, programs, and tests a combat robot — plus what happens on match day at a competition."
ACTIVE = "robots"
FILENAME = "robots.html"

BLUEPRINT = blueprint()

BODY = f"""
{page_hero(
    "Our robots",
    "Built to take a hit.",
    "Combat robots have to do two things: hit hard and stay alive. Here's how the team turns a rulebook into a machine.",
    "2026&ndash;27 build",
    "Concept &rarr; prototype &rarr; arena.<br>Student-designed. Student-built.",
    "Robots",
)}

<section class="section section--dark section--grid" aria-labelledby="one-robot">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        {BLUEPRINT}
      </div>
      <div class="reveal" style="--d:100ms">
        <p class="kicker">The build</p>
        <h2 id="one-robot">One robot.<br>Many hands.</h2>
        <p class="lead" style="margin-top:1.4rem">The team starts with the competition rules and works backward. What must the robot do? What can we realistically build? What can we test before it matters?</p>
        <p>Mechanical, electrical, and software work in parallel, then collide in the best way: the first full-system test. From there, every practice run exposes something new to fix.</p>
        <div class="spec-grid">
          <div class="spec"><dt>Drivetrain</dt><dd>Student-designed</dd></div>
          <div class="spec"><dt>Weapon</dt><dd>Student-built</dd></div>
          <div class="spec"><dt>Armor</dt><dd>Replaceable</dd></div>
          <div class="spec"><dt>Controls</dt><dd>Student-coded</dd></div>
          <div class="spec"><dt>Build crew</dt><dd>Grades 9&ndash;12</dd></div>
          <div class="spec"><dt>Season</dt><dd>2026&ndash;27 build</dd></div>
        </div>
        <p class="photo-credit">Concept drawing &mdash; final robot details are revealed after the build.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="inside">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Inside the robot</p>
        <h2 id="inside">Four systems,<br>one machine.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Every subsystem has a student owner and a backup. That way, the team can diagnose a problem without waiting for one person.</p>
      </div>
    </div>
    <div class="grid-4">
      <article class="card reveal">
        <span class="card-number">01</span>
        <div class="card-icon">{icon("gear")}</div>
        <h3>Drivetrain</h3>
        <p>The frame, wheels, gearboxes, and motors that get the robot where it needs to go.</p>
        <ul>
          <li>Chassis &amp; weight</li>
          <li>Gearing &amp; traction</li>
          <li>Serviceability</li>
        </ul>
      </article>
      <article class="card reveal" style="--d:70ms">
        <span class="card-number">02</span>
        <div class="card-icon">{icon("wrench")}</div>
        <h3>Weapon</h3>
        <p>The system that does the damage &mdash; and the mounts that keep it attached to the robot.</p>
        <ul>
          <li>Motor &amp; power budget</li>
          <li>Weapon mounts</li>
          <li>Test &amp; tune</li>
        </ul>
      </article>
      <article class="card reveal" style="--d:140ms">
        <span class="card-number">03</span>
        <div class="card-icon">{icon("chip")}</div>
        <h3>Control</h3>
        <p>Batteries, switches, wiring, and the code that turns driver input into motion.</p>
        <ul>
          <li>Power distribution</li>
          <li>Motor mixing</li>
          <li>Driver controls</li>
        </ul>
      </article>
      <article class="card reveal" style="--d:210ms">
        <span class="card-number">04</span>
        <div class="card-icon">{icon("shield")}</div>
        <h3>Armor &amp; pit</h3>
        <p>Armor panels, wedges, spares, and the calm crew that keeps the robot running all day.</p>
        <ul>
          <li>Replaceable armor</li>
          <li>Spare parts kit</li>
          <li>Safety checks</li>
        </ul>
      </article>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="competition">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Match day</p>
        <h2 id="competition">All day<br>on your feet.</h2>
        <p class="lead" style="margin-top:1.4rem">A competition is a build season in miniature: setup, safety checks, quick repairs, and a match clock that doesn't care how tired you are.</p>
        <p>Students run the pit, drive the robot, talk to other teams, and make the calls that keep the bot in the bracket. It is the most stressful and most rewarding part of the year.</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>Pit crew</dt><dd>Repairs, battery swaps, and a parts kit that is actually organized</dd></div>
          <div class="info-row"><dt>Drive team</dt><dd>Practice, communication, and a plan for every match</dd></div>
          <div class="info-row"><dt>Safety</dt><dd>Weapons checked, batteries handled correctly, and a clean pit</dd></div>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <figure class="feature-media" style="margin:0">
          <img src="assets/img/team-shop-portrait.webp" width="1000" height="1250" alt="The River Valley Robotics workbench with tools, electronics, and 3D-printed robot parts" loading="lazy">
          <figcaption class="media-tag">In the shop</figcaption>
        </figure>
        <div class="callout callout--light" style="margin-top:1.25rem">
          The robot is never finished. It is only ready for the next match.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest" aria-labelledby="safety">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Safety first</p>
        <h2 id="safety">Everybody home<br>in one piece.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Combat robotics involves real tools, real batteries, and real deadlines. Safety is the one part of the build that is never optional.</p>
      </div>
    </div>
    <div class="grid-3">
      <div class="card reveal">
        <div class="card-icon">{icon("shield")}</div>
        <h3>Before you touch a tool</h3>
        <p>Training first, safety glasses always, and a mentor sign-off before students use shop equipment.</p>
      </div>
      <div class="card reveal" style="--d:80ms">
        <div class="card-icon">{icon("bolt")}</div>
        <h3>Respect the power</h3>
        <p>Battery safety, proper fusing, and never working alone on a live system.</p>
      </div>
      <div class="card reveal" style="--d:160ms">
        <div class="card-icon">{icon("check")}</div>
        <h3>Check, then check again</h3>
        <p>Pre-match checklists, a clean pit, and the discipline to stop when something is not right.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="archive">
  <div class="container">
    <div class="feature-split" style="align-items:center">
      <div class="reveal">
        <p class="kicker">Season archive</p>
        <h2 id="archive">The next chapter<br>is being written.</h2>
        <p class="lead" style="margin-top:1.4rem">We're building a proper archive of robots, match results, and build notes. The 2026&ndash;27 season is in progress, and past seasons will be added as the team assembles its records.</p>
        <p>Want to help document the team? Photos, video, CAD exports, and build notes are always welcome.</p>
        <div style="margin-top:1.5rem">
          <a class="btn btn--dark" href="join.html">Join the team {icon("arrow", "btn-arrow")}</a>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="info-list">
          <div class="info-row"><dt>2026&ndash;27</dt><dd>Concept &amp; build &mdash; in progress</dd></div>
          <div class="info-row"><dt>Next reveal</dt><dd>After the build</dd></div>
          <div class="info-row"><dt>Archive</dt><dd>Past seasons coming soon</dd></div>
        </div>
        <p class="photo-credit">Have an old team photo or result to add? <a href="contact.html">Send it our way</a>.</p>
      </div>
    </div>
  </div>
</section>

{cta_band(
    "Help us build the next one.",
    "Parts, tools, and travel all cost money. Sponsors make the season possible — and get their name on something students built.",
    "sponsors.html#tiers",
    "Sponsor the team",
    "contact.html",
    "Ask a question",
)}
"""
