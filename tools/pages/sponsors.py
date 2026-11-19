"""Sponsorship page."""
import donors

from rvsite import (
    icon,
    page_hero,
    ASSET_VERSION,
    EMAIL_SPONSORS,
    EMAIL_PARTNERSHIPS,
    PHONE,
    PHONE_TEL,
    INSTAGRAM,
    INSTAGRAM_HANDLE,
    HCB_SLUG,
    DONATE_URL,
    LEDGER_URL,
    GRAPH_URL,
)

TITLE = "Sponsor the team | River Valley Robotics"
DESCRIPTION = "Sponsor River Valley Robotics, a student combat robotics club at River Valley High School in Yuba City. Donate online, see realistic levels, what the money buys, and how to help."
ACTIVE = "sponsors"
FILENAME = "sponsors.html"

TIERS = [
    {
        "key": "Supporter",
        "price": "$100",
        "desc": "A straightforward way to help with parts. This is the level that puts a logo on the wall.",
        "features": [
            "Name on the team website",
            "Logo on the team website",
            "Thank-you on Instagram",
            "Team sticker",
        ],
    },
    {
        "key": "Partner",
        "price": "$250",
        "desc": "For a local business that wants its name in front of the school.",
        "features": [
            "Everything in Supporter",
            "Logo on team shirts",
            "Invitation to a build night",
        ],
    },
    {
        "key": "Builder",
        "price": "$500",
        "desc": "Put your logo on the robot itself.",
        "features": [
            "Everything in Partner",
            "Logo on the robot",
            "Banner at events",
            "Business spotlight post",
        ],
    },
    {
        "key": "Champion",
        "price": "$1,000",
        "desc": "The top level. Help cover the season.",
        "features": [
            "Everything in Builder",
            "Presenting sponsor placement",
            "Robot demo at your business",
            "First pick of demo dates",
        ],
    },
]

tier_cards = ""
for idx, tier in enumerate(TIERS):
    features = "".join(
        f"<li>{icon('check')}<span>{item}</span></li>" for item in tier["features"]
    )
    tier_cards += f"""
    <article class="tier reveal" style="--d:{idx * 70}ms">
      <div class="tier-name">{tier['key']}</div>
      <div class="tier-price">{tier['price']}<small>one-time</small></div>
      <p>{tier['desc']}</p>
      <ul>{features}</ul>
      <a class="btn btn--dark btn--block" href="#donate-form" data-donate-amount="{tier['price'].replace('$', '').replace(',', '')}" data-donate-tier="{tier['key']}">Give {tier['price']}</a>
    </article>
    """

PACKET_NOTE = 'Levels, benefits, and contact info.<br><a href="assets/RVRobotics-Sponsorship-Packet.pdf" style="color:var(--accent)">Download the PDF &rarr;</a>'

# The donor wall grades every public gift by total giving. "Friend" is the
# catch-all for gifts under the $100 Supporter level, so a small gift still gets
# a card. A logo on the wall is the $100 benefit.
LEVELS = [{"slug": "friend", "label": "Friend", "min": 0, "note": "under $100"}] + [
    {
        "slug": tier["key"].lower(),
        "label": tier["key"],
        "min": int(tier["price"].replace("$", "").replace(",", "")),
        "note": f"{tier['price']} and up",
    }
    for tier in TIERS
]

DONOR_API = f"https://hcb.hackclub.com/api/v3/organizations/{HCB_SLUG}/donations?per_page=100"


def _level_tag(level):
    return f'<span class="tag tag--dark">{level["label"]} &middot; {donors.tier_note(level)}</span>'


_donations, donor_source = donors.fetch(HCB_SLUG)
DONOR_LIST = donors.aggregate(_donations, donors.load_config(), LEVELS)
DONOR_COUNT = len(DONOR_LIST)

if donor_source != "live":
    _state = "cached snapshot" if donor_source == "cache" else "no donation data"
    print(f"donor wall: {_state} ({DONOR_COUNT} donors)")

if DONOR_COUNT:
    donor_meta = (
        f"{DONOR_COUNT} public donor{'s' if DONOR_COUNT != 1 else ''} &middot; live from "
        f'<a href="{LEDGER_URL}" target="_blank" rel="noopener">Hack Club Bank</a>'
    )
else:
    donor_meta = f'No public gifts yet. <a href="{LEDGER_URL}" target="_blank" rel="noopener">See the ledger</a>'

donor_grid = donors.render_grid(
    DONOR_LIST,
    "No public gifts yet. The first name on the wall could be yours.",
)

