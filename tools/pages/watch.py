"""Watch page — match video archive."""
from rvsite import icon, page_hero, cta_band, YOUTUBE, YOUTUBE_HANDLE

TITLE = "Watch | River Valley Robotics"
DESCRIPTION = "Match footage from River Valley Robotics: fights from Impact Robotics League #1 2026, plus newer videos from the Bad Plants channel."
ACTIVE = "watch"
FILENAME = "watch.html"

EVENT = "Impact Robotics League #1 2026"
FEATURED = "edgehog-commander"

# Each video is encoded and given a poster by tools/make-videos.py.
# Keep the source file names in sync with the files supplied by the team.
# The 30-second ...-announcement-only.mp4 clip is an event announcement, not a
# match, so it is intentionally not listed here.
LOCAL_VIDEOS = [
    {"slug": "lobotomini-meteor-hammer", "source": "01-lobotomini-vs-meteor-hammer.mp4", "a": "Lobotomini", "b": "Meteor Hammer", "duration": "0:45", "note": ""},
    {"slug": "k7-mechanical-romance", "source": "02-k7-vs-mechanical-romance.mp4", "a": "K7", "b": "Mechanical Romance", "duration": "2:30", "note": ""},
    {"slug": "k7-tremor", "source": "03-k7-vs-tremor.mp4", "a": "K7", "b": "Tremor", "duration": "3:05", "note": ""},
    {"slug": "edgehog-zica", "source": "04-edgehog-vs-zica.mp4", "a": "Edgehog", "b": "Zica", "duration": "2:40", "note": ""},
    {"slug": "k7-lobotomini", "source": "06-k7-vs-lobotomini.mp4", "a": "K7", "b": "Lobotomini", "duration": "1:55", "note": ""},
    {"slug": "edgehog-lil-munch", "source": "07-edgehog-vs-lil-munch.mp4", "a": "Edgehog", "b": "Lil Munch", "duration": "1:35", "note": ""},
    {"slug": "k7-meteor-hammer-final", "source": "08-k7-vs-meteor-hammer-final.mp4", "a": "K7", "b": "Meteor Hammer", "duration": "1:10", "note": "Final"},
    {"slug": "edgehog-commander", "source": "09-edgehog-vs-commander.mp4", "a": "Edgehog", "b": "Commander", "duration": "1:55", "note": ""},
    {"slug": "lobotomini-theseus", "source": "10-lobotomini-vs-theseus.mp4", "a": "Lobotomini", "b": "Theseus", "duration": "3:55", "note": ""},
    {"slug": "k7-apocalypse-now", "source": "11-k7-vs-apocalypse-now.mp4", "a": "K7", "b": "Apocalypse Now", "duration": "2:40", "note": ""},
    {"slug": "k7-chudster", "source": "12-k7-vs-chudster.mp4", "a": "K7", "b": "Chudster", "duration": "2:00", "note": ""},
]

# Newer uploads from the channel. Playback is a privacy-enhanced YouTube embed
# created only after a visitor chooses a video.
YOUTUBE_VIDEOS = [
    {"id": "eOoZPrhjjyE", "slug": "edgehog-not-important", "a": "Edgehog", "b": "Not Important", "event": "Bot'Geddon 2026", "duration": "2:04"},
    {"id": "9EcZF5XpHmY", "slug": "edgehog-mildly-dangerous", "a": "Edgehog", "b": "Mildly Dangerous", "event": "IRL4 Championships 2026", "duration": "2:08"},
    {"id": "I88_kmLdC6c", "slug": "edgehog-envy", "a": "Edgehog", "b": "Envy", "event": "IRL4 Championships 2026", "duration": "1:05"},
    {"id": "XyJlROgx554", "slug": "edgehog-bone-crusher", "a": "Edgehog", "b": "Bone Crusher", "event": "IRL4 Championships 2026", "duration": "1:55"},
]


def seconds(duration):
    minutes, secs = duration.split(":")
    return int(minutes) * 60 + int(secs)


local_seconds = sum(seconds(video["duration"]) for video in LOCAL_VIDEOS)
youtube_seconds = sum(seconds(video["duration"]) for video in YOUTUBE_VIDEOS)
total_minutes = round((local_seconds + youtube_seconds) / 60)
local_minutes = round(local_seconds / 60)

