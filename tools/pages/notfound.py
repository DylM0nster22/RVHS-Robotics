"""404 page."""
from rvsite import icon

TITLE = "Page not found | River Valley Robotics"
DESCRIPTION = "That page isn't on the field. Return to the River Valley Robotics home page."
ACTIVE = ""
FILENAME = "404.html"
ROBOTS = "noindex, follow"

BODY = f"""
<section class="page-hero" style="min-height:78svh;display:flex;align-items:center">
  <div class="container">
    <p class="kicker">Error 404</p>
    <h1 style="font-size:clamp(5rem,18vw,14rem);line-height:.8;margin-bottom:1rem">Off the<br><span style="color:var(--gold)">field.</span></h1>
    <p class="lead">This page isn't part of the build. It may have moved, or the link may be wrong.</p>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.75rem">
      <a class="btn btn--primary" href="index.html">Back to home {icon("arrow", "btn-arrow")}</a>
      <a class="btn btn--ghost" href="contact.html">Report a broken link</a>
    </div>
  </div>
</section>
"""
