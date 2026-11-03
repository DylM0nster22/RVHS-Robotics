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
| `index.html` | Home, mission, what we do, season, robot, sponsor CTA, gallery preview |
| `about.html` | Story, values, subteams, mentors, school information, FAQ |
| `robots.html` | Build process, subsystems, match day, safety, season archive |
| `sponsors.html` | Why sponsor, levels, benefits table, partner wall, inquiry form, FAQ |
| `gallery.html` | Team photos/flyers from Instagram with a keyboard-friendly lightbox |
| `join.html` | Student, parent, and mentor paths, meeting info, interest form, FAQ |
| `contact.html` | Contact methods, general inquiry form, map |
| `credits.html` | Photo, font, and illustration credits |
| `accessibility.html` | Accessibility statement and how to request help |
| `404.html` | Friendly not-found page |
| `sponsor-packet.html` | Printable 2-page sponsorship packet (screen + print styles) |
| `assets/RVRobotics-Sponsorship-Packet.pdf` | Ready-to-send PDF version of the packet |

Supporting files: `css/site.css`, `js/site.js`, self-hosted fonts, optimized images,
`site.webmanifest`, `robots.txt`, and `sitemap.xml`.

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
here needs Node, PHP, a database, or a build command on the server.

Forms are `mailto:` forms: they open the visitor's email app with the message
pre-filled. If the district prefers a hosted form service (Google Forms, Microsoft
Forms, Formspree, etc.), replace the form `action`/JavaScript handler and update the
"this opens your email app" notes.

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
4. **Second season / combat robotics.** The copy is based on the November 2026 post
   ("2nd year of club robotics", `#combatrobotics`). Adjust the story and FAQ if the
   program changes.
5. **Sponsorship levels and prices.** The four levels ($250 / $500 / $1,000 / $2,500+)
   and benefits are recommendations. Adjust them in `tools/pages/sponsors.py`, the
   packet, and the PDF before soliciting sponsors.
6. **Budget percentages.** The "typical season allocation" chart is illustrative
   (35/30/20/10/5). Replace it with the team's actual budget when available.
7. **Sponsor logos.** The partner wall currently says "Your logo here." Add real
   logos only after commitments are confirmed and the school/district approves their
   use.
8. **Instagram link.** The site links to <https://www.instagram.com/rv.robotics/>.
   Change `INSTAGRAM` in `tools/rvsite.py` if the handle changes.
9. **Photos.** All photos and flyers are from the team's Instagram. Add new photos to
   `source/instagram/` and run the image script (below), then update the gallery and
   captions.
10. **Logo.** The official team logo is in `source/logo.jpg`. Re-run the logo script
    if a higher-resolution or updated version arrives.
11. **District approval.** School-hosted sites usually need approval for the logo,
    sponsor names, the PDF, and any external links. Check with the site administrator
    before launch.
12. **PDF.** Regenerate the PDF after any sponsor/packet edit (instructions below).

The site intentionally does **not** invent student counts, mentor counts, awards, or
competition results. The team facts shown (second season, Room 408, grades 9–12,
zero experience required) come from the team's Instagram. Sponsor prices and budget
percentages are editable planning figures, not confirmed numbers.

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

### Option B — edit the HTML directly

The root `.html` files are complete and editable. This is fine for one-off changes,
but running `python tools/build.py` again will overwrite them with the page modules.
If you choose this route, stop using the generator.

### Shared pieces

- `tools/rvsite.py` — header, footer, navigation, contact details, icons, layout.
- `tools/pages/home.py`, `about.py`, `robots.py`, `sponsors.py`, `gallery.py`,
  `join.py`, `contact.py`, `credits.py`, `accessibility.py`, `notfound.py`,
  `packet.py`.
- `css/site.css` — all site styles and responsive breakpoints.
- `js/site.js` — mobile navigation, reveal animations, counters, lightbox,
  tier prefill, and mailto forms.

---

## Images and logo

The team's Instagram source images are in `source/instagram/`. The site uses optimized
`.webp` versions in `assets/img/`.

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

## Sponsorship packet PDF

The packet is designed as two US Letter pages. To regenerate the PDF from
`sponsor-packet.html` with Chrome or Edge:

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --headless=new --disable-gpu --no-pdf-header-footer `
  --print-to-pdf="assets\RVRobotics-Sponsorship-Packet.pdf" `
  "file:///$((Resolve-Path 'sponsor-packet.html').Path -replace '\\','/')"
```

Or open `sponsor-packet.html` in a browser and choose **Print / Save as PDF** (the
page has a button for it). Keep the **Letter** paper size and **Background graphics**
enabled so the green/gold sections print.

After changing prices, benefits, or contact details in `tools/pages/packet.py`, run
`python tools/build.py` and then regenerate the PDF.

---

## Accessibility

The site targets WCAG 2.1 AA:

- Semantic headings and landmarks, skip link, visible focus styles.
- Keyboard-operable mobile menu and photo lightbox (Esc, arrow keys).
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
- **Program:** student combat robotics club (second season as of 2026–27).
- **Meetings:** Thursdays and Fridays, Room 408 (source: team Instagram).
- **Instagram:** [@rv.robotics](https://www.instagram.com/rv.robotics/).
- **Google Classroom:** `gftqhxdh` (source: team Instagram bio).
- **Photos:** team workbench, first-meeting flyer, and club update flyer from Instagram.

The site references combat robotics in general terms. It does not claim a specific
competition league, team number, awards, or match record.

---

## Credits

- Team photography and flyers: [@rv.robotics](https://www.instagram.com/rv.robotics/).
- River Valley High School Falcons logo: River Valley High School / Yuba City Unified
  School District.
- Official team logo: River Valley Robotics (provided by the team).
- Typefaces: Barlow Condensed and Inter, SIL Open Font License 1.1, self-hosted.
- Icons and the robot concept drawing: original SVG work made for this site.

See `credits.html` for the public-facing version.