featured = next(video for video in LOCAL_VIDEOS if video["slug"] == FEATURED)
featured_title = f"{featured['a']} vs. {featured['b']}"

local_cards = ""
for video in LOCAL_VIDEOS:
    title = f"{video['a']} vs. {video['b']}"
    meta = f"{video['note']} &middot; IRL #1 &middot; 2026" if video["note"] else "IRL #1 &middot; 2026"
    modal_meta = EVENT + (" · " + video["note"] if video["note"] else "")
    local_cards += f"""
    <a class="video-card" href="assets/video/{video['slug']}.mp4"
       data-media data-video-src="assets/video/{video['slug']}.mp4" data-poster="assets/img/video/{video['slug']}.webp"
       data-title="{title}" data-meta="{modal_meta}"
       data-desc="Overhead match footage from Impact Robotics League #1 2026. Full match, {video['duration']}."
       aria-label="Play {title}, {video['duration']}">
      <span class="video-thumb">
        <img src="assets/img/video/{video['slug']}.webp" width="1280" height="720" alt="" loading="lazy" decoding="async">
        <span class="video-play" aria-hidden="true">{icon("play")}</span>
        <span class="video-duration">{video['duration']}</span>
      </span>
      <span class="video-card-body">
        <span class="video-card-title">{video['a']} <em>vs.</em> {video['b']}</span>
        <span class="video-card-meta">{meta}</span>
      </span>
    </a>
    """

youtube_cards = ""
for video in YOUTUBE_VIDEOS:
    title = f"{video['a']} vs. {video['b']}"
    youtube_cards += f"""
    <a class="video-card video-card--yt" href="https://www.youtube.com/watch?v={video['id']}" target="_blank" rel="noopener"
       data-media data-youtube="{video['id']}" data-poster="assets/img/video/yt-{video['slug']}.webp"
       data-title="{title}" data-meta="{video['event']}"
       data-desc="Match video from {video['event']}, published on the Bad Plants channel. Plays through YouTube."
       aria-label="Play {title} on YouTube, {video['duration']}">
      <span class="video-thumb">
        <img src="assets/img/video/yt-{video['slug']}.webp" width="1280" height="720" alt="" loading="lazy" decoding="async">
        <span class="video-play" aria-hidden="true">{icon("play")}</span>
        <span class="video-source">{icon("youtube")} YouTube</span>
        <span class="video-duration">{video['duration']}</span>
      </span>
      <span class="video-card-body">
        <span class="video-card-title">{video['a']} <em>vs.</em> {video['b']}</span>
        <span class="video-card-meta">{video['event']}</span>
      </span>
    </a>
    """

