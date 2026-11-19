"""Contact page."""
from rvsite import (icon, page_hero, EMAIL, EMAIL_INFO, EMAIL_TEAM, EMAIL_SPONSORS,
                    EMAIL_PARTNERSHIPS, EMAIL_OUTREACH, EMAIL_PRESIDENT,
                    PHONE, INSTAGRAM, INSTAGRAM_HANDLE, ADDRESS_1, ADDRESS_2, ROOM, MEETINGS, CLASSROOM)

TITLE = "Contact | River Valley Robotics"
DESCRIPTION = "Contact River Valley Robotics at River Valley High School in Yuba City, California. Reach the team about sponsorship, joining, mentoring, or media."
ACTIVE = "contact"
FILENAME = "contact.html"

BODY = f"""
{page_hero(
    "Contact",
    "Say hello.",
    "Questions about joining, sponsoring, or visiting the shop? Email is the best way to reach us.",
    "Response time",
    "We're students, so please allow a couple of school days for a reply. For school questions, call the RVHS front office.",
    "Contact",
)}

<section class="section section--paper" aria-label="Contact methods">
  <div class="container">
    <div class="grid-3">
      <article class="card reveal">
        <div class="card-icon">{icon("mail")}</div>
        <h3>Email</h3>
        <p>The best way to reach the team. Tell us what you need and we'll route it to the right person.</p>
        <p><a class="text-link" href="mailto:{EMAIL}">{EMAIL} {icon("arrow")}</a></p>
      </article>
      <article class="card reveal" style="--d:70ms">
        <div class="card-icon">{icon("phone")}</div>
        <h3>Call or visit</h3>
        <p>River Valley High School front office:<br><a href="tel:+15308222500">{PHONE}</a></p>
        <p>{ADDRESS_1}<br>{ADDRESS_2}</p>
        <p class="small muted">We meet {MEETINGS} in {ROOM}.</p>
      </article>
      <article class="card reveal" style="--d:140ms">
        <div class="card-icon">{icon("instagram")}</div>
        <h3>Follow</h3>
        <p>Build updates, meeting changes, and match-day photos.</p>
        <p><a class="text-link" href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE} {icon("external")}</a></p>
      </article>
    </div>
    <div class="heading-row" style="margin-top:clamp(2.75rem, 5vw, 4.5rem)">
      <div>
        <p class="kicker">Direct addresses</p>
        <h2>Who to email.</h2>
      </div>
      <p class="mono-label">Every address ends in @rvhsrobotics.com</p>
    </div>
    <div class="info-list" style="max-width:54rem">
      <div class="info-row"><dt>General</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a> &mdash; anything that does not fit a category below.</dd></div>
      <div class="info-row"><dt>Information</dt><dd><a href="mailto:{EMAIL_INFO}">{EMAIL_INFO}</a> &mdash; basic questions about the club, our meetings, and what we build.</dd></div>
      <div class="info-row"><dt>Team &amp; parents</dt><dd><a href="mailto:{EMAIL_TEAM}">{EMAIL_TEAM}</a> &mdash; students who want to join, parents with scheduling questions, and current members.</dd></div>
      <div class="info-row"><dt>Sponsorship</dt><dd><a href="mailto:{EMAIL_SPONSORS}">{EMAIL_SPONSORS}</a> &mdash; levels, the sponsor packet, check or transfer gifts, and logo files.</dd></div>
      <div class="info-row"><dt>Partnerships</dt><dd><a href="mailto:{EMAIL_PARTNERSHIPS}">{EMAIL_PARTNERSHIPS}</a> &mdash; businesses, in-kind donations, robot demos, and longer-term partnerships.</dd></div>
      <div class="info-row"><dt>Outreach &amp; media</dt><dd><a href="mailto:{EMAIL_OUTREACH}">{EMAIL_OUTREACH}</a> &mdash; event invitations, photos, interviews, and press requests.</dd></div>
      <div class="info-row"><dt>Club president</dt><dd><a href="mailto:{EMAIL_PRESIDENT}">{EMAIL_PRESIDENT}</a> &mdash; student leadership and anything that needs the president directly.</dd></div>
    </div>
    <p class="small muted" style="max-width:54rem;margin-top:1.25rem">Not sure which one to use? Send it to <a href="mailto:{EMAIL}">{EMAIL}</a>. It reaches the whole team, so a message never gets lost in the wrong inbox.</p>
  </div>
</section>

<section class="section section--white" aria-labelledby="message">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Send a message</p>
        <h2 id="message">Tell us<br>what you need.</h2>
        <p class="lead" style="margin-top:1.4rem">Use the form and we'll get back to you. If you're a business interested in sponsorship, the <a href="sponsors.html#sponsor-form">sponsor inquiry form</a> has a few extra fields that help us respond faster.</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>Sponsors</dt><dd><a href="sponsors.html">Levels, benefits, and the packet</a></dd></div>
          <div class="info-row"><dt>Students</dt><dd><a href="join.html#students">How to join the club</a></dd></div>
          <div class="info-row"><dt>Mentors</dt><dd><a href="join.html#mentors">Ways to help</a></dd></div>
          <div class="info-row"><dt>Media</dt><dd>Photos, logos, and interview requests &mdash; <a href="mailto:{EMAIL_OUTREACH}">{EMAIL_OUTREACH}</a></dd></div>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <form class="form-card" data-mailto="{EMAIL}" data-subject="Website inquiry — River Valley Robotics">
          <div class="form-grid">
            <div class="field field--full">
              <label for="contact-form-name">Your name</label>
              <input id="contact-form-name" name="name" type="text" autocomplete="name" required>
            </div>
            <div class="field field--full">
              <label for="contact-form-email">Email</label>
              <input id="contact-form-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="field field--full">
              <label for="contact-form-topic">Topic</label>
              <select id="contact-form-topic" name="topic" required>
                <option value="">Choose one</option>
                <option>Sponsorship</option>
                <option>Joining the team</option>
                <option>Mentoring / volunteering</option>
                <option>Robot demo or event</option>
                <option>Media / press</option>
                <option>Something else</option>
              </select>
            </div>
            <div class="field field--full">
              <label for="contact-form-message">Message</label>
              <textarea id="contact-form-message" name="message" required></textarea>
            </div>
          </div>
          <div class="form-foot">
            <p class="form-note">This form opens your email app with the details filled in. Prefer to write directly? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
            <button class="btn btn--dark" type="submit">Send message {icon("arrow", "btn-arrow")}</button>
          </div>
          <p class="small" data-form-status hidden style="margin-top:1rem;color:var(--green)"></p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="find-us">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">Find us</p>
        <h2 id="find-us">On campus.</h2>
      </div>
      <p class="mono-label">801 El Margarita Rd. &middot; Yuba City, CA 95993</p>
    </div>
    <div style="border:1px solid var(--line);background:var(--white);padding:0.5rem">
      <iframe
        title="Map to River Valley High School, 801 El Margarita Road, Yuba City, California"
        src="https://www.google.com/maps?q=801+El+Margarita+Rd,+Yuba+City,+CA+95993&amp;output=embed"
        width="100%" height="420" style="border:0;display:block" loading="lazy"
        referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
    <p class="photo-credit">Meetings are {MEETINGS} in {ROOM}. Check Google Classroom (code <strong>{CLASSROOM}</strong>) or <a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a> for changes.</p>
  </div>
</section>
"""
