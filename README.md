# River Valley Robotics — website

The official website for **River Valley Robotics**, the student combat robotics club at
River Valley High School in Yuba City, California.

**Target address:** <https://rvrobotics.ycusd.org>

The site is plain HTML, CSS, and JavaScript. There is no server-side code and no
build step required to host it.

---

## What's included

| Page | Purpose |
| --- | --- |
| `index.html` | Home, what students do, shop photos, sponsor CTA, meeting CTA |
| `about.html` | Club story, student work, meeting details, FAQ |
| `robots.html` | Current build, CAD and shop photos, build process, shop rules, next steps |
| `cad.html` | Interactive 3D CAD viewer for the 3lb vertical spinner and the other public combat robots with STEP files |
| `sponsors.html` | Donate online through Hack Club Bank, live donor wall with names, logos, and levels, why sponsor, parts costs, levels, benefits table, inquiry form, FAQ |
| `gallery.html` | All team photos and flyers from Instagram, with a keyboard-friendly lightbox |
| `watch.html` | Match video archive: 11 fights from Impact Robotics League #1 2026, plus newer YouTube picks |
| `join.html` | Student and parent/mentor info, meeting details, interest form, FAQ |
| `contact.html` | Contact methods, general inquiry form, map |
| `credits.html` | Photo, CAD, font, illustration, and software credits |
| `accessibility.html` | Accessibility statement and how to request help |
| `404.html` | Friendly not-found page |
| `sponsor-packet.html` | Printable 2-page sponsorship packet (screen + print styles) |
| `assets/RVRobotics-Sponsorship-Packet.pdf` | Ready-to-send PDF version of the packet |

Supporting files: `css/site.css`, `js/site.js`, self-hosted fonts, optimized images,
web-optimized match video in `assets/video/`, `site.webmanifest`, `robots.txt`, and
`sitemap.xml`.

The CAD lab also uses `js/cad-viewer.js`, self-hosted Three.js modules in
`assets/js/vendor/`, and converted models and thumbnails in `assets/models/`.
Everything is static; the browser loads one GLB at a time.

---

## Preview locally

From this folder:

```powershell
python -m http.server 8080
```

Open <http://localhost:8080/>. The PDF and all relative links work over the local server.

You can also open `index.html` directly, but a local server is closer to the real host.

---

## Deploy

Upload the **contents** of this folder to the web root for `rvrobotics.ycusd.org`,
keeping the folder structure:

```
*.html
css/
js/
assets/
site.webmanifest
robots.txt
sitemap.xml
```

`tools/` and `source/` are working files. They do not need to be uploaded. Nothing
here needs Node, PHP, a database, or a build command on the server. The files in
`assets/video/` are already compressed for the web; ffmpeg is only needed when you
replace them.

Forms are `mailto:` forms: they open the visitor's email app with the message
pre-filled. If the district prefers a hosted form service (Google Forms, Microsoft
Forms, Formspree, etc.), replace the form `action`/JavaScript handler and update the
"this opens your email app" notes.

### Hosting on rvhsrobotics.com

The site runs on Cloudflare as a **Worker with static assets** (the Git-connected
static app the dashboard creates). The deploy settings live in `wrangler.jsonc`
so they travel with the repository:

| Setting | Value |
| --- | --- |
| Worker name | `rvhs-robotics` |
| Production branch | `main` |
| Build command | `python3 tools/stage.py` |
| Deploy command | `npx wrangler deploy` (default) |
| Assets directory | `./dist` |
| Not-found page | `dist/404.html` |

`wrangler.jsonc` is what keeps the deploy clean. Without it, Wrangler defaults to
the repository root and publishes `tools/`, `source/`, `.openchamber/`, and the
`dist/` copy along with the real pages.

The domain has to be a Cloudflare zone before a Custom Domain can be attached:

1. Cloudflare dashboard → Add a site → `rvhsrobotics.com` → Free plan.
2. At Porkbun, replace the four `*.ns.porkbun.com` nameservers with the two
   Cloudflare gives you. Keep the registrar and email settings; DNSSEC stays off.
