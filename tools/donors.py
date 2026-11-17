"""Donor wall data for the sponsorship page.

Online gifts land in the team's Hack Club Bank account, and HCB publishes them
at a public, unauthenticated JSON endpoint. The wall is built twice from that
same feed:

  * ``tools/build.py`` renders a snapshot into ``sponsors.html`` so the names
    are in the HTML even before JavaScript runs;
  * ``js/donors.js`` refreshes the snapshot in the browser, so a new gift shows
    up on the next page load without rebuilding or redeploying the site.

Sponsor logos, display names, and links are hand-maintained in
``assets/data/donors.json``, keyed by the donor name shown on HCB.
"""
from __future__ import annotations

import html
import json
import ssl
import urllib.request
from datetime import datetime, timezone

from rvsite import ROOT

try:  # certifi ships with pip and keeps a current root bundle
    import certifi

    _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except ImportError:  # fall back to the platform store
    _SSL_CONTEXT = ssl.create_default_context()

API = "https://hcb.hackclub.com/api/v3/organizations/{slug}/donations?per_page=100&page={page}"
CACHE_PATH = ROOT / "tools" / ".cache" / "donors.json"
CONFIG_PATH = ROOT / "assets" / "data" / "donors.json"
MAX_PAGES = 3
SKIP_STATUS = {"failed", "refunded", "reversed", "cancelled", "canceled"}
ANON_KEY = "__anonymous__"


def _get_json(url, timeout=6):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "RV-Robotics-site/1.0 (+https://rvrobotics.ycusd.org/)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout, context=_SSL_CONTEXT) as response:
        return json.loads(response.read().decode("utf-8"))


def _read_cache():
    try:
        payload = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []
    donations = payload.get("donations") if isinstance(payload, dict) else None
    return donations if isinstance(donations, list) else []


def fetch(slug):
    """Return ``(donations, source)`` where source is live, cache, or none."""
    donations = []
    try:
        for page in range(1, MAX_PAGES + 1):
            batch = _get_json(API.format(slug=slug, page=page))
            if not isinstance(batch, list) or not batch:
                break
            donations.extend(batch)
            if len(batch) < 100:
                break
    except (OSError, ValueError):
        donations = []

    if donations:
        try:
            CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
            CACHE_PATH.write_text(
                json.dumps(
                    {
                        "fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        "donations": donations,
                    },
                    indent=1,
                ),
                encoding="utf-8",
            )
        except OSError:
            pass
        return donations, "live"

    cached = _read_cache()
    return cached, ("cache" if cached else "none")


def load_config():
    try:
        payload = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    sponsors = payload.get("sponsors") if isinstance(payload, dict) else None
    return sponsors if isinstance(sponsors, dict) else {}


def _settings_for(name, config):
    wanted = name.casefold()
    for key, value in config.items():
        if key.casefold() == wanted and isinstance(value, dict):
            return value
    return {}


def level_for(cents, levels):
    earned = [level for level in levels if cents >= level["min"] * 100]
    if not earned:
        return levels[0]
    return max(earned, key=lambda level: level["min"])


def _initials(name):
    cleaned = "".join(ch if ch.isalnum() or ch in " .&'-" else " " for ch in name).split()
    if not cleaned:
        return "?"
    if len(cleaned) == 1:
        return cleaned[0][:1].upper()
    return (cleaned[0][:1] + cleaned[-1][:1]).upper()


