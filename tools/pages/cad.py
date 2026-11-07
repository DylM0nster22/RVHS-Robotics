"""CAD lab page."""
import html
import json
from pathlib import Path

from rvsite import icon, page_hero, cta_band, ASSET_VERSION

ROOT = Path(__file__).resolve().parent.parent.parent
MANIFEST = ROOT / "assets" / "models" / "manifest.json"

TITLE = "3D CAD lab | River Valley Robotics"
DESCRIPTION = "Orbit the actual STEP CAD for the 3lb vertical spinner and the other public combat robots from DylM0nster22 on GitHub. Interactive 3D in the browser, no plugins."
ACTIVE = "cad"
FILENAME = "cad.html"

EXTRA_HEAD = """<script type="importmap">
  {
    "imports": {
      "three": "./assets/js/vendor/three.module.js",
      "three/addons/": "./assets/js/vendor/addons/"
    }
  }
  </script>"""

GROUP_ORDER = ["3 lb", "1 lb", "Plastic ant", "150 g", "Other robots"]


def load_models():
    if not MANIFEST.exists():
        raise SystemExit(
            "assets/models/manifest.json is missing. Run "
            "`node tools/make-models.mjs` first (see README)."
        )
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["models"]


MODELS = load_models()
for model in MODELS:
    model["glb"] = f'{model["glb"]}?v={ASSET_VERSION}'
    model["thumb"] = f'{model["thumb"]}?v={ASSET_VERSION}'
FEATURED = next((model for model in MODELS if model.get("featured")), MODELS[0])
BY_ID = {model["id"]: model for model in MODELS}
COUNT = len(MODELS)
COMBAT_COUNT = sum(1 for model in MODELS if model.get("group") == "combat")


def group_label(model):
    value = model.get("class", "").lower()
    if "3 lb" in value:
        return "3 lb"
    if "1 lb" in value:
        return "1 lb"
    if "plastic ant" in value:
        return "Plastic ant"
    if "150 g" in value:
        return "150 g"
    return "Other robots"


def dimensions(model):
    stats = model.get("stats") or {}
    bbox = stats.get("bbox")
    if not bbox:
        return "Dimensions loading"
    return f'{bbox["x"]:g} &times; {bbox["y"]:g} &times; {bbox["z"]:g} mm'


def triangle_count(model):
    stats = model.get("stats") or {}
    triangles = stats.get("triangles")
    if not triangles:
        return "Mesh data loading"
    return f"{triangles:,} triangles"


def megabytes(value):
    if not value:
        return ""
    return f"{value / 1024 / 1024:.1f} MB"


def specs_html(model):
    rows = []
    for label, value in model.get("specs", []):
        rows.append(f"<div><dt>{label}</dt><dd>{value}</dd></div>")
    return "\n".join(rows)


def stats_html(model):
    return " &middot; ".join([dimensions(model), triangle_count(model)])


def select_options():
    chunks = []
    for group in GROUP_ORDER:
        group_models = [model for model in MODELS if group_label(model) == group]
        if not group_models:
            continue
        options = "\n".join(
            f'<option value="{model["id"]}"{" selected" if model["id"] == FEATURED["id"] else ""}>'
            f'{html.escape(model["name"])} &mdash; {html.escape(model["type"])}</option>'
            for model in group_models
        )
        chunks.append(f'<optgroup label="{group}">\n{options}\n</optgroup>')
    return "\n".join(chunks)