3. After the zone is active, delete the Porkbun parking records (apex A records to
   `207.207.210.*`, `www` CNAME to `uixie.porkbun.com`). Keep MX and TXT.
4. Worker → Settings → Domains & Routes → Add custom domain → `rvhsrobotics.com`.
   Add `www.rvhsrobotics.com` too, then redirect www to the apex with a Redirect
   Rule.
5. Change `SITE_URL` in `tools/rvsite.py` to `https://rvhsrobotics.com`, run
   `python tools/build.py`, regenerate the packet PDF, and push.

To check the deployable folder locally, run `python tools/stage.py` and serve
`dist/` with `python -m http.server 8080 --directory dist`.

Once the custom domain works, set `workers_dev` and `preview_urls` to `false` in
`wrangler.jsonc` if the `*.workers.dev` address should stop being public.

What Cloudflare does and does not fix:

- **It does** give the site HTTPS, caching, and a public address that the district
  filter does not control. A district-managed network or device can still block or
  allow `rvhsrobotics.com` by category, so ask the site administrator to approve
  and allowlist the domain before a launch.
- **It does not** unblock Hack Club Bank. The donation iframe and the donor-wall
  fetch both go to `hcb.hackclub.com`, and K-12 filters often put finance and
  payment domains in a blocked category. The embedded form has a direct-link
  fallback and the wall keeps its build-time snapshot when the live fetch fails,
  so the page still works, but visitors on a school network may not be able to
  donate. Card payments on a school device may also be against district policy;
  treat the page as something families open at home.
- A small Cloudflare Worker on your own domain can proxy
  `GET /api/donations` to the HCB API and cache it, which keeps the wall current
  even where the HCB API is blocked. The hosted donation form itself has to stay
  on `hcb.hackclub.com`; do not try to proxy the card form.
- Moving the site to a domain the district does not manage means the school's
  approval rules still apply to student photos, sponsor logos, and the sponsor
  packet. Get that approval before pointing the domain at it.

---

## Donations (Hack Club Bank)

Online donations run through **Hack Club Bank (HCB)**, Hack Club's 501(c)(3) fiscal
sponsor. `sponsors.html` embeds HCB's hosted donation form and builds the donor wall
from HCB's public donations API. Both update on their own.

- Donation form: <https://hcb.hackclub.com/donations/start/rvhs-robotics-club>
- Public ledger: <https://hcb.hackclub.com/rvhs-robotics-club>
- Donations API: <https://hcb.hackclub.com/api/v3/organizations/rvhs-robotics-club/donations>
- Donor graph (fallback image): <https://graph.hcb.hackclub.com/rvhs-robotics-club>

The slug lives in `tools/rvsite.py` as `HCB_SLUG` and is shared by the page modules.
If the HCB organization slug changes, update that one value, then run
`python tools/build.py`.

### Donor wall

The wall groups every **public** gift by level and shows the donor's name next
to their logo (or initials). Levels are based on total giving, so a monthly gift
adds up over the season:

| Level | Total given | On the wall |
| --- | --- | --- |
| Friend | under $100 | Name + initials |
| Supporter | $100 and up | Name + logo |
| Partner | $250 and up | Name + logo |
| Builder | $500 and up | Name + logo |
| Champion | $1,000 and up | Name + logo |

`Friend` is the catch-all for anyone under $100; it only exists on the wall, not
in the sponsorship packet. The $100 Supporter level includes the website logo,
so a $100 donor can send a file for their card.

The levels are generated from `TIERS` in `tools/pages/sponsors.py`, so changing a
tier price changes the wall thresholds too. The level tags under the wall, the
section headings, and the JavaScript refresh all read the same level data.

Two renderers keep the wall current:

- `tools/donors.py` fetches the donations API during `python tools/build.py` and
  writes a snapshot into `sponsors.html`, so the names are in the HTML without
  JavaScript. The response is cached in `tools/.cache/donors.json` and stands in
  when the build machine is offline.
- `js/donors.js` re-fetches the same API in the browser and replaces the snapshot.
  A new gift appears on the next page load — no rebuild, no redeploy.

