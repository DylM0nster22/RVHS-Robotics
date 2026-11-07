#!/usr/bin/env node
/**
 * Render transparent WebP thumbnails for the CAD library.
 *
 * Setup (one time):
 *   cd tools
 *   npm install
 *
 * Run from the project root:
 *   node tools/make-model-thumbs.mjs
 *   node tools/make-model-thumbs.mjs --only 3lb-vertical-spinner
 *
 * Uses the installed Chrome/Edge through puppeteer-core. Set CHROME_PATH if
 * neither browser is in the default location. The page's own `?thumb=1` mode
 * strips the site chrome, hides the grid, and exposes a 600x450 render target.
 */
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import puppeteer from "puppeteer-core";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "..");
const MANIFEST = path.join(ROOT, "assets", "models", "manifest.json");
const OUT = path.join(ROOT, "assets", "models", "thumbs");
const args = process.argv.slice(2);
const only = args.includes("--only") ? args[args.indexOf("--only") + 1] : null;
const azimuth = args.includes("--az") ? args[args.indexOf("--az") + 1] : null;
const elevation = args.includes("--el") ? args[args.indexOf("--el") + 1] : null;

const CHROME_CANDIDATES = [
  process.env.CHROME_PATH,
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
].filter(Boolean);

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".glb": "model/gltf-binary",
  ".webp": "image/webp",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".woff2": "font/woff2",
  ".ico": "image/x-icon",
};

function findChrome() {
  for (const candidate of CHROME_CANDIDATES) {
    if (candidate && fs.existsSync(candidate)) return candidate;
  }
  throw new Error("Chrome or Edge not found. Set CHROME_PATH.");
}

function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((request, response) => {
      const url = new URL(request.url || "/", "http://127.0.0.1");
      const decoded = decodeURIComponent(url.pathname);
      const relative = decoded === "/" ? "index.html" : decoded.replace(/^\/+/, "");
      const target = path.resolve(ROOT, relative);
      if (!target.startsWith(ROOT) || !fs.existsSync(target) || fs.statSync(target).isDirectory()) {
        response.writeHead(404, { "content-type": "text/plain" });
        response.end("not found");
        return;
      }
      const ext = path.extname(target).toLowerCase();
      const body = fs.readFileSync(target);
      response.writeHead(200, {
        "content-type": MIME[ext] || "application/octet-stream",
        "content-length": body.length,
        "cache-control": "no-store",
      });
      response.end(body);
    });
    server.listen(0, "127.0.0.1", () => resolve(server));
  });
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(MANIFEST, "utf8"));
  const models = manifest.models.filter((model) => !only || model.id === only);
  if (!models.length) throw new Error(`unknown model: ${only}`);
  fs.mkdirSync(OUT, { recursive: true });

  const server = await startServer();
  const port = server.address().port;
  const browser = await puppeteer.launch({
    executablePath: findChrome(),
    headless: true,
    args: [
      "--hide-scrollbars",
      "--enable-unsafe-swiftshader",
      "--disable-dev-shm-usage",
      "--force-color-profile=srgb",
    ],
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 900, height: 700, deviceScaleFactor: 2 });

    for (const model of models) {
      const url = `http://127.0.0.1:${port}/cad.html?model=${encodeURIComponent(model.id)}&thumb=1${
        azimuth !== null ? `&az=${encodeURIComponent(azimuth)}` : ""
      }${elevation !== null ? `&el=${encodeURIComponent(elevation)}` : ""}`;
      process.stdout.write(`[${model.id}] rendering... `);
      await page.goto(url, { waitUntil: "domcontentloaded", timeout: 60000 });
      await page.waitForFunction(
        () => window.__cadThumbnailReady === true || window.__cadThumbnailError === true,
        { timeout: 90000 }
      );
      const failed = await page.evaluate(() => window.__cadThumbnailError === true);
      if (failed) throw new Error(`viewer failed to render ${model.id}`);
      await page.evaluate(() => document.fonts.ready);
      await new Promise((resolve) => setTimeout(resolve, 250));

      const target = await page.$("#cad-viewport");
      if (!target) throw new Error("thumbnail target missing");
      const file = path.join(OUT, `${model.id}.webp`);
      await target.screenshot({
        path: file,
        type: "webp",
        quality: 88,
        omitBackground: true,
      });
      console.log(`${path.relative(ROOT, file)} (${(fs.statSync(file).size / 1024).toFixed(0)} KB)`);
    }
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch((error) => {
  console.error(`\n${error.message}`);
  process.exit(1);
});
