"""Printable sponsorship packet (also exported to PDF)."""

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>River Valley Robotics — 2026–27 Sponsorship Packet</title>
<meta name="description" content="Sponsorship levels, benefits, and contact information for River Valley Robotics at River Valley High School, Yuba City.">
<style>
  @font-face { font-family: "Barlow Condensed"; font-weight: 600; src: url("assets/fonts/barlow-condensed-600.woff2") format("woff2"); }
  @font-face { font-family: "Barlow Condensed"; font-weight: 700; src: url("assets/fonts/barlow-condensed-700.woff2") format("woff2"); }
  @font-face { font-family: "Barlow Condensed"; font-weight: 800; src: url("assets/fonts/barlow-condensed-800.woff2") format("woff2"); }
  @font-face { font-family: "Inter"; font-weight: 400 700; src: url("assets/fonts/inter-var.woff2") format("woff2"); }

  :root {
    --ink: #101512;
    --forest: #173d20;
    --green: #1f5c2e;
    --accent: #8fca9f;
    --accent-deep: #23643a;
    --paper: #f3f5f2;
    --line: rgba(16, 21, 18, 0.16);
    --muted: #5a665e;
  }
  * { box-sizing: border-box; }
  html { background: #dfe4e0; }
  body {
    margin: 0;
    font-family: "Inter", -apple-system, "Segoe UI", Arial, sans-serif;
    font-size: 9.6pt;
    line-height: 1.5;
    color: var(--ink);
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  h1, h2, h3, h4 {
    margin: 0;
    font-family: "Barlow Condensed", "Arial Narrow", sans-serif;
    text-transform: uppercase;
    line-height: 0.95;
    letter-spacing: 0.01em;
  }
  p { margin: 0 0 0.55em; }
  p:last-child { margin-bottom: 0; }
  a { color: var(--forest); text-decoration: none; }
  ul { margin: 0; padding: 0; list-style: none; }

  .toolbar {
    position: sticky; top: 0; z-index: 10;
    display: flex; justify-content: space-between; align-items: center; gap: 1rem;
    padding: 0.75rem 1.25rem;
    background: var(--ink); color: #fff;
    font-size: 12px;
  }
  .toolbar a { color: rgba(255,255,255,.75); }
  .toolbar a:hover { color: #fff; }
  .toolbar button {
    border: 0; background: var(--accent); color: var(--ink);
    font: 700 11px/1 "Inter", sans-serif; letter-spacing: .1em; text-transform: uppercase;
    padding: 0.7rem 1rem; cursor: pointer;
  }
  .pages { padding: 28px 12px 48px; }

  .page {
    position: relative;
    width: 8.5in;
    min-height: 11in;
    margin: 0 auto 28px;
    padding: 0.55in 0.6in 0.5in;
    background: #fff;
    box-shadow: 0 10px 40px rgba(0,0,0,.18);
    overflow: hidden;
  }

  .p-head {
    display: flex; align-items: center; justify-content: space-between; gap: 1rem;
    padding-bottom: 10px; border-bottom: 2px solid var(--forest);
  }
  .p-brand { display: flex; align-items: center; gap: 10px; }
  .p-brand img { height: 46px; width: auto; }
  .p-brand strong {
    display: block; font-family: "Barlow Condensed", sans-serif; font-size: 21px;
    font-weight: 700; letter-spacing: .08em; line-height: .95; text-transform: uppercase;
  }
  .p-brand span { display: block; font-size: 7.5px; letter-spacing: .2em; text-transform: uppercase; color: var(--muted); margin-top: 2px; }
  .p-head-right { text-align: right; font-size: 7.5px; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); line-height: 1.7; }

  .cover {
    position: relative;
    margin: 18px 0 14px;
    padding: 26px 28px 24px;
    background: var(--forest);
    color: #fff;
    overflow: hidden;
  }
  .cover::after {
    content: ""; position: absolute; right: -60px; top: -80px;
    width: 260px; height: 260px; border: 1px solid rgba(255,255,255,.14); border-radius: 50%;
    box-shadow: 0 0 0 40px rgba(255,255,255,.03), 0 0 0 80px rgba(255,255,255,.02);
  }
  .cover .kicker { color: var(--accent); }
  .cover h1 { font-size: 54px; font-weight: 800; max-width: 8em; margin: 8px 0 10px; }
  .cover p { color: rgba(255,255,255,.78); max-width: 40em; font-size: 10.5px; }
  .cover .meta { display: flex; flex-wrap: wrap; gap: 18px; margin-top: 16px; font-size: 7.5px; letter-spacing: .13em; text-transform: uppercase; color: rgba(255,255,255,.55); }
  .cover .meta strong { color: var(--accent); font-weight: 600; }

  .photo-strip { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-bottom: 16px; }
  .photo-strip img { width: 100%; height: 1.35in; object-fit: cover; display: block; }

  .kicker {
    display: inline-flex; align-items: center; gap: 7px;
    font-size: 7px; font-weight: 700; letter-spacing: .2em; text-transform: uppercase;
    color: var(--green); margin: 0 0 7px;
  }
  .kicker::before { content: ""; width: 18px; height: 2px; background: var(--accent-deep); }

  .two { display: grid; grid-template-columns: 1.2fr .8fr; gap: 26px; }
  .three { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
  .four { display: grid; grid-template-columns: repeat(4, 1fr); gap: 9px; }

  h2 { font-size: 26px; font-weight: 700; margin-bottom: 7px; }
  h3 { font-size: 14px; font-weight: 700; letter-spacing: .03em; margin-bottom: 4px; }
  .lead { font-size: 10.5px; color: #333; }

  .cost-box { border: 1px solid var(--line); border-top: 3px solid var(--green); padding: 11px 12px; }
  .cost-list { display: grid; gap: 3px; margin-top: 5px; }
  .cost-list li { display: flex; justify-content: space-between; gap: 8px; padding-bottom: 3px; border-bottom: 1px solid var(--line); font-size: 7.8px; }
  .cost-list li:last-child { border-bottom: 0; padding-bottom: 0; }
  .cost-list b { font-family: "Barlow Condensed", sans-serif; font-size: 10px; }

  .tier {
    border: 1px solid var(--line); border-top: 4px solid var(--forest);
    padding: 12px 11px; display: flex; flex-direction: column; gap: 6px;
  }
  .tier .name { font-family: "Barlow Condensed", sans-serif; font-size: 16px; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; }
  .tier .price { font-family: "Barlow Condensed", sans-serif; font-size: 30px; font-weight: 700; line-height: .9; color: var(--forest); }
  .tier .price small { font-family: "Inter", sans-serif; font-size: 7px; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); }
  .tier p { font-size: 7.8px; color: var(--muted); }
  .tier ul { display: grid; gap: 3px; margin-top: 2px; }
  .tier li { position: relative; padding-left: 9px; font-size: 7.6px; line-height: 1.4; }
  .tier li::before { content: ""; position: absolute; left: 0; top: .45em; width: 4px; height: 4px; background: var(--accent-deep); }

  table { width: 100%; border-collapse: collapse; font-size: 7.8px; }
  th, td { padding: 5px 6px; border-bottom: 1px solid var(--line); text-align: left; }
  thead th { background: var(--forest); color: #fff; font-size: 6.6px; letter-spacing: .09em; text-transform: uppercase; }
  thead th:not(:first-child) { text-align: center; }
  tbody td { text-align: center; color: var(--green); font-weight: 700; }
  tbody th { font-weight: 400; color: #333; }
  tbody tr:nth-child(even) { background: rgba(16,21,18,.025); }

  .next { counter-reset: n; display: grid; gap: 7px; }
  .next li { position: relative; padding-left: 26px; font-size: 8.4px; }
  .next li::before {
    counter-increment: n; content: counter(n, decimal-leading-zero);
    position: absolute; left: 0; top: 0; font-family: "Barlow Condensed", sans-serif;
    font-size: 13px; font-weight: 700; color: var(--accent-deep);
  }
  .next strong { display: block; font-size: 8.6px; }

  .contact-box { margin-top: 10px; padding: 12px 14px; background: var(--paper); border-left: 3px solid var(--accent-deep); font-size: 8.4px; }
  .contact-box .big { font-family: "Barlow Condensed", sans-serif; font-size: 16px; font-weight: 700; letter-spacing: .03em; }
  .fine { margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--line); font-size: 5.9px; line-height: 1.55; color: #7a827d; }
  .foot { display: flex; justify-content: space-between; gap: 10px; align-items: center; margin-top: 14px; padding-top: 8px; border-top: 1px solid var(--line); font-size: 6.6px; letter-spacing: .09em; text-transform: uppercase; color: var(--muted); }
  .school { display: flex; align-items: center; gap: 8px; }
  .school img { width: 28px; height: 28px; }

  @page { size: Letter; margin: 0; }
  @media print {
    html, body { background: #fff; }
    .toolbar { display: none; }
    .pages { padding: 0; }
    .page { margin: 0; box-shadow: none; width: 8.5in; min-height: 11in; page-break-after: always; }
    .page:last-child { page-break-after: auto; }
    a { color: inherit; }
  }
</style>
</head>
<body>
<div class="toolbar">
  <a href="index.html">&larr; Back to rvrobotics.ycusd.org</a>
  <button type="button" onclick="window.print()">Print / Save as PDF</button>
</div>
<div class="pages">

  <!-- PAGE 1 -->
  <article class="page">
    <header class="p-head">
      <div class="p-brand">
        <img src="assets/img/logo-mark.webp" alt="">
        <div>
          <strong>River Valley Robotics</strong>
          <span>River Valley High School &middot; Yuba City, CA</span>
        </div>
      </div>
      <div class="p-head-right">
        Sponsorship packet<br>
        2026&ndash;27 season
      </div>
    </header>

    <section class="cover">
      <p class="kicker">Partner with the club</p>
      <h1>Sponsor<br>the build.</h1>
      <p>River Valley Robotics is a student club at River Valley High School. We design, build, and drive small combat robots. Your support pays for the parts, tools, and entry fees that keep the build moving.</p>
      <div class="meta">
        <span><strong>2nd</strong> season</span>
        <span><strong>408</strong> shop</span>
        <span><strong>Thu &amp; Fri</strong> meetings</span>
        <span><strong>9&ndash;12</strong> grades</span>
      </div>
    </section>

    <div class="photo-strip">
      <img src="assets/img/packet-robot.jpg" alt="The assembled combat robot">
      <img src="assets/img/packet-cad.jpg" alt="CAD model of the robot">
      <img src="assets/img/packet-soldering.jpg" alt="A student soldering a robot part">
    </div>

    <div class="two">
      <div>
        <p class="kicker">Who we are</p>
        <h2>A small club.<br>A real build.</h2>
        <p class="lead">The club started in fall 2025. Students handle the CAD, the 3D printing, the wiring, and the driving. You don't need experience to start.</p>
        <p>Sponsors make the season possible. Your support covers the parts, tools, fees, and travel that turn an after-school club into a real build.</p>
      </div>
      <div class="cost-box">
        <p class="kicker">What your support buys</p>
        <h3>Parts and fees.</h3>
        <ul class="cost-list">
          <li><span>Drive motor</span><b>$20&ndash;$40</b></li>
          <li><span>Speed controller</span><b>$20&ndash;$35</b></li>
          <li><span>Battery</span><b>$25&ndash;$50</b></li>
          <li><span>Filament spool</span><b>$20&ndash;$25</b></li>
          <li><span>Event entry fee</span><b>$50&ndash;$150</b></li>
          <li><span>Team shirt</span><b>$15&ndash;$25</b></li>
        </ul>
        <p style="margin-top:6px;font-size:6.8px;color:var(--muted)">Ballpark prices. We'll share the actual budget when we talk.</p>
      </div>
    </div>

    <div class="foot">
      <div class="school"><img src="assets/img/rvhs-logo.png" alt=""><span>River Valley High School &middot; Home of the Falcons</span></div>
      <span>rvrobotics.ycusd.org</span>
    </div>
  </article>

  <!-- PAGE 2 -->
  <article class="page">
    <header class="p-head">
      <div class="p-brand">
        <img src="assets/img/logo-mark.webp" alt="">
        <div>
          <strong>River Valley Robotics</strong>
          <span>Sponsorship levels &amp; benefits</span>
        </div>
      </div>
      <div class="p-head-right">
        2026&ndash;27<br>
        rvrobotics.ycusd.org
      </div>
    </header>

    <div style="margin-top:16px">
      <p class="kicker">Sponsorship levels</p>
      <h2>Pick a level.</h2>
      <div class="four" style="margin-top:9px">
        <div class="tier">
          <div class="name">Supporter</div>
          <div class="price">$100<small> one-time</small></div>
          <p>A straightforward way to help with parts.</p>
          <ul><li>Name on the team website</li><li>Thank-you on Instagram</li><li>Team sticker</li></ul>
        </div>
        <div class="tier">
          <div class="name">Partner</div>
          <div class="price">$250<small> one-time</small></div>
          <p>Put your name in front of the school.</p>
          <ul><li>Everything in Supporter</li><li>Logo on the website</li><li>Logo on team shirts</li><li>Build night invitation</li></ul>
        </div>
        <div class="tier">
          <div class="name">Builder</div>
          <div class="price">$500<small> one-time</small></div>
          <p>Put your logo on the robot itself.</p>
          <ul><li>Everything in Partner</li><li>Logo on the robot</li><li>Banner at events</li><li>Business spotlight post</li></ul>
        </div>
        <div class="tier">
          <div class="name">Champion</div>
          <div class="price">$1,000<small> one-time</small></div>
          <p>The top level. Help cover the season.</p>
          <ul><li>Everything in Builder</li><li>Presenting placement</li><li>Robot demo at your business</li><li>First pick of demo dates</li></ul>
        </div>
      </div>
    </div>

    <div style="margin-top:16px">
      <p class="kicker">Benefits at a glance</p>
      <table>
        <thead>
          <tr><th>Benefit</th><th>Supporter<br>$100</th><th>Partner<br>$250</th><th>Builder<br>$500</th><th>Champion<br>$1,000</th></tr>
        </thead>
        <tbody>
          <tr><th>Name on the team website</th><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Thank-you on Instagram</th><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Logo on the team website</th><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Logo on team shirts</th><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Logo on the robot</th><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Banner at events</th><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Business spotlight post</th><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td><td>&#10003;</td></tr>
          <tr><th>Robot demo at your business</th><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&#10003;</td></tr>
        </tbody>
      </table>
      <p style="margin-top:5px;font-size:6.8px;color:var(--muted)">Logo placement depends on the shirt and robot order dates. We'll confirm the details before you give.</p>
    </div>

    <div class="two" style="margin-top:16px;grid-template-columns:1fr 1fr">
      <div>
        <p class="kicker">Other ways to help</p>
        <h3>Cash is not the only way.</h3>
        <ul style="display:grid;gap:4px;font-size:8px;margin-top:5px">
          <li>&bull; Materials: aluminum, fasteners, filament, electronics</li>
          <li>&bull; Services: machining, printing, photography, food</li>
          <li>&bull; Expertise: mentoring, shop supervision, career talks</li>
          <li>&bull; Access: a tour, a demo, or a real problem to solve</li>
        </ul>
      </div>
      <div>
        <p class="kicker">Next steps</p>
        <ol class="next">
          <li><strong>Reach out.</strong> Email or call to tell us what you'd like to support.</li>
          <li><strong>Pick a level.</strong> We'll confirm benefits and recognition details.</li>
          <li><strong>Get recognized.</strong> We'll coordinate logos, shirts, and the robot.</li>
        </ol>
      </div>
    </div>

    <div class="contact-box">
      <div class="big">Ready to sponsor? Let's talk.</div>
      <p>Email <a href="mailto:rvrobotics@ycusd.org">rvrobotics@ycusd.org</a> &nbsp;&middot;&nbsp; RVHS front office: <a href="tel:+15308222500">(530) 822-2500</a><br>
      River Valley High School, Attn: Robotics, 801 El Margarita Rd., Yuba City, CA 95993</p>
      <p style="margin-top:4px"><a href="https://rvrobotics.ycusd.org/sponsors.html">rvrobotics.ycusd.org/sponsors</a></p>
    </div>

    <div class="fine">
      Ask us about current tax-deductible giving options and receipts before you give; donations may be processed through the RVHS Booster Club or the district depending on the type of support. Sponsorship recognition is subject to team, school, and district approval. Yuba City Unified School District prohibits discrimination, harassment, intimidation, and bullying based on actual or perceived race, color, ethnicity, national origin, immigration status, ancestry, age, creed, religion, political affiliation, gender, gender identity, gender expression, genetic information, mental or physical disability, sex, sexual orientation, marital status, pregnancy or parental status, medical information, military veteran status, or any other basis protected by law or regulation.
    </div>
    <div class="foot">
      <div class="school"><img src="assets/img/rvhs-logo.png" alt=""><span>River Valley High School &middot; Yuba City Unified School District</span></div>
      <span>2026&ndash;27</span>
    </div>
  </article>

</div>
</body>
</html>
"""
