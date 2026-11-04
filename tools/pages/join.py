"""Join / get involved page."""
from rvsite import icon, page_hero, EMAIL, ROOM, MEETINGS, CLASSROOM

TITLE = "Join the club | River Valley Robotics"
DESCRIPTION = "Join River Valley Robotics, a student combat robotics club at River Valley High School. Meetings are Thursdays and Fridays in Room 408. No experience required."
ACTIVE = "join"
FILENAME = "join.html"

BODY = f"""
{page_hero(
    "Get involved",
    "Come to<br>a meeting.",
    "We meet Thursdays and Fridays in Room 408. If you're a River Valley student in grades 9&ndash;12 and you're curious, stop by. No experience needed.",
    "Meets",
    f"{MEETINGS} &middot; {ROOM}<br>Grades 9&ndash;12<br>No experience needed",
    "Join",
)}

<section class="section section--paper" id="students" aria-labelledby="students-heading">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">For students</p>
        <h2 id="students-heading">You don't need<br>to know anything yet.</h2>
        <p class="lead" style="margin-top:1.4rem">You can start by watching, asking questions, and trying a small job. That's how most people learn in the shop.</p>
        <p>We need people who can design, print, solder, code, drive, take photos, or keep the parts bin organized. If you're not sure where you fit, that's fine. We'll help you find something.</p>
        <ul class="check-list" style="list-style:none;padding:0;display:grid;gap:.55rem;margin-top:1.25rem">
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>Learn the tools safely, at your own pace</span></li>
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>Work on a real robot, not a worksheet</span></li>
          <li style="display:flex;gap:.6rem">{icon("check", "check-icon")}<span>Try more than one job before you pick a lane</span></li>
        </ul>
        <div style="margin-top:1.75rem">
          <a class="btn btn--dark" href="#interest">Tell us you're interested {icon("arrow", "btn-arrow")}</a>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="info-list">
          <div class="info-row"><dt>When</dt><dd>{MEETINGS}</dd></div>
          <div class="info-row"><dt>Where</dt><dd>{ROOM}, River Valley High School</dd></div>
          <div class="info-row"><dt>Who</dt><dd>RVHS students, grades 9&ndash;12</dd></div>
          <div class="info-row"><dt>Classroom</dt><dd>Google Classroom code <strong>{CLASSROOM}</strong> for announcements</dd></div>
          <div class="info-row"><dt>Cost</dt><dd>Ask us about current fees. We don't want cost to be the reason you don't join.</dd></div>
        </div>
        <div class="callout callout--light" style="margin-top:1.5rem">
          You can come to a meeting before you decide. Talk to us and see what it's like.
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="mentors" aria-labelledby="mentors-heading">
  <div class="container">
    <div class="feature-split">
      <div class="reveal">
        <p class="kicker">Parents &amp; mentors</p>
        <h2 id="mentors-heading">We can use<br>your help.</h2>
        <p class="lead" style="margin-top:1.4rem">Driving students to events, supervising the shop, bringing food, or teaching a skill all help. Technical experience is nice, but reliability matters more.</p>
        <p>If you're interested, email <a href="mailto:{EMAIL}">{EMAIL}</a> and tell us what you can help with. District volunteer requirements apply for regular volunteers.</p>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="callout callout--light">
          You don't have to be a robotics expert. You just have to show up and treat students with respect.
        </div>
        <div style="margin-top:1.5rem">
          <a class="btn btn--outline" href="mailto:{EMAIL}?subject=Volunteering%20with%20River%20Valley%20Robotics">Email about volunteering {icon("mail", "btn-arrow")}</a>
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
        <p class="lead" style="margin-top:1.4rem">Send us a quick note and we'll get back to you with the current meeting schedule and next steps. Students, parents, and mentors can all use this form.</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>Meetings</dt><dd>{MEETINGS} in {ROOM}</dd></div>
          <div class="info-row"><dt>Classroom</dt><dd>Google Classroom code <strong>{CLASSROOM}</strong></dd></div>
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

<section class="section section--white" aria-labelledby="join-faq">
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
        <summary>Do I need experience?</summary>
        <p>No. We teach the tools, the software, and the safety rules. Curiosity and showing up matter more than experience.</p>
      </details>
      <details>
        <summary>Can I join in the middle of the year?</summary>
        <p>Yes. The start of a season is the easiest time to onboard, but we can help you catch up and find a job that fits where the team is.</p>
      </details>
      <details>
        <summary>What if I can only come once a week?</summary>
        <p>Come once a week. Consistency matters more than hours, especially at the start. Build season gets busier, but there is work for every schedule.</p>
      </details>
      <details>
        <summary>Do I need to buy my own tools?</summary>
        <p>No. The team provides tools and safety equipment. If you have your own safety glasses or hand tools, bring them, but nothing is required.</p>
      </details>
    </div>
  </div>
</section>
"""