def model_cards():
    cards = []
    for index, model in enumerate(MODELS, start=1):
        stats = model.get("stats") or {}
        featured = " cad-card--featured" if model.get("featured") else ""
        badge = '<span class="cad-card-badge">Featured</span>' if model.get("featured") else ""
        alt = f'3D render of the {model["name"]} CAD model'
        card_stats = dimensions(model)
        if stats.get("triangles"):
            card_stats += f' &middot; {stats["triangles"]:,} tris'
        cards.append(
            f"""<a class="cad-card{featured}" href="cad.html?model={model["id"]}" data-cad-model="{model["id"]}">
  <span class="cad-card-media">
    <img src="{model["thumb"]}" width="600" height="450" alt="{html.escape(alt)}" loading="lazy">
    <span class="cad-card-view">View in 3D {icon("cube")}</span>
    {badge}
  </span>
  <span class="cad-card-copy">
    <span class="cad-card-top">
      <span class="mono-label">{index:02d} &middot; {html.escape(model["class"])}</span>
      <span class="cad-card-type">{html.escape(model["type"])}</span>
    </span>
    <strong>{html.escape(model["name"])}</strong>
    <span class="cad-card-stats">{card_stats}</span>
  </span>
</a>"""
        )
    return "\n".join(cards)


MODELS_DATA = json.dumps(
    {"models": MODELS, "featured": FEATURED["id"]},
    ensure_ascii=False,
    separators=(",", ":"),
).replace("</", "<\\/")