def aggregate(donations, config, levels):
    """Group gifts by donor and attach the level their total earns."""
    merged = {}
    for donation in donations:
        if not isinstance(donation, dict):
            continue
        if str(donation.get("status") or "").lower() in SKIP_STATUS:
            continue
        try:
            cents = int(donation.get("amount_cents") or 0)
        except (TypeError, ValueError):
            continue
        if cents <= 0:
            continue

        donor = donation.get("donor") or {}
        name = str(donor.get("name") or "").strip()
        anonymous = bool(donor.get("anonymous")) or not name
        key = ANON_KEY if anonymous else name.casefold()
        entry = merged.get(key)
        if entry is None:
            entry = merged[key] = {
                "name": "Anonymous" if anonymous else name,
                "anonymous": anonymous,
                "cents": 0,
                "gifts": 0,
            }
        entry["cents"] += cents
        entry["gifts"] += 1

    donors = []
    for entry in merged.values():
        settings = _settings_for(entry["name"], config)
        if settings.get("hide"):
            continue
        display = str(settings.get("display") or entry["name"]).strip() or entry["name"]
        level = level_for(entry["cents"], levels)
        forced = str(settings.get("tier") or "").strip().casefold()
        if forced:
            match = next(
                (item for item in levels if item["label"].casefold() == forced or item["slug"] == forced),
                None,
            )
            if match:
                level = match
        donors.append(
            {
                "name": display,
                "initials": _initials(display),
                "tier": level,
                "cents": entry["cents"],
                "gifts": entry["gifts"],
                "logo": str(settings.get("logo") or "").strip(),
                "url": str(settings.get("url") or "").strip(),
            }
        )

    donors.sort(key=lambda item: (-item["tier"]["min"], -item["cents"], item["name"].casefold()))
    return donors


def levels_attribute(levels):
    """JSON for the data attribute that keeps js/donors.js in sync."""
    ordered = sorted(levels, key=lambda item: -item["min"])
    return html.escape(json.dumps(ordered, separators=(",", ":")), quote=True)


def tier_note(tier):
    """The threshold shown next to a level heading on the wall."""
    note = str(tier.get("note") or "").strip()
    if note:
        return note
    return "any gift" if tier["min"] == 0 else f"${tier['min']:,} and up"


def _card(donor):
    if donor["logo"]:
        mark = (
            f'<img class="donor-logo" src="{html.escape(donor["logo"], quote=True)}" '
            'width="96" height="56" alt="" loading="lazy" decoding="async">'
        )
    else:
        mark = f'<span class="donor-mark" aria-hidden="true">{html.escape(donor["initials"])}</span>'

    name = html.escape(donor["name"])
    if donor["url"]:
        name_html = (
            f'<a class="donor-name" href="{html.escape(donor["url"], quote=True)}" '
            f'target="_blank" rel="noopener sponsored">{name}</a>'
        )
    else:
        name_html = f'<span class="donor-name">{name}</span>'

    return f"""        <li class="donor-card" data-tier="{donor['tier']['slug']}">
          {mark}
          <span class="donor-body">{name_html}</span>
        </li>"""


def render_grid(donors, empty_text):
    """Render one section per level, highest level first.

    Every card shows the donor's name next to their logo (or initials), so a
    name is never replaced by a picture.
    """
    if not donors:
        return f'<p class="donor-wall-empty" data-donor-empty>{empty_text}</p>'

    order = []
    grouped = {}
    for donor in donors:
        slug = donor["tier"]["slug"]
        if slug not in grouped:
            grouped[slug] = []
            order.append(slug)
        grouped[slug].append(donor)

    sections = []
    for slug in order:
        members = grouped[slug]
        tier = members[0]["tier"]
        count = len(members)
        cards = "\n".join(_card(donor) for donor in members)
        sections.append(
            f"""    <section class="donor-tier" data-tier="{slug}" aria-labelledby="donor-tier-{slug}">
      <div class="donor-tier-head">
        <h3 class="donor-tier-name" id="donor-tier-{slug}">{html.escape(tier["label"])}</h3>
        <span class="donor-tier-note">{html.escape(tier_note(tier))}</span>
        <span class="donor-tier-count">{count} donor{"" if count == 1 else "s"}</span>
      </div>
      <ul class="donor-grid">
{cards}
      </ul>
    </section>"""
        )

    return "\n".join(sections)
