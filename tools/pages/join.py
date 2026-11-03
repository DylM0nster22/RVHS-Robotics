"""Join / get involved page."""
from rvsite import icon, page_hero, cta_band, EMAIL, ROOM, MEETINGS

TITLE = "Join the team | River Valley Robotics"
DESCRIPTION = "Join River Valley Robotics, a student combat robotics club at River Valley High School. No experience required. Meetings are Thursdays and Fridays in Room 408."
ACTIVE = "join"
FILENAME = "join.html"

BODY = f"""
{page_hero(
    "Get involved",
    "Join the build.",
    "No experience required. No secret handshake. If you're curious and willing to show up, there is a place for you on this combat robotics team.",
    "Meets",
    f"{MEETINGS} &middot; {ROOM}<br>RVHS students in grades 9&ndash;12.<br>Parents and community mentors welcome.",
    "Join",
)}

<section class="section section--paper" aria-labelledby="paths">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Three ways in</p>
        <h2 id="paths">Pick your path.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">The team runs on students, families, and mentors. Everyone starts somewhere &mdash; usually by walking into the shop and asking what they can do.</p>
      </div>
    </div>
    <div class="role-grid">
      <article class="role reveal">
        <span class="role-tag">Students</span>
        <h3>Build with us</h3>
        <p>Design, fabricate, wire, code, document, or run the business side. Choose a subteam and learn on real work.</p>
        <p style="margin-top:1rem"><a class="text-link" href="#students">Student info {icon("arrow")}</a></p>
      </article>
      <article class="role reveal" style="--d:70ms">
        <span class="role-tag">Parents</span>
        <h3>Support the team</h3>
        <p>Help with transportation, food, events, fundraising, or shop supervision. Small, consistent help matters.</p>
        <p style="margin-top:1rem"><a class="text-link" href="#mentors">Parent info {icon("arrow")}</a></p>
      </article>
      <article class="role reveal" style="--d:140ms">
        <span class="role-tag">Mentors</span>
        <h3>Teach what you know</h3>
        <p>Bring machining, wiring, code, CAD, business, or media experience &mdash; or just a willingness to learn alongside us.</p>
        <p style="margin-top:1rem"><a class="text-link" href="#mentors">Mentor info {icon("arrow")}</a></p>
      </article>
    </div>
  </div>
</section>

<section class="section section--white" id="students" aria-labelledby="students-heading">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">For students</p>
        <h2 id="students-heading">Start where<br>you are.</h2>
        <p class="lead" style="margin-top:1.4rem">You do not need to know how to use a drill, write code, or design a part. You need to be curious, follow safety rules, and be part of the team.</p>
        <p>New members rotate through the shop, learn the basics, and then choose a subteam. Older students and mentors teach the tools. The work is real, and it goes into a combat robot that competes.</p>
        <h3 style="margin-top:1.6rem">What you'll get</h3>
        <ul class="check-list" style="list-style:none;padding:0;display:grid;gap:.55rem;margin-top:.8rem">
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>Hands-on experience with tools, CAD, electronics, and code</span></li>
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>A team that respects beginners and rewards reliability</span></li>
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>Something real for your resume, college applications, and portfolio</span></li>
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>Match days, a pit crew, and a group that becomes a second family</span></li>
        </ul>
        <div style="margin-top:1.75rem">
          <a class="btn btn--dark" href="#interest">Tell us you're interested {icon("arrow", "btn-arrow")}</a>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="info-list">
          <div class="info-row"><dt>Who</dt><dd>RVHS students, grades 9&ndash;12</dd></div>
          <div class="info-row"><dt>When</dt><dd>{MEETINGS}, plus extra build sessions near a competition</dd></div>
          <div class="info-row"><dt>Where</dt><dd>{ROOM}, River Valley High School</dd></div>
          <div class="info-row"><dt>Classroom</dt><dd>Google Classroom code <strong>gftqhxdh</strong> for announcements</dd></div>
          <div class="info-row"><dt>Experience</dt><dd>None required. Training provided.</dd></div>
          <div class="info-row"><dt>Cost</dt><dd>Ask about current team fees; we work to keep cost from being a barrier.</dd></div>
        </div>
        <div class="callout callout--light" style="margin-top:1.5rem">
          The best time to join is the start of the season. The second-best time is now.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--dark" id="mentors" aria-labelledby="mentors-heading">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">For parents &amp; mentors</p>
        <h2 id="mentors-heading">You don't have<br>to be an expert.</h2>
        <p class="lead" style="margin-top:1.4rem">Some of the most useful help has nothing to do with robots: driving students to events, organizing a parts bin, bringing dinner to a build night, or asking the question that makes a student explain their idea more clearly.</p>
        <p>If you do have technical experience &mdash; machining, electrical, software, CAD, project management &mdash; we would love to put it to work. Mentors teach by asking questions, not by taking the controller.</p>
        <div style="margin-top:1.5rem; display:flex; flex-wrap:wrap; gap:.75rem">
          <a class="btn btn--primary" href="#interest">Offer to help {icon("arrow", "btn-arrow")}</a>
          <a class="btn btn--ghost" href="contact.html">Ask a question</a>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="info-list">
          <div class="info-row"><dt>Who</dt><dd>Parents, alumni, RVHS staff, and community professionals</dd></div>
          <div class="info-row"><dt>Time</dt><dd>A few hours a month, one build night a week, or more &mdash; your call</dd></div>
          <div class="info-row"><dt>Clearance</dt><dd>District volunteer requirements apply for regular volunteers</dd></div>
          <div class="info-row"><dt>Skills</dt><dd>Technical or not &mdash; reliability and respect matter most</dd></div>
        </div>
        <div class="callout" style="margin-top:1.5rem">
          Students remember the adults who showed up. Be one of them.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" id="interest" aria-labelledby="interest-heading">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Interest form</p>
        <h2 id="interest-heading">Say hello.</h2>
        <p class="lead" style="margin-top:1.4rem">Send us a quick note and we'll get back to you with the current meeting schedule and next steps. Students, parents, and mentors all use the same form.</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>Meetings</dt><dd>{MEETINGS} in {ROOM}</dd></div>
          <div class="info-row"><dt>Classroom</dt><dd>Join the Google Classroom with code <strong>gftqhxdh</strong></dd></div>
          <div class="info-row"><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div class="info-row"><dt>Response</dt><dd>We're students, so please allow a couple of school days.</dd></div>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <form class="form-card" data-mailto="{EMAIL}" data-subject="Join interest — River Valley Robotics">
          <div class="form-grid">
            <div class="field field--full">
              <label for="join-name">Your name</label>
              <input id="join-name" name="name" type="text" autocomplete="name" required>
            </div>
            <div class="field field--full">
              <label for="join-email">Email</label>
              <input id="join-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="field">
              <label for="join-role">I am a&hellip;</label>
              <select id="join-role" name="role" required>
                <option value="">Choose one</option>
                <option>Student (grade 9)</option>
                <option>Student (grade 10)</option>
                <option>Student (grade 11)</option>
                <option>Student (grade 12)</option>
                <option>Parent / guardian</option>
                <option>Community mentor</option>
                <option>RVHS staff</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field">
              <label for="join-interest">I'm interested in <span class="optional">(optional)</span></label>
              <select id="join-interest" name="interest">
                <option value="">Not sure yet</option>
                <option>Mechanical / fabrication</option>
                <option>Electrical / wiring</option>
                <option>Software / programming</option>
                <option>Business / sponsorship</option>
                <option>Media / design</option>
                <option>Mentoring / supervision</option>
                <option>General help</option>
              </select>
            </div>
            <div class="field field--full">
              <label for="join-message">Anything else? <span class="optional">(optional)</span></label>
              <textarea id="join-message" name="message" placeholder="Tell us a little about yourself, your schedule, or what you'd like to learn."></textarea>
            </div>
          </div>
          <div class="form-foot">
            <p class="form-note">This form opens your email app with the details filled in. Prefer to write directly? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
            <button class="btn btn--dark" type="submit">Send interest {icon("arrow", "btn-arrow")}</button>
          </div>
          <p class="small" data-form-status hidden style="margin-top:1rem;color:var(--green)"></p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="next">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">What happens next</p>
        <h2 id="next">From email<br>to build night.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">No auditions, no tryouts. Just a conversation and a first meeting.</p>
      </div>
    </div>
    <div class="role-grid">
      <article class="role reveal">
        <span class="role-tag">Step 01</span>
        <h3>Send a note</h3>
        <p>Use the form or email us. Tell us who you are and what you're curious about.</p>
      </article>
      <article class="role reveal" style="--d:70ms">
        <span class="role-tag">Step 02</span>
        <h3>Come to a meeting</h3>
        <p>Visit after school, meet the team, and see what a build night actually feels like.</p>
      </article>
      <article class="role reveal" style="--d:140ms">
        <span class="role-tag">Step 03</span>
        <h3>Pick a subteam</h3>
        <p>Try a few things, then settle into the work that fits you best. We'll help.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="join-faq">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Questions</p>
        <h2 id="join-faq">Before you start.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Still unsure? That's normal. Come by and see what it's like.</p>
      </div>
    </div>
    <div class="faq">
      <details>
        <summary>What if I can only come once a week?</summary>
        <p>Come once a week. Consistency matters more than hours, especially at the start. Build season gets busier, but there is work for every schedule.</p>
      </details>
      <details>
        <summary>Do I need to buy my own tools?</summary>
        <p>No. The team provides tools and safety equipment. If you have your own safety glasses or hand tools, bring them, but nothing is required.</p>
      </details>
      <details>
        <summary>Can I join in the middle of the year?</summary>
        <p>Yes, though the start of a season is the easiest time to onboard. We'll help you catch up and find a job that fits where the team is.</p>
      </details>
      <details>
        <summary>Is the team competitive?</summary>
        <p>We compete, and we want to do well. But the bigger goal is learning. Students who are new to robotics are not a liability &mdash; they are the point.</p>
      </details>
      <details>
        <summary>What do parents actually do?</summary>
        <p>Transportation, food, event help, fundraising, supervision, and professional advice. Every family has different capacity; whatever you can offer is useful.</p>
      </details>
      <details>
        <summary>Is there a fee?</summary>
        <p>Ask us about current team fees and materials costs. We work to keep cost from being a barrier and can talk through options confidentially.</p>
      </details>
    </div>
  </div>
</section>

{cta_band(
    "Bring a friend.",
    "The strongest teams are built by people who bring someone else in. Forward this page to a student, parent, or mentor who would be a good fit.",
    "contact.html",
    "Contact the team",
    "sponsors.html#tiers",
    "Sponsor the team",
)}
"""
