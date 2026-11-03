"""Sponsorship page."""
from rvsite import icon, page_hero, EMAIL, PHONE

TITLE = "Sponsor the team | River Valley Robotics"
DESCRIPTION = "Sponsor River Valley Robotics, a student combat robotics club in Yuba City. Put your business behind the next generation of builders, programmers, and problem-solvers. See levels, benefits, and how support is used."
ACTIVE = "sponsors"
FILENAME = "sponsors.html"

TIERS = [
    {
        "key": "Supporter",
        "price": "$250",
        "note": "Get the team started",
        "desc": "A meaningful first step for a local business or family.",
        "features": [
            "Name listed on the team website",
            "Social media thank-you",
            "Team sticker pack",
        ],
        "featured": False,
    },
    {
        "key": "Partner",
        "price": "$500",
        "note": "Wear the name",
        "desc": "Put your logo in front of students, families, and fans.",
        "features": [
            "Everything in Supporter",
            "Logo on the team website",
            "Logo on team shirts",
            "Invitation to the end-of-season showcase",
        ],
        "featured": False,
    },
    {
        "key": "Builder",
        "price": "$1,000",
        "note": "Most popular",
        "desc": "A visible partnership across the robot and the season.",
        "features": [
            "Everything in Partner",
            "Logo on the combat robot",
            "Banner at competitions",
            "Business spotlight on social media",
        ],
        "featured": True,
    },
    {
        "key": "Champion",
        "price": "$2,500+",
        "note": "Lead the build",
        "desc": "Presenting-level support for the team's biggest season yet.",
        "features": [
            "Everything in Builder",
            "Presenting sponsor placement",
            "Robot demo at your business",
            "First pick of showcase demos",
        ],
        "featured": False,
    },
]

tier_cards = ""
for idx, tier in enumerate(TIERS):
    features = "".join(
        f"<li>{icon('check')}<span>{item}</span></li>" for item in tier["features"]
    )
    featured_class = " tier--featured" if tier["featured"] else ""
    badge = '<span class="tier-badge">Most popular</span>' if tier["featured"] else ""
    tier_cards += f"""
    <article class="tier{featured_class} reveal" style="--d:{idx * 70}ms">
      {badge}
      <div class="tier-name">{tier['key']}</div>
      <div class="tier-price">{tier['price']}<small>{'starting' if tier['price'].endswith('+') else 'one-time'}</small></div>
      <p>{tier['desc']}</p>
      <ul>{features}</ul>
      <a class="btn {'btn--dark' if tier['featured'] else 'btn--outline'} btn--block" href="#sponsor-form" data-tier="{tier['key']}">Choose {tier['key']}</a>
    </article>
    """