BODY = f"""
{page_hero(
    "CAD lab",
    "Every robot,<br>in the round.",
    "The actual CAD, not a render. Orbit the 3lb vertical spinner, then open the other public combat robots from Dyl's GitHub. STEP files converted for the browser, with the originals one click away.",
    f"{COUNT} public models",
    f"{COMBAT_COUNT} combat robots, each with a full CAD assembly and a public GitHub repo. Drag, zoom, and take them apart with your eyes.",
    "CAD lab",
)}

<section class="section cad-stage" id="viewer" aria-labelledby="cad-viewer-heading">
  <div class="container">
    <div class="cad-shell">
      <div class="cad-visual">
        <div class="cad-viewport" id="cad-viewport" tabindex="0" role="application" aria-describedby="cad-hint" aria-keyshortcuts="ArrowLeft ArrowRight ArrowUp ArrowDown + - R A W G F" aria-label="Interactive 3D model viewer. Drag to orbit, scroll to zoom, right-drag to pan.">
          <canvas id="cad-canvas" aria-hidden="true"></canvas>

          <div class="cad-toolbar" role="toolbar" aria-label="3D view controls">
            <button class="cad-tool" type="button" data-cad-action="reset" aria-label="Reset view" title="Reset view (R)">
              {icon("reset")}<span>Reset</span>
            </button>
            <button class="cad-tool" type="button" data-cad-action="spin" aria-label="Toggle auto-rotate" aria-pressed="true" title="Auto-rotate (A)">
              {icon("rotate")}<span>Spin</span>
            </button>
            <button class="cad-tool" type="button" data-cad-action="wireframe" aria-label="Toggle wireframe" aria-pressed="false" title="Wireframe (W)">
              {icon("wireframe")}<span>Wire</span>
            </button>
            <button class="cad-tool" type="button" data-cad-action="grid" aria-label="Toggle floor grid" aria-pressed="true" title="Grid (G)">
              {icon("grid")}<span>Grid</span>
            </button>
            <button class="cad-tool" type="button" data-cad-action="fullscreen" aria-label="Enter fullscreen" aria-pressed="false" title="Fullscreen (F)">
              {icon("fullscreen")}<span>Full</span>
            </button>
          </div>

          <div class="cad-viewport-tag">
            <span class="cad-live-dot" aria-hidden="true"></span>
            <span id="cad-viewport-label">{html.escape(FEATURED["name"])}</span>
          </div>

          <div class="cad-loading" id="cad-loading" aria-hidden="true">
            <span class="mono-label" id="cad-loading-label">Loading model</span>
            <div class="cad-progress"><span id="cad-progress-bar"></span></div>
            <span class="cad-progress-pct" id="cad-progress-pct">0%</span>
          </div>

          <div class="cad-error" id="cad-error" role="alert" hidden>
            <span class="mono-label">Model unavailable</span>
            <p id="cad-error-text">The model could not be loaded. Check your connection, or open the original STEP file.</p>
            <a class="text-link" id="cad-error-link" href="{FEATURED["stepUrl"]}" target="_blank" rel="noopener">Open the STEP file {icon("external")}</a>
          </div>

          <div class="cad-fallback" id="cad-fallback">
            <span class="mono-label">3D CAD</span>
            <p>The interactive model needs JavaScript and WebGL. The original file is still available:</p>
            <a class="text-link" id="cad-fallback-link" href="{FEATURED["stepUrl"]}" target="_blank" rel="noopener">Open the STEP file {icon("external")}</a>
          </div>

          <p class="cad-hint" id="cad-hint">Drag to orbit <span aria-hidden="true">&middot;</span> Scroll to zoom <span aria-hidden="true">&middot;</span> Right-drag to pan</p>
          <span class="cad-corner" aria-hidden="true">RV / CAD</span>
        </div>
        <p class="cad-viewer-note">Each model is framed to fit the viewer, so relative scale between different robots is not exact. Print from the original STEP, not the on-screen mesh.</p>
      </div>

      <aside class="cad-panel" aria-label="Selected model">
        <p class="kicker" id="cad-panel-kicker">Featured build</p>
        <h2 id="cad-viewer-heading" data-cad-name>{html.escape(FEATURED["name"])}</h2>
        <p class="cad-model-meta">
          <span data-cad-class>{html.escape(FEATURED["class"])}</span>
          <span class="cad-sep" aria-hidden="true">/</span>
          <span data-cad-type>{html.escape(FEATURED["type"])}</span>
        </p>
        <p class="cad-model-desc" data-cad-desc>{FEATURED["description"]}</p>

        <dl class="cad-specs" data-cad-specs>
          {specs_html(FEATURED)}
        </dl>

        <p class="cad-model-stats" data-cad-stats>{stats_html(FEATURED)}</p>

        <div class="cad-links">
          <a class="text-link" data-cad-repo href="{FEATURED["repoUrl"]}" target="_blank" rel="noopener">Source on GitHub {icon("external")}</a>
          <a class="text-link" data-cad-step href="{FEATURED["stepUrl"]}" target="_blank" rel="noopener">Download STEP {icon("download")}</a>
        </div>

        <div class="cad-picker">
          <label for="cad-model-select">Choose a model</label>
          <select id="cad-model-select" class="cad-select">
            {select_options()}
          </select>
          <div class="cad-pager">
            <button type="button" class="cad-pager-btn" data-cad-prev aria-label="Previous model">{icon("prev")}<span>Prev</span></button>
            <span class="cad-position" id="cad-position">01 / {COUNT:02d}</span>
            <button type="button" class="cad-pager-btn" data-cad-next aria-label="Next model"><span>Next</span>{icon("next")}</button>
          </div>
        </div>

        <p class="cad-source-note">CAD by <a href="https://github.com/DylM0nster22" target="_blank" rel="noopener">DylM0nster22</a> and collaborators. Check each repo for its license before reusing a model.</p>      </aside>
    </div>

    <p class="visually-hidden" id="cad-status" role="status" aria-live="polite"></p>
    <noscript>
      <div class="cad-noscript">
        <p>JavaScript is off, so the interactive 3D viewer is not active. The original files are on GitHub:</p>
        <ul class="cad-noscript-list">
          {"".join(f'<li><a href="{model["repoUrl"]}" target="_blank" rel="noopener">{html.escape(model["name"])}</a> <span>{html.escape(model["type"])}</span></li>' for model in MODELS)}
        </ul>
      </div>
    </noscript>
  </div>
</section>

<section class="section section--paper" id="models" aria-labelledby="cad-library">
  <div class="container">
    <div class="heading-row cad-library-head">
      <div>
        <p class="kicker">The library</p>
        <h2 id="cad-library">All {COUNT} models.</h2>
      </div>
    </div>
    <div class="cad-grid" id="cad-grid">
      {model_cards()}
    </div>
    <p class="cad-library-note">Every card opens the same viewer with that model selected. The STEP link inside the viewer always points at the original file on GitHub.</p>
  </div>
</section>

<section class="section section--white" aria-labelledby="cad-how">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="kicker">How it works</p>
        <h2 id="cad-how">Real CAD,<br>no plugin.</h2>
      </div>
      <div class="head-copy">
        <p class="lead">The site is still plain HTML, CSS, and JavaScript. The heavy lifting happens ahead of time, and the browser only downloads the model you pick.</p>
      </div>
    </div>
    <div class="grid-3">
      <article class="card reveal">
        <div class="card-icon">{icon("link")}</div>
        <h3>Straight from GitHub</h3>
        <p>Every model links back to its public repository and the original STEP file. Nothing is re-modeled for the site.</p>
      </article>
      <article class="card reveal" style="--d:70ms">
        <div class="card-icon">{icon("cube")}</div>
        <h3>Tessellated once</h3>
        <p>STEP files are converted to compressed GLB assets with OpenCascade and meshoptimizer. The first model loads immediately; the rest wait until you pick one.</p>
      </article>
      <article class="card reveal" style="--d:140ms">
        <div class="card-icon">{icon("zoom")}</div>
        <h3>Built to explore</h3>
        <p>Orbit, pan, zoom, wireframe, floor grid, and fullscreen. Keyboard controls work when the viewer has focus.</p>
      </article>
    </div>

    <div class="faq cad-faq">
      <details>
        <summary>Viewer controls</summary>
        <p><strong>Mouse:</strong> drag to orbit, scroll to zoom, right-drag to pan. <strong>Touch:</strong> one finger orbits, two fingers zoom and pan. <strong>Keyboard:</strong> arrow keys orbit, <kbd>+</kbd> and <kbd>&minus;</kbd> zoom, <kbd>R</kbd> resets, <kbd>A</kbd> toggles spin, <kbd>W</kbd> wireframe, <kbd>G</kbd> grid, and <kbd>F</kbd> fullscreen. <strong>Buttons:</strong> the toolbar does the same thing and works without a mouse wheel.</p>
      </details>
      <details>
        <summary>How accurate is the 3D model?</summary>
        <p>The geometry comes from each repo's STEP file. Curved surfaces are tessellated into triangles for display, so small curves are slightly simplified, and the mesh is not a substitute for the original CAD. Dimensions listed in the viewer are the model's overall extents in millimeters. Each model is framed to fit the viewer, so scale between different robots is not directly comparable. Print and machine from the STEP file.</p>
      </details>
      <details>
        <summary>Why are some builds missing?</summary>
        <p>This page focuses on the public combat robots. Workshop projects and other CAD files are left out, and a repo without a STEP file or one that is not public yet does not appear. The library uses the main assembly from each repo, not every individual part STL or print plate. If a build gets a new file, add it to <code>tools/models.json</code> and rebuild the assets.</p>
      </details>
      <details>
        <summary>Credits and reuse</summary>
        <p>CAD by DylM0nster22 and the listed collaborators. Models are linked from their public repositories; check each repository for license terms before reusing geometry, images, or design files. The 3D viewer uses Three.js (MIT) and the meshoptimizer decoder (MIT), both self-hosted.</p>
      </details>
    </div>
  </div>
</section>

{cta_band(
    "Want to build one?",
    "The CAD is public. The shop is in Room 408. Come to a meeting, ask questions, and make the next version better.",
    "join.html",
    "How to join",
    "contact.html",
    "Ask a question",
)}
"""

MODELS_JSON = MODELS_DATA
BODY += f"""
<script type="application/json" id="cad-models-data">{MODELS_DATA}</script>
<script type="module" src="js/cad-viewer.js?v={ASSET_VERSION}"></script>
"""