donor_fallback = f"""
    <div class="donor-wall-fallback" data-donor-fallback{' hidden' if DONOR_COUNT else ''}>
      <a class="donor-wall-graph" href="{LEDGER_URL}" target="_blank" rel="noopener" aria-label="Donor graph for RVHS Robotics Club — open the public HCB ledger">
        <span class="donor-wall-label">Live donor graph &middot; graph.hcb.hackclub.com</span>
        <img src="{GRAPH_URL}" width="1152" height="88" alt="Donor wall for RVHS Robotics Club, live from Hack Club Bank" loading="lazy">
      </a>
    </div>"""

donor_levels = "".join(_level_tag(level) for level in sorted(LEVELS, key=lambda item: item["min"]))
donor_levels_attr = donors.levels_attribute(LEVELS)

EXTRA_BODY = f'<script src="js/donors.js?v={ASSET_VERSION}" defer></script>'

DONATE_POINTS = [
    (
        "shield",
        "Tax-deductible",
        "Hack Club Bank is a 501(c)(3). You get an emailed receipt as soon as the gift clears.",
    ),
    (
        "chip",
        "Card payments by Stripe",
        "Stripe processes the card. Your card number goes to Stripe, not to us or HCB.",
    ),
    (
        "users",
        "An open ledger",
        "Every dollar in and out is posted publicly on our HCB page, so anyone can check.",
    ),
]

donate_points = "".join(
    f'<li>{icon(key)}<div><strong>{title}</strong><span>{text}</span></div></li>'
    for key, title, text in DONATE_POINTS
)

DONATE_SECTION = f"""
<section class="section section--white" id="donate" aria-labelledby="donate-heading">
  <div class="container">
    <div class="donate-grid">
      <div class="reveal">
        <p class="kicker">Give online</p>
        <h2 id="donate-heading">Donate in<br>two minutes.</h2>
        <p class="lead" style="margin-top:1.4rem">Give any amount, one time or monthly. Gifts go straight to the team's Hack Club Bank account and turn into motors, batteries, filament, and entry fees.</p>
        <ul class="donate-points">
          {donate_points}
        </ul>
        <div class="donate-actions">
          <a class="btn btn--dark" href="{DONATE_URL}" target="_blank" rel="noopener">Open the donation page {icon("external", "btn-arrow")}</a>
          <a class="text-link" href="{LEDGER_URL}" target="_blank" rel="noopener">See the public ledger {icon("external")}</a>
        </div>
        <div class="donate-other">
          <h3>Prefer not to use a card?</h3>
          <p>Email <a href="mailto:{EMAIL_SPONSORS}">{EMAIL_SPONSORS}</a> for a check or transfer, or <a href="mailto:{EMAIL_PARTNERSHIPS}">{EMAIL_PARTNERSHIPS}</a> for an in-kind gift or a larger partnership. Either way, <a href="#tiers">pick a sponsorship level</a> for logo placement.</p>
        </div>
      </div>
      <div class="reveal donate-panel" id="donate-form" style="--d:100ms">
        <div class="donate-panel-head">
          <span class="donate-panel-title">Donation form</span>
          <span class="donate-panel-tag">Secure &middot; HCB</span>
        </div>
        <p class="donate-hint" data-donate-hint aria-live="polite" hidden></p>
        <iframe class="donate-frame" src="{DONATE_URL}" title="Donation form for RVHS Robotics Club, hosted by Hack Club Bank" allow="payment" scrolling="yes" loading="lazy"></iframe>
        <p class="small muted donate-panel-note">The form is hosted by Hack Club Bank. If it does not load, <a href="{DONATE_URL}" target="_blank" rel="noopener">open it in a new tab</a>.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--tight section--forest" id="donors" aria-labelledby="donors-heading">
  <div class="container">
    <div class="donor-wall-head">
      <div>
        <p class="kicker">Donor wall</p>
        <h2 id="donors-heading">Who backs<br>the build.</h2>
      </div>
      <div>
        <p>Public gifts show up here with the donor's name and logo, grouped by level. Levels follow total giving, so a monthly gift adds up over the season. Anonymous gifts are listed as Anonymous.</p>
        <p class="donor-wall-meta" data-donor-meta>{donor_meta}</p>
      </div>
    </div>
    <div class="donor-wall" data-donor-wall data-donor-api="{DONOR_API}" data-donor-levels="{donor_levels_attr}" data-donor-ledger="{LEDGER_URL}">
      <div data-donor-list>
        {donor_grid}
      </div>
    </div>
    {donor_fallback.strip()}
    <div class="donor-levels">
      <span class="donor-levels-label">Levels</span>
      {donor_levels}
    </div>
    <p class="donor-wall-note">Gifts under $100 are listed as Friends. Supporter ($100) and up get a logo on the wall: send us a file and it replaces the initials on the card.</p>
  </div>
</section>
"""