BODY = f"""
{page_hero(
    "Sponsorship",
    "Sponsor the build.",
    "Your support puts tools in students' hands, keeps a combat robot in the arena, and turns a school club into a launchpad for the next generation of engineers.",
    "Sponsor packet",
    "Levels, benefits, and budget.<br><a href=\"assets/RVRobotics-Sponsorship-Packet.pdf\" style=\"color:var(--gold)\">Download the PDF &rarr;</a>",
    "Sponsors",
)}

<section class="section section--paper" aria-labelledby="why">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Why it matters</p>
        <h2 id="why">Your business.<br>Their launchpad.</h2>
        <p class="lead" style="margin-top:1.4rem">A combat robotics team is a small company run by students. They plan budgets, manage deadlines, solve technical problems, and explain their work to adults. Now in our second season, sponsorship is what makes that experience possible.</p>
        <p>Every dollar goes into the build: parts, tools, event fees, travel, and the supplies that let a student try an idea a second time. Your name goes where the work happens &mdash; on the robot, the shirts, the website, and the pit.</p>
        <div class="tag-row" style="margin-top:1.5rem">
          <span class="tag tag--gold">Local visibility</span>
          <span class="tag">Workforce pipeline</span>
          <span class="tag">Community impact</span>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="budget">
          <div class="budget-row">
            <span class="budget-label">Registration &amp; event fees</span>
            <span class="budget-track"><span class="budget-fill" style="--value:35%"></span></span>
            <span class="budget-value">35%</span>
          </div>
          <div class="budget-row">
            <span class="budget-label">Robot materials &amp; parts</span>
            <span class="budget-track"><span class="budget-fill" style="--value:30%"></span></span>
            <span class="budget-value">30%</span>
          </div>
          <div class="budget-row">
            <span class="budget-label">Tools &amp; shop supplies</span>
            <span class="budget-track"><span class="budget-fill" style="--value:20%"></span></span>
            <span class="budget-value">20%</span>
          </div>
          <div class="budget-row">
            <span class="budget-label">Travel &amp; competition</span>
            <span class="budget-track"><span class="budget-fill budget-fill--gold" style="--value:10%"></span></span>
            <span class="budget-value">10%</span>
          </div>
          <div class="budget-row">
            <span class="budget-label">Outreach &amp; community</span>
            <span class="budget-track"><span class="budget-fill budget-fill--gold" style="--value:5%"></span></span>
            <span class="budget-value">5%</span>
          </div>
        </div>
        <p class="small muted" style="margin-top:1.1rem">Typical season allocation. Actual spending follows the team budget and district purchasing rules.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="tiers" aria-labelledby="tiers-heading">
  <div class="container">
    <div class="section-head section-head--center">
      <p class="kicker">Sponsorship levels</p>
      <h2 id="tiers-heading">Pick your level.</h2>
      <p class="head-copy" style="text-align:center">Every level includes a thank-you on our website and in our season recap. Custom packages are welcome if none of these fit.</p>
    </div>
    <div class="tier-grid">
      {tier_cards}
    </div>
    <p class="small muted" style="margin-top:1.25rem">Sponsorship is accepted year-round. Logo deadlines for shirts and the robot are set each season; contact us for the current date.</p>
  </div>
</section>

<section class="section section--paper-2" aria-labelledby="benefits">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Benefits</p>
        <h2 id="benefits">What you get.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Recognition is only part of it. Sponsors also get a direct line to a team that is learning exactly the skills local employers need.</p>
      </div>
    </div>
    <div class="benefits-wrap">
      <table class="benefits">
        <caption class="visually-hidden">Sponsorship benefits by level</caption>
        <thead>
          <tr>
            <th scope="col">Benefit</th>
            <th scope="col">Supporter<br><span class="table-price">$250</span></th>
            <th scope="col">Partner<br><span class="table-price">$500</span></th>
            <th scope="col">Builder<br><span class="table-price">$1,000</span></th>
            <th scope="col">Champion<br><span class="table-price">$2,500+</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">Name on the team website</th><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Social media thank-you</th><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Logo on team shirts</th><td>—</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Logo on the combat robot</th><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Banner at competitions</th><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Business spotlight post</th><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Presenting sponsor placement</th><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
          <tr><th scope="row">Robot demo at your business</th><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="partners">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">2026&ndash;27 partners</p>
        <h2 id="partners">Your name<br>could be here.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">We're building the partner wall for the coming season. Be one of the first businesses to back the team &mdash; and get the most visible recognition of the year.</p>
        <div style="margin-top:1.5rem">
          <a class="btn btn--primary" href="#sponsor-form">Become a sponsor {icon("arrow", "btn-arrow")}</a>
        </div>
      </div>
    </div>
    <div class="logo-wall">
      <div class="logo-slot logo-slot--active">Your logo here</div>
      <div class="logo-slot">Your logo here</div>
      <div class="logo-slot">Your logo here</div>
      <div class="logo-slot">Your logo here</div>
      <div class="logo-slot">Your logo here</div>
      <div class="logo-slot">Your logo here</div>
    </div>
    <p class="photo-credit">Current partners are added as commitments are confirmed. <a href="#sponsor-form">Talk to us about joining the wall.</a></p>
  </div>
</section>

<section class="section section--white" id="sponsor-form" aria-labelledby="inquiry">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Start a conversation</p>
        <h2 id="inquiry">Let's build<br>something together.</h2>
        <p class="lead" style="margin-top:1.4rem">Tell us a little about your business and what you'd like to support. We'll follow up with a packet, a budget conversation, and next steps.</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
          <div class="info-row"><dt>Phone</dt><dd><a href="tel:+15308222500">{PHONE}</a> &mdash; RVHS front office</dd></div>
          <div class="info-row"><dt>Instagram</dt><dd><a href="https://www.instagram.com/rv.robotics/" target="_blank" rel="noopener">@rv.robotics</a></dd></div>
          <div class="info-row"><dt>Mail</dt><dd>River Valley High School<br>Attn: Robotics<br>801 El Margarita Rd.<br>Yuba City, CA 95993</dd></div>
        </div>
        <div class="callout callout--light" style="margin-top:1.5rem">
          Ask us about in-kind donations, materials, machining time, and mentor expertise. Cash is not the only way to help.
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <form class="form-card" data-mailto="{EMAIL}" data-subject="Sponsorship inquiry — River Valley Robotics">
          <div class="form-grid">
            <div class="field field--full">
              <label for="company">Business or organization</label>
              <input id="company" name="company" type="text" autocomplete="organization" required>
            </div>
            <div class="field">
              <label for="contact-name">Contact name</label>
              <input id="contact-name" name="contact_name" type="text" autocomplete="name" required>
            </div>
            <div class="field">
              <label for="contact-email">Email</label>
              <input id="contact-email" name="email" type="email" autocomplete="email" required>
            </div>
            <div class="field">
              <label for="phone">Phone <span class="optional">(optional)</span></label>
              <input id="phone" name="phone" type="tel" autocomplete="tel">
            </div>
            <div class="field">
              <label for="sponsor-tier">Sponsorship level</label>
              <select id="sponsor-tier" name="level">
                <option value="">Not sure yet</option>
                <option value="Supporter — $250">Supporter &mdash; $250</option>
                <option value="Partner — $500">Partner &mdash; $500</option>
                <option value="Builder — $1,000">Builder &mdash; $1,000</option>
                <option value="Champion — $2,500+">Champion &mdash; $2,500+</option>
                <option value="Custom / in-kind">Custom or in-kind</option>
              </select>
            </div>
            <div class="field field--full">
              <label for="message">What would you like to support? <span class="optional">(optional)</span></label>
              <textarea id="message" name="message" placeholder="Tell us about your business, your goals, or the kind of support you have in mind."></textarea>
            </div>
          </div>
          <div class="form-foot">
            <p class="form-note">This form opens your email app with the details filled in. Prefer to write directly? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
            <button class="btn btn--dark" type="submit">Send inquiry {icon("arrow", "btn-arrow")}</button>
          </div>
          <p class="small" data-form-status hidden style="margin-top:1rem;color:var(--green)"></p>
        </form>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" aria-labelledby="sponsor-faq">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Sponsor questions</p>
        <h2 id="sponsor-faq">The details.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Need something that isn't here? Call or email us &mdash; we'll find a straight answer.</p>
      </div>
    </div>
    <div class="faq">
      <details>
        <summary>Is my sponsorship tax deductible?</summary>
        <p>Ask us for the current tax information before you give. Donations may be processed through the RVHS Booster Club or the district, depending on the type of support. We'll give you the correct receipt and documentation.</p>
      </details>
      <details>
        <summary>Can we donate materials or services instead of cash?</summary>
        <p>Yes. Aluminum, fasteners, tools, machining time, printing, food for build nights, and professional expertise are all valuable. We'll work with you on an in-kind acknowledgement.</p>
      </details>
      <details>
        <summary>Can we choose what our sponsorship supports?</summary>
        <p>Usually. We can direct support toward a specific need such as registration, a subsystem, safety equipment, or travel. We'll confirm the details in writing.</p>
      </details>
      <details>
        <summary>How will our logo be used?</summary>
        <p>With your approval, on the team website, shirts, robot, event banner, and social posts according to your level. We'll ask for a vector logo and brand guidelines when you commit.</p>
      </details>
      <details>
        <summary>When is the deadline for logo placement?</summary>
        <p>Shirt and robot deadlines are set each season. Sponsor early to guarantee placement on both. Website and social recognition can be added year-round.</p>
      </details>
      <details>
        <summary>Will the team visit our business?</summary>
        <p>Champion sponsors can schedule a robot demo or a student presentation. We can also host your team at the school shop, subject to district visitor rules.</p>
      </details>
    </div>
  </div>
</section>

<section class="section section--tight section--dark">
  <div class="container">
    <div class="sponsor-cta" style="background:var(--gold);color:var(--ink)">
      <div>
        <p class="kicker" style="color:var(--forest)">Take the packet with you</p>
        <h2 style="color:var(--ink)">Everything in one PDF.</h2>
        <p style="color:rgba(8,13,10,.72)">Levels, benefits, budget, and contact information &mdash; ready to share with your team or your boss.</p>
      </div>
      <div class="sponsor-cta-actions">
        <a class="btn btn--dark" href="assets/RVRobotics-Sponsorship-Packet.pdf">Download packet {icon("download", "btn-arrow")}</a>
        <a class="btn btn--outline" href="mailto:{EMAIL}">Email us</a>
      </div>
    </div>
  </div>
</section>
"""
