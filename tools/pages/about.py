"""About page."""
from rvsite import icon, page_hero, cta_band, INSTAGRAM, INSTAGRAM_HANDLE, ROOM, MEETINGS, CLASSROOM

TITLE = "About the club | River Valley Robotics"
DESCRIPTION = "River Valley Robotics is a student club at River Valley High School in Yuba City, California. Learn how the club started, what students do, and when we meet."
ACTIVE = "about"
FILENAME = "about.html"

BODY = f"""
{page_hero(
    "About",
    "A small club<br>with a full build.",
    "River Valley Robotics started in fall 2025. We're a student club at River Valley High School, and this is our second year.",
    "At a glance",
    f"Meets {MEETINGS} &middot; {ROOM}<br>Grades 9&ndash;12<br>No experience needed",
    "About",
)}

<section class="section section--paper" aria-labelledby="story">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">The short version</p>
        <h2 id="story">We started<br>in fall 2025.</h2>
        <p class="lead" style="margin-top:1.4rem">The club began with a first meeting in September 2025 and a simple goal: build a combat robot and learn what it takes to keep it running.</p>
        <p>This year we're doing it again with a new robot. Students design parts in CAD, print and assemble them, wire the electronics, and test the robot until it does what we want. On a small team, everyone ends up helping with more than one job.</p>
        <p>We meet Thursdays and Fridays in Room 408. Announcements go out through Google Classroom (code <strong>{CLASSROOM}</strong>) and <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</p>
        <div class="tag-row" style="margin-top:1.5rem">
          <span class="tag tag--accent">Combat robotics</span>
          <span class="tag">Second season</span>
          <span class="tag">Grades 9&ndash;12</span>
        </div>
      </div>
      <figure class="feature-media feature-media--portrait reveal" style="--d:100ms; margin:0">
        <img src="assets/img/students-workshop.webp" width="1000" height="1250" alt="Two River Valley Robotics students at a workbench with a soldering iron and robot parts" loading="lazy">
        <figcaption class="media-tag">After a build session</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="work">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">What we do</p>
        <h2 id="work">Four kinds of work.<br>One robot.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Pick a part of the build that sounds interesting. You can try a few things before you settle on one.</p>
      </div>
    </div>
    <div class="role-grid role-grid--four">
      <article class="role reveal">
        <span class="role-tag">Design</span>
        <h3>CAD &amp; parts</h3>
        <p>Model the chassis, weapon, and armor. Print prototypes and fix what doesn't fit.</p>
      </article>
      <article class="role reveal" style="--d:60ms">
        <span class="role-tag">Build</span>
        <h3>Shop &amp; assembly</h3>
        <p>Drill, tap, print, and assemble. Learn the tools and keep the robot in one piece.</p>
      </article>
      <article class="role reveal" style="--d:120ms">
        <span class="role-tag">Wiring</span>
        <h3>Electronics &amp; code</h3>
        <p>Solder the speed controllers, route the wiring, and get the motors moving in the right direction.</p>
      </article>
      <article class="role reveal" style="--d:180ms">
        <span class="role-tag">Drive</span>
        <h3>Testing &amp; repairs</h3>
        <p>Practice driving, find the weak points, and fix them before the next match.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="meetings">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Meetings</p>
        <h2 id="meetings">Find us in<br>Room 408.</h2>
        <p class="lead" style="margin-top:1.4rem">We meet Thursdays and Fridays. Come to a meeting, or email first if you want to check the schedule.</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>When</dt><dd>{MEETINGS}</dd></div>
          <div class="info-row"><dt>Where</dt><dd>{ROOM}, River Valley High School</dd></div>
          <div class="info-row"><dt>Who</dt><dd>RVHS students in grades 9&ndash;12</dd></div>
          <div class="info-row"><dt>Classroom</dt><dd>Google Classroom code <strong>{CLASSROOM}</strong></dd></div>
          <div class="info-row"><dt>Instagram</dt><dd><a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a></dd></div>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="callout callout--light">
          New members are welcome. You don't need to know how to solder, code, or use CAD. We'll show you.
        </div>
        <div style="margin-top:1.5rem">
          <a class="btn btn--dark" href="join.html">Join the club {icon("arrow", "btn-arrow")}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="faq">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Questions</p>
        <h2 id="faq">Good to know.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Still curious? Email <a href="mailto:rvrobotics@ycusd.org">rvrobotics@ycusd.org</a> or come find us in {ROOM}.</p>
      </div>
    </div>
    <div class="faq">
      <details>
        <summary>What is combat robotics?</summary>
        <p>Combat robotics is a category of robot competition where students build small, remote-controlled machines that compete in matches. The robots have to follow a set of safety and build rules, and the goal is to disable or outlast the other robot.</p>
      </details>
      <details>
        <summary>Do I need robotics experience to join?</summary>
        <p>No. Most of the skills are learned in the shop. We teach the tools, the software, and the safety rules from the beginning. Curiosity and showing up matter more than experience.</p>
      </details>
      <details>
        <summary>Who can join?</summary>
        <p>River Valley High School students in grades 9 through 12. Parents, alumni, and community members can help as mentors and volunteers.</p>
      </details>
      <details>
        <summary>When do you meet?</summary>
        <p>{MEETINGS} in {ROOM}. Check Google Classroom (code <strong>{CLASSROOM}</strong>) or the team Instagram for schedule changes, especially around competitions.</p>
      </details>
      <details>
        <summary>Does it cost anything?</summary>
        <p>Ask us about current team fees and materials costs. We don't want cost to be the reason someone doesn't join, and we can talk through options with families.</p>
      </details>
    </div>
  </div>
</section>

{cta_band(
    "Come see the shop.",
    "The easiest way to find out if the club is for you is to stop by a meeting. We'll show you what we're working on.",
    "join.html",
    "Join the club",
    "contact.html",
    "Ask a question",
)}
"""