If the live request fails (blocked network, CSP, HCB outage), the page keeps the
build-time snapshot. The HCB donor graph image is shown only when the build had no
donor data at all. Nothing needs to be updated by hand for a gift to appear.

### Sponsor names and logos

`assets/data/donors.json` maps an HCB donor name to what the site should show:

```json
{
  "sponsors": {
    "Acme Machine": {
      "display": "Acme Machine Co.",
      "logo": "assets/img/sponsors/acme-machine.png",
      "url": "https://acme.example",
      "tier": "Builder"
    }
  }
}
```

- Keys match the donor name on the HCB ledger (case does not matter).
- `display` renames the card; `url` links it; `logo` swaps the initials tile for
  the sponsor's mark. The donor's name stays on the card in every case.
- `tier` forces a level, which is useful for in-kind sponsors whose cash gifts do
  not match the level they were promised.
- `hide: true` removes a card.

Put logo files in `assets/img/sponsors/` (see the README there). The logo is the
$100 Supporter benefit, so add one for a Supporter or higher; donors without a
file show their initials, so a gift never needs a file to appear. Anonymous gifts
are grouped into a single "Anonymous" card.

The form is an iframe with a fixed height (`930px`, `990px` at 460px wide and below)
because HCB does not report its content height to the parent page. If HCB changes
the form layout, adjust `.donate-frame` in `css/site.css`. The panel also has a
direct link to the hosted donation page for browsers or networks that block
third-party frames.

If the school's web server sends a Content-Security-Policy, allow
`frame-src https://hcb.hackclub.com`, `connect-src https://hcb.hackclub.com`, and
`img-src https://graph.hcb.hackclub.com` or the form, the live wall, and the graph
fallback will be blocked. The frame also loads Stripe and Cloudflare Turnstile for
card processing and bot checks; HCB's page already permits them.

HCB does not support preselecting a donation amount in the URL, so the four sponsor
level buttons jump to the form and show the amount to enter. Card data is handled by
Stripe on HCB's page; the site never sees it. Checks, transfers, and in-kind gifts
still go through the sponsor inquiry form.

---

## Before you publish — review these

These details came from the team's Instagram or are sensible defaults. Confirm them
before the site goes live.

1. **Email address.** The site uses `rvrobotics@ycusd.org`. Confirm that address
   exists (or replace it) in `tools/rvsite.py` and in the sponsor packet. It appears
   in the footer, contact page, forms, packet, and structured data.
2. **Meeting details.** The site says **Thursdays and Fridays, Room 408**, based on
   the team's November 2026 Instagram update. Change `MEETINGS` and `ROOM` in
   `tools/rvsite.py` if that changes.
3. **Google Classroom.** The join page lists code **`gftqhxdh`** from the team's
   Instagram bio. Update if the class changes.
4. **Second year / combat robotics.** The copy is based on the November 2026 post
   ("2nd year of club robotics", `#combatrobotics`) plus the team's timeline: the
   first meeting was September 22, 2025; the first robots were built in 2026. Adjust
   the story, the About timeline, and the FAQ if the program changes.
5. **Sponsorship levels and prices.** The four levels ($100 / $250 / $500 / $1,000)
   and benefits are realistic starting points, not confirmed numbers. Adjust them in
   `tools/pages/sponsors.py`, the packet, and the PDF before soliciting sponsors.
6. **Parts costs.** The "What your money buys" list is a ballpark range for common
   parts and fees. Replace it with the team's actual quotes or budget when available.
7. **Sponsor logos.** The donor wall adds a card for every public gift
   automatically. Logos are opt-in: put a file in `assets/img/sponsors/` and point to
   it from `assets/data/donors.json`. Add a logo only after the sponsor confirms it
   and the school/district approves it.
8. **Instagram link.** The site links to <https://www.instagram.com/rv.robotics/>.
   Change `INSTAGRAM` in `tools/rvsite.py` if the handle changes.