BODY = f"""
{page_hero(
    "Sponsorship",
    "Help us buy parts.",
    "We're a second-year club with a real parts bill. Sponsorship pays for motors, batteries, filament, tools, entry fees, and travel. Depending on the level, your name can go on the robot, the shirts, and the site.",
    "Sponsor packet",
    PACKET_NOTE,
    "Sponsors",
)}

{DONATE_SECTION}

<section class="section section--paper" aria-labelledby="why">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Why sponsor</p>
        <h2 id="why">A small team<br>with a real budget.</h2>
        <p class="lead" style="margin-top:1.4rem">A combat robot is not free. Motors, speed controllers, batteries, filament, tools, and entry fees add up fast. Your support lets students build a robot, test it, break it, and fix it.</p>
        <p>We're a second-year club, and the first names are already on the <a href="#donors">donor wall</a>. Local businesses and families can help us get the parts we need. You don't need to be a robotics company.</p>
        <div class="tag-row" style="margin-top:1.5rem">
          <span class="tag tag--accent">Local business</span>
          <span class="tag">In-kind welcome</span>
          <span class="tag">Any amount</span>
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <div class="cost-box">
          <p class="kicker">What your money buys</p>
          <h3>Parts and fees.</h3>
          <ul class="cost-list">
            <li><span>Drive motor</span><span>$20&ndash;$40</span></li>
            <li><span>Speed controller</span><span>$20&ndash;$35</span></li>
            <li><span>Battery</span><span>$25&ndash;$50</span></li>
            <li><span>Filament spool</span><span>$20&ndash;$25</span></li>
            <li><span>Event entry fee</span><span>$50&ndash;$150</span></li>
            <li><span>Team shirt</span><span>$15&ndash;$25</span></li>
          </ul>
          <p class="small muted" style="margin-top:1rem">Ballpark prices. We'll share the actual budget when we talk.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" id="tiers" aria-labelledby="tiers-heading">
  <div class="container">
    <div class="section-head section-head--center">
      <p class="kicker">Sponsorship levels</p>
      <h2 id="tiers-heading">Pick a level.</h2>
      <p class="head-copy" style="text-align:center">Every level is a one-time gift. Custom amounts and in-kind donations are welcome.</p>
    </div>
    <div class="tier-grid">
      {tier_cards}
    </div>
    <p class="small muted" style="margin-top:1.25rem">We're looking for our first sponsors. If you commit before the shirt and robot orders, your logo makes the first batch. Email us for the current deadline.</p>
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
        <p class="lead">Your name goes on the robot, the shirts, and the site. You also get to see the robot your money built.</p>
      </div>
    </div>
    <div class="benefits-wrap">
      <table class="benefits">
        <caption class="visually-hidden">Sponsorship benefits by level</caption>
        <thead>
          <tr>
            <th scope="col">Benefit</th>
            <th scope="col">Supporter<br><span class="table-price">$100</span></th>
            <th scope="col">Partner<br><span class="table-price">$250</span></th>
            <th scope="col">Builder<br><span class="table-price">$500</span></th>
            <th scope="col">Champion<br><span class="table-price">$1,000</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><th scope="row">Name on the team website</th><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Thank-you on Instagram</th><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Logo on the team website</th><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Logo on team shirts</th><td>—</td><td>✓</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Logo on the robot</th><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Banner at events</th><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Business spotlight post</th><td>—</td><td>—</td><td>✓</td><td>✓</td></tr>
          <tr><th scope="row">Robot demo at your business</th><td>—</td><td>—</td><td>—</td><td>✓</td></tr>
        </tbody>
      </table>
    </div>
    <p class="small muted" style="margin-top:1rem">Logo placement depends on the shirt and robot order dates. We'll confirm the details before you give.</p>
  </div>
</section>

<section class="section section--white" id="sponsor-form" aria-labelledby="inquiry">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div class="reveal">
        <p class="kicker">Start a conversation</p>
        <h2 id="inquiry">Tell us what<br>you'd like to support.</h2>
        <p class="lead" style="margin-top:1.4rem">Send a note and we'll follow up with the packet, a budget, and next steps. If you're not sure about a level, choose &ldquo;Not sure yet.&rdquo;</p>
        <div class="info-list" style="margin-top:1.75rem">
          <div class="info-row"><dt>Email</dt><dd><a href="mailto:{EMAIL_SPONSORS}">{EMAIL_SPONSORS}</a></dd></div>
          <div class="info-row"><dt>Partnerships</dt><dd><a href="mailto:{EMAIL_PARTNERSHIPS}">{EMAIL_PARTNERSHIPS}</a></dd></div>
          <div class="info-row"><dt>Phone</dt><dd><a href="{PHONE_TEL}">{PHONE}</a> &mdash; call or text</dd></div>
          <div class="info-row"><dt>Instagram</dt><dd><a href="{INSTAGRAM}" target="_blank" rel="noopener">{INSTAGRAM_HANDLE}</a></dd></div>
          <div class="info-row"><dt>Mail</dt><dd>River Valley High School<br>Attn: Robotics<br>801 El Margarita Rd.<br>Yuba City, CA 95993</dd></div>
        </div>
        <div class="callout callout--light" style="margin-top:1.5rem">
          In-kind donations are welcome too: aluminum, fasteners, filament, machining time, printing, or food for a build night.
        </div>
      </div>
      <div class="reveal" style="--d:100ms">
        <form class="form-card" data-mailto="{EMAIL_SPONSORS}" data-subject="Sponsorship inquiry — River Valley Robotics">
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
                <option value="Supporter — $100">Supporter &mdash; $100</option>
                <option value="Partner — $250">Partner &mdash; $250</option>
                <option value="Builder — $500">Builder &mdash; $500</option>
                <option value="Champion — $1,000">Champion &mdash; $1,000</option>
                <option value="Custom / in-kind">Custom or in-kind</option>
              </select>
            </div>
            <div class="field field--full">
              <label for="message">What would you like to support? <span class="optional">(optional)</span></label>
              <textarea id="message" name="message" placeholder="Tell us about your business, your goals, or the kind of support you have in mind."></textarea>
            </div>
          </div>
          <div class="form-foot">
            <p class="form-note">This form opens your email app with the details filled in. Prefer to write directly? Email <a href="mailto:{EMAIL_SPONSORS}">{EMAIL_SPONSORS}</a>.</p>
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
        <p class="lead">Need something that isn't here? Email or call us and we'll give you a straight answer.</p>
      </div>
    </div>
    <div class="faq">
      <details>
        <summary>How do I donate online?</summary>
        <p>Use the form at the top of this page, or open <a href="{DONATE_URL}" target="_blank" rel="noopener">hcb.hackclub.com/donations/start/{HCB_SLUG}</a> in a new tab. You can give any amount, one time or monthly. Hack Club Bank hosts the form, the receipts, and the public ledger.</p>
      </details>
      <details>
        <summary>Is my donation tax deductible?</summary>
        <p>Online gifts are tax-deductible through Hack Club Bank, a 501(c)(3). You'll get an emailed receipt as soon as the gift clears, so keep it for your records. For checks, transfers, or in-kind support, talk to us first so we route the gift through the right account.</p>
      </details>
      <details>
        <summary>Can we donate materials or services instead of cash?</summary>
        <p>Yes. Aluminum, fasteners, filaments, tools, machining time, printing, food for a build night, and professional expertise are all useful. We'll work with you on an in-kind acknowledgement.</p>
      </details>
      <details>
        <summary>What does the money go toward?</summary>
        <p>Parts for the robot, shop supplies, tools that wear out, event entry fees, and travel. If you want your support to go toward something specific, tell us and we'll confirm it in writing.</p>
      </details>
      <details>
        <summary>How does the donor wall work?</summary>
        <p>The <a href="#donors">donor wall</a> reads our public Hack Club Bank ledger, so a new public gift appears there without anyone editing the site. Your name and level come from the donation. Levels follow total giving: Friend under $100, then Supporter at $100 (that level includes a logo on this page), Partner, Builder, and Champion. Anonymous gifts are listed as Anonymous. Send us a logo and we'll swap it in for your initials.</p>
      </details>
      <details>
        <summary>When is the deadline for logo placement?</summary>
        <p>Shirt and robot deadlines are set each season. Sponsor early to guarantee placement on both. Website and social recognition can be added year-round.</p>
      </details>
    </div>
  </div>
</section>

<section class="section section--tight section--forest">
  <div class="container">
    <div class="sponsor-cta" style="background:transparent;color:var(--white)">
      <div>
        <p class="kicker">Sponsor packet</p>
        <h2 style="color:var(--white)">Take the details with you.</h2>
        <p style="color:rgba(255,255,255,.72)">Levels, benefits, and contact info in one PDF.</p>
      </div>
      <div class="sponsor-cta-actions">
        <a class="btn btn--primary" href="assets/RVRobotics-Sponsorship-Packet.pdf">Download the packet {icon("download", "btn-arrow")}</a>
        <a class="btn btn--ghost" href="mailto:{EMAIL_SPONSORS}">Email us</a>
      </div>
    </div>
  </div>
</section>
"""
