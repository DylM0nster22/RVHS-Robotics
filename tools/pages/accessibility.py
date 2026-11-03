"""Accessibility statement page."""
from rvsite import icon, page_hero, EMAIL

TITLE = "Accessibility | River Valley Robotics"
DESCRIPTION = "River Valley Robotics is committed to making this website usable for everyone. Read our accessibility statement and how to request help."
ACTIVE = ""
FILENAME = "accessibility.html"

BODY = f"""
{page_hero(
    "Accessibility",
    "Built for everyone.",
    "We want every student, family member, and community member to be able to use this site and take part in the team.",
    "Questions?",
    f"Email <a href=\"mailto:{EMAIL}\" style=\"color:var(--gold)\">{EMAIL}</a> or call the RVHS front office at (530) 822-2500.",
    "Accessibility",
)}

<section class="section section--paper">
  <div class="container">
    <div class="feature-split feature-split--top">
      <div>
        <p class="kicker">Our commitment</p>
        <h2>Clear, usable,<br>and welcoming.</h2>
        <p class="lead" style="margin-top:1.4rem">This site aims to meet the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA. That means readable contrast, keyboard-friendly navigation, meaningful link text, captions and alt text for images, and layouts that work on phones and with screen readers.</p>
        <p>Accessibility is an ongoing process, not a one-time checklist. If something doesn't work for you, we want to know.</p>
      </div>
      <div>
        <div class="info-list">
          <div class="info-row"><dt>Keyboard</dt><dd>All navigation, forms, and the photo viewer can be used without a mouse.</dd></div>
          <div class="info-row"><dt>Motion</dt><dd>Animations are reduced or turned off when your device requests reduced motion.</dd></div>
          <div class="info-row"><dt>Contrast</dt><dd>Text and controls are designed for strong contrast in the default theme.</dd></div>
          <div class="info-row"><dt>Images</dt><dd>Decorative images are hidden from assistive tech; meaningful images have descriptions.</dd></div>
          <div class="info-row"><dt>Forms</dt><dd>Every field has a visible label and a clear error path.</dd></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">Request help</p>
        <h2>Tell us what<br>you need.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">Need this information in another format, want to report a barrier, or need an accommodation to take part in the team? Contact us and we'll work on it.</p>
        <p>For district-level accessibility concerns, contact Yuba City Unified School District at <a href="https://www.ycusd.org/" target="_blank" rel="noopener">ycusd.org</a>.</p>
        <div style="margin-top:1.5rem; display:flex; flex-wrap:wrap; gap:.75rem">
          <a class="btn btn--dark" href="mailto:{EMAIL}?subject=Website%20accessibility">Email the team {icon("mail", "btn-arrow")}</a>
          <a class="btn btn--outline" href="contact.html">Contact page</a>
        </div>
      </div>
    </div>
    <div class="callout callout--light">
      This site is maintained by students. We fix issues as quickly as we can, usually within a few school days.
    </div>
  </div>
</section>
"""