9. **Photos.** All photos and flyers are from the team's Instagram, including the
   second-post carousel (shop, CAD, electronics, soldering, and the assembled robot).
   Add new photos to `source/instagram/` and run the image script (below), then update
   the gallery and captions.
10. **Match video.** The Watch page hosts 11 fights from Impact Robotics League #1
    2026. Confirm the team and the event organizer approve publishing the footage,
    and check with the school before uploading identifiable students. The newer
    YouTube picks are embedded, not copied. Follow the video workflow below to add
    or replace footage.
11. **Logo.** The official team logo is in `source/logo.jpg`. Re-run the logo script
    if a higher-resolution or updated version arrives.
12. **District approval.** School-hosted sites usually need approval for the logo,
    sponsor names, the PDF, and any external links. Check with the site administrator
    before launch.
13. **PDF.** Regenerate the PDF after any sponsor/packet edit (instructions below).
14. **CAD viewer.** Confirm the model authors and collaborators approve publishing the
    converted models and thumbnails, and check each GitHub repository's license before
    sharing or reusing geometry. The CAD lab links back to every source repo.
15. **HCB donation page.** The form is hosted at
    `hcb.hackclub.com/donations/start/rvhs-robotics-club`. Confirm the HCB
    organization is active and transparent, the page shows **RVHS Robotics Club**,
    and a test gift produces the tax receipt. If the HCB slug changes, update
    `HCB_SLUG` in `tools/rvsite.py` and rebuild.

The site intentionally does **not** invent student counts, mentor counts, awards, or
competition results. The team facts shown (second year, Room 408, grades 9–12,
no experience required) come from the team's Instagram. Sponsor prices and parts
costs are editable planning figures, not confirmed numbers.

---

## Editing content

The HTML files in the root are generated from the small Python page modules in
`tools/pages/`. You have two options:

### Option A — edit the page modules (recommended)

1. Edit a file in `tools/pages/` (or `tools/rvsite.py` for shared header/footer text).
2. Run:

   ```powershell
   python tools/build.py
   ```

3. Rebuild the PDF (see below) if you changed the packet.

### Option B - edit the HTML directly

The root `.html` files are complete and editable. This is fine for one-off changes,
but running `python tools/build.py` again will overwrite them with the page modules.
If you choose this route, stop using the generator.

When you change `css/site.css`, `js/site.js`, or the model/thumbnail assets, bump
`ASSET_VERSION` in `tools/rvsite.py` so browsers fetch the new files instead of
using their cache.

### Shared pieces

- `tools/rvsite.py` — header, footer, navigation, contact details, icons, layout.
- `tools/donors.py` — builds the donor wall snapshot from the HCB donations API.
- `tools/pages/home.py`, `about.py`, `robots.py`, `sponsors.py`, `gallery.py`,
  `watch.py`, `join.py`, `contact.py`, `credits.py`, `accessibility.py`,
  `notfound.py`, `packet.py`.
- `css/site.css` — all site styles and responsive breakpoints.
- `js/site.js` — mobile navigation, reveal animations, lightbox, tier prefill,
  and mailto forms.
- `js/donors.js` — refreshes the donor wall from Hack Club Bank on page load.

---

## Images and logo

The team's Instagram source images are in `source/instagram/`. The folder includes
the shop bench, CAD screenshots, electronics, soldering, the assembled robot, the
printed armor, and both flyers. The site uses optimized `.webp` versions in
`assets/img/`.

To re-crop and re-compress after adding new source photos:

```powershell
# 1. Put new source photos in source/instagram/
# 2. Edit the file names in tools/make-images.py if needed
python tools/make-images.py
```

This also rebuilds `assets/img/og.jpg` (the social sharing card).

To rebuild the logo assets, header mark, footer logo, and favicons from
`source/logo.jpg`:

```powershell
python tools/make-logo.py
```

This writes `assets/img/logo-mark.webp`, `logo-footer.webp`, and the app icons.
The full-resolution transparent logo is saved as `source/logo-full.png`.

To swap a gallery image, replace the matching file in `assets/img/` and update the
caption and alt text in `tools/pages/gallery.py` (then rebuild), or edit
`gallery.html` directly.

---