BODY = f"""
{page_hero(
    "Watch",
    "Fights from<br>the floor.",
    f"Full matches from {EVENT}, plus newer fights from the {YOUTUBE_HANDLE} channel. Pick a card to play. Nothing starts until you choose it.",
    "2026 season",
    f"{len(LOCAL_VIDEOS)} arena matches<br>{len(YOUTUBE_VIDEOS)} YouTube picks<br>{total_minutes} minutes of footage",
    "Watch",
)}

<section class="section section--dark section--grid" aria-labelledby="featured">
  <div class="container">
    <div class="video-feature">
      <a class="video-hero reveal" href="assets/video/{featured['slug']}.mp4"
         data-media data-video-src="assets/video/{featured['slug']}.mp4" data-poster="assets/img/video/{featured['slug']}.webp"
         data-title="{featured_title}" data-meta="Impact Robotics League #1 2026"
         data-desc="Overhead match footage from Impact Robotics League #1 2026. Full match, {featured['duration']}."
         aria-label="Play featured match: {featured_title}, {featured['duration']}">
        <img src="assets/img/video/{featured['slug']}.webp" width="1280" height="720" alt="" decoding="async">
        <span class="video-hero-shade" aria-hidden="true"></span>
        <span class="video-play video-play--lg" aria-hidden="true">{icon("play")}</span>
        <span class="video-hero-caption" aria-hidden="true">
          <span class="mono-label">Featured match</span>
          <strong>{featured_title}</strong>
        </span>
        <span class="video-duration">{featured['duration']}</span>
      </a>
      <div class="video-feature-copy reveal" style="--d:100ms">
        <p class="kicker">Featured match</p>
        <h2 id="featured">{featured['a']} vs.<br>{featured['b']}.</h2>
        <p class="lead" style="margin-top:1.4rem">Overhead footage from the high school field at Impact Robotics League #1 2026. This is the match as recorded, start to finish.</p>
        <dl class="spec-grid">
          <div class="spec"><dt>Event</dt><dd>IRL #1</dd></div>
          <div class="spec"><dt>Season</dt><dd>2026</dd></div>
          <div class="spec"><dt>Length</dt><dd>{featured['duration']}</dd></div>
          <div class="spec"><dt>Format</dt><dd>Full match</dd></div>
        </dl>
        <a class="text-link" href="#irl-1" style="margin-top:1.5rem">Browse all matches {icon("arrow")}</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--paper" id="irl-1" aria-labelledby="irl-heading">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">Impact Robotics League #1</p>
        <h2 id="irl-heading">The 2026<br>matches.</h2>
      </div>
      <p class="mono-label">{len(LOCAL_VIDEOS)} videos &middot; {local_minutes} min</p>
    </div>
    <div class="video-grid">
      {local_cards}
    </div>
    <p class="photo-credit">Overhead footage from Impact Robotics League #1 2026. Event overlays and sponsor marks belong to the event and its sponsors. Match videos have arena audio; if you need a description or another accommodation, <a href="contact.html">contact the team</a>.</p>
  </div>
</section>

<section class="section section--white" aria-labelledby="channel">
  <div class="container">
    <div class="heading-row">
      <div>
        <p class="kicker">From the channel</p>
        <h2 id="channel">Newer<br>fights.</h2>
      </div>
      <a class="text-link" href="{YOUTUBE}/videos" target="_blank" rel="noopener">All videos on {YOUTUBE_HANDLE} {icon("external")}</a>
    </div>
    <p class="lead" style="max-width:62ch;margin-bottom:clamp(1.5rem,3vw,2.25rem)">Recent uploads from the Bad Plants channel, including Bot'Geddon 2026 and the IRL4 Championships. These load from YouTube's privacy-enhanced player only after you press play.</p>
    <div class="video-grid video-grid--four">
      {youtube_cards}
    </div>
    <p class="photo-credit">Videos and thumbnails from <a href="{YOUTUBE}" target="_blank" rel="noopener">{YOUTUBE_HANDLE}</a> on YouTube.</p>
  </div>
</section>

<dialog class="video-modal" id="video-modal" aria-labelledby="video-modal-title" aria-describedby="video-modal-desc">
  <div class="video-modal-stage">
    <video class="video-modal-video" id="video-modal-video" controls playsinline preload="none"></video>
    <div class="video-modal-embed" id="video-modal-embed" hidden></div>
    <button class="video-modal-close" type="button" data-video-close aria-label="Close video player">{icon("close")}</button>
  </div>
  <div class="video-modal-bar">
    <div class="video-modal-copy" aria-live="polite">
      <p class="mono-label" id="video-modal-meta"></p>
      <h2 class="video-modal-title" id="video-modal-title"></h2>
      <p class="video-modal-desc" id="video-modal-desc"></p>
    </div>
    <div class="video-modal-actions">
      <a class="btn btn--ghost btn--sm" id="video-modal-link" href="#" target="_blank" rel="noopener" hidden>Watch on YouTube {icon("external")}</a>
      <div class="video-modal-nav">
        <button class="video-modal-btn" type="button" data-video-prev aria-label="Previous video">{icon("prev")}</button>
        <button class="video-modal-btn" type="button" data-video-next aria-label="Next video">{icon("next")}</button>
      </div>
    </div>
  </div>
</dialog>

{cta_band(
    "Want to build one?",
    "Come to a meeting in Room 408. Grades 9&ndash;12, no experience needed, and you can help with the next robot.",
    "join.html",
    "How to join",
    "contact.html",
    "Ask a question",
)}
"""
