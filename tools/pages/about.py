"""About page."""
from rvsite import icon, page_hero, cta_band, INSTAGRAM, INSTAGRAM_HANDLE, ROOM, MEETINGS

TITLE = "About the team | River Valley Robotics"
DESCRIPTION = "Meet River Valley Robotics: a student-led combat robotics club at River Valley High School in Yuba City, California. Learn how the team works, what we value, and how to get involved."
ACTIVE = "about"
FILENAME = "about.html"

BODY = f"""
{page_hero(
    "About us",
    "A team, not just a machine.",
    "River Valley Robotics is a student-led combat robotics club at River Valley High School. We build robots, but the real project is the people doing the building.",
    "At a glance",
    f"River Valley High School<br>Yuba City Unified School District<br>Meets {MEETINGS} &middot; {ROOM}",
    "About",
)}

<section class="section section--paper" aria-labelledby="story">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Our story</p>
        <h2 id="story">We learn<br>by building.</h2>
        <p class="lead" style="margin-top:1.4rem">River Valley Robotics is in its second year as a club robotics team. Every season starts with a question: can we build a machine that survives the arena? Then a room full of students tries to answer it.</p>
        <p>Some of us came in knowing how to solder. Most of us didn't. What we share is a willingness to learn in public: to sketch an idea, ask for help, cut the wrong piece, and try again. That is what combat robotics looks like up close.</p>
        <p>Along the way, students practice CAD, fabrication, electronics, programming, project management, and communication. Those skills travel. So does the habit of solving a problem with a team.</p>
        <div class="tag-row" style="margin-top:1.5rem">
          <span class="tag tag--gold">Combat robotics</span>
          <span class="tag">Student-led</span>
          <span class="tag">Second season</span>
        </div>
      </div>
      <div class="reveal" style="--d:120ms">
        <figure class="feature-media" style="margin:0">
          <img src="assets/img/team-shop.webp" width="1100" height="1100" alt="The team's workbench in Room 408, with drills, tools, electronics, and 3D-printed robot parts" loading="lazy">
          <figcaption class="media-tag">The shop &middot; Room 408</figcaption>
        </figure>
        <div class="callout callout--light" style="margin-top:1.25rem">
          &ldquo;The robot is the excuse. The team is the point.&rdquo;
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="values">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">What we value</p>
        <h2 id="values">How we work.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Four rules that hold up whether we're drilling a frame at lunch or packing the pit at a competition.</p>
      </div>
    </div>
    <div class="value-grid">
      <div class="value reveal">
        <span class="value-num">01</span>
        <h3>Learn by doing</h3>
        <p>The fastest way to understand something is to build it, break it, and try again.</p>
      </div>
      <div class="value reveal" style="--d:60ms">
        <span class="value-num">02</span>
        <h3>Everyone contributes</h3>
        <p>No benchwarmers. Every member owns a job and a real piece of the build.</p>
      </div>
      <div class="value reveal" style="--d:120ms">
        <span class="value-num">03</span>
        <h3>Build it safe</h3>
        <p>Safety glasses on, tools respected, checklists followed &mdash; every time, for everyone.</p>
      </div>
      <div class="value reveal" style="--d:180ms">
        <span class="value-num">04</span>
        <h3>Give back</h3>
        <p>We share what we learn with our school and our community, not just the scoreboard.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="subteams">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Subteams</p>
        <h2 id="subteams">Find your<br>corner of the shop.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Students choose a home base, but everyone helps everywhere. On a small team, the person who designs the part may also be the one who packs the crate.</p>
      </div>
    </div>
    <div class="role-grid">
      <article class="role reveal">
        <span class="role-tag">Hands-on</span>
        <h3>Mechanical</h3>
        <p>CAD, prototyping, machining, assembly, and keeping the frame in one piece.</p>
      </article>
      <article class="role reveal" style="--d:50ms">
        <span class="role-tag">Wiring</span>
        <h3>Electrical</h3>
        <p>Motors, speed controllers, batteries, switches, and clean, labeled wiring.</p>
      </article>
      <article class="role reveal" style="--d:100ms">
        <span class="role-tag">Code</span>
        <h3>Software</h3>
        <p>Controls, motor mixing, testing, and making the robot predictable for the driver.</p>
      </article>
      <article class="role reveal" style="--d:150ms">
        <span class="role-tag">Outreach</span>
        <h3>Business</h3>
        <p>Sponsorships, budgeting, event planning, and telling the team's story.</p>
      </article>
      <article class="role reveal" style="--d:200ms">
        <span class="role-tag">The bot</span>
        <h3>Weapon &amp; armor</h3>
        <p>Weapon mounts, wedges, armor panels, and the repairs that keep us in the bracket.</p>
      </article>
      <article class="role reveal" style="--d:250ms">
        <span class="role-tag">Story</span>
        <h3>Media &amp; design</h3>
        <p>Photos, video, social media, posters, and the look of the team.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="mentors">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Mentors</p>
        <h2 id="mentors">The adults<br>behind the build.</h2>
        <p class="lead" style="margin-top:1.4rem">Our mentors are teachers, parents, alumni, and local professionals who give time, tools, and perspective. They don't build the robot for us. They help us learn how to build it ourselves.</p>
        <p>You don't need to be a robotics expert to help. We need people who can teach a skill, supervise a shop, drive students, organize a fundraiser, or simply show up consistently.</p>
        <div style="margin-top:1.5rem">
          <a class="btn btn--primary" href="join.html#mentors">Become a mentor {icon("arrow", "btn-arrow")}</a>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="info-list">
          <div class="info-row"><dt>Who</dt><dd>Teachers, parents, alumni, and industry professionals</dd></div>
          <div class="info-row"><dt>Commitment</dt><dd>As little as a few hours a month, or every build session</dd></div>
          <div class="info-row"><dt>Clearance</dt><dd>District volunteer requirements apply for regular volunteers</dd></div>
          <div class="info-row"><dt>Skills needed</dt><dd>Machining, wiring, code, CAD, media, fundraising, mentoring &mdash; or none of the above</dd></div>
        </div>
        <div class="callout" style="margin-top:1.5rem">Every hour a mentor gives is an hour a student spends learning something real.</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="school">
  <div class="container">
    <div class="feature-split" style="align-items:center">
      <div class="reveal">
        <p class="kicker">Our school</p>
        <h2 id="school">Falcons, through<br>and through.</h2>
        <p class="lead" style="margin-top:1.4rem">We are proud to represent River Valley High School and the Yuba City community. Our club is part of the school's wider push to make hands-on, career-connected learning available to every student.</p>
        <p>Meetings are {MEETINGS} in {ROOM}. Announcements and schedule changes go out through Google Classroom (code <strong>gftqhxdh</strong>) and <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a>.</p>
        <div style="margin-top:1.5rem; display:flex; flex-wrap:wrap; gap:0.75rem">
          <a class="btn btn--outline" href="contact.html">Contact us {icon("arrow", "btn-arrow")}</a>
          <a class="btn btn--outline" href="https://rvhs.ycusd.org/" target="_blank" rel="noopener">RVHS website {icon("external")}</a>
        </div>
      </div>
      <div class="reveal" style="--d:100ms; display:grid; place-items:center; background:var(--white); border:1px solid var(--line); padding:clamp(2rem,5vw,3.5rem)">
        <img src="assets/img/rvhs-logo.png" width="260" height="260" alt="River Valley High School Falcons logo" loading="lazy" style="width:clamp(140px,16vw,190px);height:auto">
        <p class="mono-label" style="margin-top:1.5rem;text-align:center">River Valley High School<br>Home of the Falcons</p>
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
        <p class="lead">Still curious? Email us at <a href="mailto:rvrobotics@ycusd.org">rvrobotics@ycusd.org</a> or come find us in {ROOM}.</p>
      </div>
    </div>
    <div class="faq">
      <details>
        <summary>What is combat robotics?</summary>
        <p>Combat robotics is exactly what it sounds like: students design and build remote-controlled robots that compete in matches. The goal is to disable or outlast the opponent while staying inside the competition's safety and build rules.</p>
      </details>
      <details>
        <summary>Do I need robotics experience to join?</summary>
        <p>No. Most of our members start with no robotics background. We teach the tools, the software, and the safety rules from the beginning. Curiosity and reliability matter more than experience.</p>
      </details>
      <details>
        <summary>Who can join the team?</summary>
        <p>River Valley High School students in grades 9 through 12. We also welcome parents, alumni, and community members as mentors and volunteers.</p>
      </details>
      <details>
        <summary>When do you meet?</summary>
        <p>{MEETINGS} in {ROOM}. Check Google Classroom (code <strong>gftqhxdh</strong>) or the team Instagram for schedule changes, especially around competitions.</p>
      </details>
      <details>
        <summary>What does it cost?</summary>
        <p>Ask us about current team fees and materials costs. We work hard to keep cost from being a barrier and can talk through options with families.</p>
      </details>
      <details>
        <summary>How can my business help?</summary>
        <p>Sponsorships of any size help with parts, tools, event fees, and travel. In-kind donations of materials, machining time, or professional expertise are welcome too. Start on the <a href="sponsors.html">sponsorship page</a>.</p>
      </details>
    </div>
  </div>
</section>

{cta_band(
    "Come see what we're building.",
    "Students, parents, and community members are always welcome to stop by, ask questions, and get involved.",
    "join.html",
    "Join the team",
    "contact.html",
    "Contact us",
)}
"""