## Match video

The Watch page plays 11 locally hosted matches from Impact Robotics League #1 2026
and four newer YouTube picks. The local videos are 720p H.264 MP4s in
`assets/video/`; posters are in `assets/img/video/`. Total size is about 62 MB.
The page data (source file names, match names, durations, YouTube IDs) lives in
`tools/pages/watch.py`. The supplied 30-second announcement clip is not a match, so
it is intentionally left out of the archive.

The videos are committed, so rebuilding the site does **not** require ffmpeg. To add
or replace footage, use the preparation script:

```powershell
# 1. Put the original MP4s in a folder outside the repository.
# 2. Add or edit a row in LOCAL_VIDEOS in tools/pages/watch.py.
# 3. Point at ffmpeg and encode.
$env:FFMPEG = "C:\path\to\ffmpeg.exe"
python tools/make-videos.py --source "D:\path\to\match-footage" --force

# Rebuild the pages after the files exist.
python tools/build.py
```

The script writes `assets/video/<slug>.mp4`, a 1280×720 WebP poster for each match
(halfway through the fight), and reports the sizes. It uses CRF 30 video and 64 kbps
mono audio to keep the archive small; adjust the values in `encode_video()` if the
footage needs more detail.

Useful flags:

- `--skip-video` rebuilds posters only, without re-encoding the MP4s.
- `--youtube` refreshes the four YouTube thumbnail images from `i.ytimg.com`.
- `--force` overwrites existing MP4s. Without it, the script keeps files that are
  newer than their source.

The newer YouTube picks are privacy-enhanced embeds (`youtube-nocookie.com`) created
only when a visitor presses play. Update their IDs, titles, and durations in
`YOUTUBE_VIDEOS` in `tools/pages/watch.py`, then run `--youtube` if the thumbnails
changed.

The video player is in `js/site.js` (the `Video player` block) and the styles are in
`css/site.css` under `Watch / video`. Each card is a normal link to the MP4 or the
YouTube watch page, so the page still works if JavaScript is unavailable.

---

## 3D CAD viewer

`cad.html` is a static Three.js viewer. The 3lb vertical spinner is the featured
model; the library includes the other public combat robot builds with a full STEP
assembly. Model metadata (names, descriptions, specs, repo paths, camera angles,
and optional color overrides) lives in `tools/models.json`. The generated runtime
manifest is
`assets/models/manifest.json`, and the page embeds that data when it builds.

The browser loads one compressed GLB at a time. STEP files are converted ahead of
time with OpenCascade (`occt-import-js`), compressed with meshoptimizer
(`gltfpack`), and rendered with self-hosted Three.js modules. Nothing needs Node
on the web server.

To rebuild the model assets after changing `tools/models.json` or a model repo:

```powershell
# One time, installs the conversion tools (not needed to host the site).
cd tools
npm install

# From the project root: download STEP files, convert, and write the manifest.
node tools/make-models.mjs

# Rebuild the HTML so the new manifest and model views are embedded first.
python tools/build.py

# Optional but recommended: render new card thumbnails with Chrome or Edge.
node tools/make-model-thumbs.mjs
```

Useful flags:

- `node tools/make-models.mjs --only 3lb-vertical-spinner --force` rebuilds one model.
- `node tools/make-models.mjs --jobs 2` converts two models at once.
- `node tools/make-model-thumbs.mjs --only 3lb-vertical-spinner` re-renders one card.
- Set `CHROME_PATH` if Chrome or Edge is not in the default Windows location.

Some STEP exports lose colors on subassemblies even when the original CAD has them.
Add `nodeColors` (by assembly node name), `meshColors` (by mesh name), or
`colorReplacements` (from one existing color to another) to an entry in
`tools/models.json`, then rebuild. A `nodeColors` value can be a hex string to fill
uncolored parts, or `{ "color": "#...", "force": true }` to override colored parts
too. `meshColors` and `colorReplacements` always force the change.

Downloads are cached in `tools/.cache/models` (ignored by Git). The generated GLBs
and thumbnails are committed, so a normal deploy does not need Node or the source
STEP files. `assets/models/manifest.json` is generated; edit `tools/models.json`
instead.

Each model links to its public GitHub repository and original STEP file. Check the
repository's license before reusing geometry or design files. The viewer uses
Three.js and the meshoptimizer decoder, both MIT licensed; their notices are in
`assets/js/vendor/LICENSE-three.txt` and
`assets/js/vendor/LICENSE-meshoptimizer.txt`.

## Sponsorship packet PDF

The packet is designed as two US Letter pages. To regenerate the PDF from
`sponsor-packet.html` with Chrome or Edge:

```powershell
$pdf = (Resolve-Path 'assets').Path + '\RVRobotics-Sponsorship-Packet.pdf'
$html = (Resolve-Path 'sponsor-packet.html').Path -replace '\\','/'
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless=new --disable-gpu --no-pdf-header-footer `
  --print-to-pdf="$pdf" "file:///$html"
```

Or open `sponsor-packet.html` in a browser and choose **Print / Save as PDF** (the
page has a button for it). Keep the **Letter** paper size and **Background graphics**
enabled so the green/silver sections print.

After changing prices, benefits, or contact details in `tools/pages/packet.py`, run
`python tools/build.py` and then regenerate the PDF.

---

## Accessibility

The site targets WCAG 2.1 AA:

- Semantic headings and landmarks, skip link, visible focus styles.
- Keyboard-operable mobile menu and photo lightbox (Esc, arrow keys).
- Match videos never autoplay; they open in a native-controls player, and YouTube
  picks load only after the visitor chooses one.
- Reduced-motion support.
- Descriptive alt text and labelled form fields.
- Sufficient text/background contrast in the default theme.

If a school accessibility reviewer finds an issue, update `accessibility.html` and
the relevant component. The statement page invites visitors to report barriers.

---

## Content notes

- **Team name:** River Valley Robotics / RV Robotics.
- **School:** River Valley High School, 801 El Margarita Rd., Yuba City, CA 95993.
- **District:** Yuba City Unified School District.
- **Program:** student combat robotics club. First meeting September 22, 2025;
  first robots built in 2026; second year of the club as of 2026–27.
- **Donor wall:** built from HCB's public donations API and grouped by level
  (Friend under $100, then Supporter at $100 with a website logo, Partner,
  Builder, Champion). Names and logos come from `assets/data/donors.json`.
- **Meetings:** Thursdays and Fridays, Room 408 (source: team Instagram).
- **Instagram:** [@rv.robotics](https://www.instagram.com/rv.robotics/).
- **Google Classroom:** `gftqhxdh` (source: team Instagram bio).
- **Photos:** all photos and flyers come from the team's Instagram, including the
  second-post carousel (shop, CAD, electronics, soldering, and the assembled robot).
- **Match video:** 11 fights from Impact Robotics League #1 2026, plus newer videos
  from the [@BadPlants1](https://www.youtube.com/@BadPlants1) YouTube channel.
  Event names and match spellings come from the supplied files and video titles.
- **Colors:** school green, black, white, and silver, taken from the River Valley
  High School Falcons mark. No gold.

The site references combat robotics in general terms. It does not claim a specific
competition league, team number, awards, or match record.

---

## Credits

- Team photography and flyers: [@rv.robotics](https://www.instagram.com/rv.robotics/).
- Match footage: Impact Robotics League #1 2026, supplied for the site.
- YouTube match videos and thumbnails: [@BadPlants1](https://www.youtube.com/@BadPlants1).
- River Valley High School Falcons logo: River Valley High School / Yuba City Unified
  School District.
- Official team logo: River Valley Robotics (provided by the team).
- Typefaces: Barlow Condensed and Inter, SIL Open Font License 1.1, self-hosted.
- CAD models: [DylM0nster22's public GitHub repositories](https://github.com/DylM0nster22)
  and the listed collaborators. Check each repo for license terms.
- 3D viewer: Three.js and meshoptimizer, MIT licensed, self-hosted.
- Icons and page graphics: original work made for this site.

See `credits.html` for the public-facing version.
