#!/usr/bin/env node
/**
 * Convert the public STEP files in tools/models.json into optimized GLB files
 * for the CAD viewer.
 *
 * Setup (one time):
 *   cd tools
 *   npm install
 *
 * Run from the project root:
 *   node tools/make-models.mjs
 *   node tools/make-models.mjs --only 3lb-vertical-spinner --force
 *   node tools/make-models.mjs --jobs 2
 *
 * The script downloads each STEP file into tools/.cache/models, builds a raw
 * GLB with OpenCascade (occt-import-js), compresses it with meshoptimizer
 * (gltfpack), and writes assets/models/<id>.glb plus a runtime manifest at
 * assets/models/manifest.json. The source manifest is never modified.
 */
import { spawn } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import occtimport from "occt-import-js";
import { Document, NodeIO } from "@gltf-transform/core";

const require = createRequire(import.meta.url);
const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, "..");
const SOURCE_MANIFEST = path.join(HERE, "models.json");
const CACHE = path.join(HERE, ".cache", "models");
const OUT = path.join(ROOT, "assets", "models");
const RAW = path.join(CACHE, "raw");
const STATS = path.join(OUT, ".stats");
const RUNTIME_MANIFEST = path.join(OUT, "manifest.json");

function parseArgs(argv) {
  const args = { force: false, jobs: 1, only: null, one: null };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--force") args.force = true;
    else if (arg === "--jobs") args.jobs = Number(argv[++i]) || 1;
    else if (arg === "--only") args.only = argv[++i];
    else if (arg === "--one") args.one = argv[++i];
    else if (arg === "--help" || arg === "-h") {
      console.log("Usage: node tools/make-models.mjs [--only ID] [--jobs N] [--force]");
      process.exit(0);
    }
  }
  return args;
}

const args = parseArgs(process.argv.slice(2));

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8"));
}

function loadModels() {
  return readJson(SOURCE_MANIFEST).models;
}

function rawUrl(model) {
  const encoded = model.stepPath.split("/").map(encodeURIComponent).join("/");
  return `https://raw.githubusercontent.com/${model.repo}/${model.branch}/${encoded}`;
}

function repoUrl(model) {
  return `https://github.com/${model.repo}`;
}

function stepUrl(model) {
  return `${repoUrl(model)}/blob/${model.branch}/${model.stepPath.split("/").map(encodeURIComponent).join("/")}`;
}

async function download(model) {
  const target = path.join(CACHE, `${model.id}.step`);
  const stamp = path.join(CACHE, `${model.id}.source`);
  const source = rawUrl(model);
  if (!args.force && fs.existsSync(target) && fs.existsSync(stamp) && fs.readFileSync(stamp, "utf8") === source) {
    return target;
  }
  fs.mkdirSync(CACHE, { recursive: true });
  console.log(`  downloading ${source}`);
  const response = await fetch(source);
  if (!response.ok) throw new Error(`download failed: ${response.status} ${response.statusText} (${source})`);
  const chunks = [];
  let received = 0;
  for await (const chunk of response.body) {
    chunks.push(chunk);
    received += chunk.length;
    if (received > 2 * 1024 * 1024 && process.stdout.isTTY) {
      process.stdout.write(`\r  downloading ${(received / 1024 / 1024).toFixed(1)} MB`);
    }
  }
  if (process.stdout.isTTY) process.stdout.write("\n");
  const buffer = Buffer.concat(chunks);
  if (buffer.length < 1024) throw new Error(`download looks wrong (${buffer.length} bytes): ${source}`);
  fs.writeFileSync(target, buffer);
  fs.writeFileSync(stamp, source);
  return target;
}

function accessor(doc, buffer, array, type, componentType) {
  return doc
    .createAccessor(`${type}-${doc.getRoot().listAccessors().length}`)
    .setType(type)
    .setArray(array)
    .setBuffer(buffer);
}

function createGlb(meshes, name) {
  const doc = new Document();
  const buffer = doc.createBuffer("buffer");
  const scene = doc.createScene(name);
  const materials = new Map();
  let parts = 0;

  const materialFor = (color) => {
    const key = color ? color.map((value) => value.toFixed(4)).join(",") : "default";
    if (materials.has(key)) return materials.get(key);
    const material = doc
      .createMaterial(key === "default" ? "CAD default" : key)
      .setBaseColorFactor(color ? [...color, 1] : [0.72, 0.75, 0.72, 1])
      .setMetallicFactor(0.08)
      .setRoughnessFactor(0.55)
      .setDoubleSided(true);
    materials.set(key, material);
    return material;
  };

  meshes.forEach((mesh, index) => {
    const position = mesh.attributes && mesh.attributes.position && mesh.attributes.position.array;
    if (!position || position.length < 9) return;
    let indices = mesh.index && mesh.index.array;
    if (!indices || indices.length < 3) {
      indices = new Uint32Array(position.length / 3);
      for (let i = 0; i < indices.length; i += 1) indices[i] = i;
    }
    const normal = mesh.attributes && mesh.attributes.normal && mesh.attributes.normal.array;

    const primitive = doc.createPrimitive();
    primitive.setAttribute("POSITION", accessor(doc, buffer, new Float32Array(position), "VEC3"));
    if (normal && normal.length === position.length) {
      primitive.setAttribute("NORMAL", accessor(doc, buffer, new Float32Array(normal), "VEC3"));
    }
    primitive.setIndices(accessor(doc, buffer, new Uint32Array(indices), "SCALAR"));
    primitive.setMaterial(materialFor(mesh.color || null));

    const partName = mesh.name && mesh.name.trim() ? mesh.name.trim() : `Part ${index + 1}`;
    const part = doc.createMesh(partName).addPrimitive(primitive);
    const node = doc.createNode(partName).setMesh(part);
    scene.addChild(node);
    parts += 1;
  });

  if (!parts) throw new Error("no renderable meshes in STEP file");
  doc.getRoot().getAsset().generator = "RV Robotics CAD pipeline (occt-import-js + gltfpack)";
  return { doc, parts };
}

function bboxFromMeshes(meshes) {
  const min = [Infinity, Infinity, Infinity];
  const max = [-Infinity, -Infinity, -Infinity];
  let triangles = 0;
  let vertices = 0;
  for (const mesh of meshes) {
    const position = mesh.attributes && mesh.attributes.position && mesh.attributes.position.array;
    if (!position) continue;
    vertices += Math.floor(position.length / 3);
    if (mesh.index && mesh.index.array) triangles += Math.floor(mesh.index.array.length / 3);
    for (let i = 0; i < position.length; i += 3) {
      for (let axis = 0; axis < 3; axis += 1) {
        const value = position[i + axis];
        if (value < min[axis]) min[axis] = value;
        if (value > max[axis]) max[axis] = value;
      }
    }
  }
  return {
    triangles,
    vertices,
    bbox: {
      x: Math.round((max[0] - min[0]) * 10) / 10,
      y: Math.round((max[1] - min[1]) * 10) / 10,
      z: Math.round((max[2] - min[2]) * 10) / 10
    }
  };
}

function run(command, argv) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, argv, { stdio: "inherit" });
    child.on("error", reject);
    child.on("exit", (code) => {
      if (code === 0) resolve();
      else reject(new Error(`${command} exited with ${code}`));
    });
  });
}

async function convertOne(model) {
  const occt = await occtimport();
  console.log(`[${model.id}] reading STEP`);
  const stepFile = await download(model);
  const stepBuffer = fs.readFileSync(stepFile);
  const started = Date.now();
  const result = occt.ReadStepFile(new Uint8Array(stepBuffer), {
    linearUnit: "millimeter",
    linearDeflectionType: "bounding_box_ratio",
    linearDeflection: model.deflection || 0.003,
    angularDeflection: 0.5
  });
  if (!result || !result.success || !result.meshes || !result.meshes.length) {
    throw new Error(`OpenCascade could not read ${model.stepPath}`);
  }
  console.log(
    `[${model.id}] tessellated ${result.meshes.length} solids in ${((Date.now() - started) / 1000).toFixed(1)}s`
  );

  const { doc, parts } = createGlb(result.meshes, model.name);
  const rawFile = path.join(RAW, `${model.id}.glb`);
  fs.mkdirSync(RAW, { recursive: true });
  const rawGlb = await new NodeIO().writeBinary(doc);
  fs.writeFileSync(rawFile, rawGlb);
  console.log(`[${model.id}] raw GLB ${(rawGlb.byteLength / 1024 / 1024).toFixed(1)} MB`);

  const glbFile = path.join(OUT, `${model.id}.glb`);
  fs.mkdirSync(OUT, { recursive: true });
  const gltfpack = require.resolve("gltfpack/cli.js");
  await run(process.execPath, [gltfpack, "-i", rawFile, "-o", glbFile, "-cc", "-vp", "14"]);
  fs.rmSync(rawFile, { force: true });

  const stats = {
    ...bboxFromMeshes(result.meshes),
    parts,
    stepBytes: stepBuffer.length,
    glbBytes: fs.statSync(glbFile).size,
    generated: new Date().toISOString()
  };
  fs.mkdirSync(STATS, { recursive: true });
  fs.writeFileSync(path.join(STATS, `${model.id}.json`), JSON.stringify(stats, null, 2));
  console.log(
    `[${model.id}] wrote ${path.relative(ROOT, glbFile)} (${(stats.glbBytes / 1024 / 1024).toFixed(2)} MB, ${stats.triangles.toLocaleString()} tris)`
  );
}

async function buildRuntimeManifest(models) {
  const merged = models.map((model) => {
    const statsFile = path.join(STATS, `${model.id}.json`);
    const stats = fs.existsSync(statsFile) ? readJson(statsFile) : null;
    return {
      ...model,
      repoUrl: repoUrl(model),
      stepUrl: stepUrl(model),
      glb: `assets/models/${model.id}.glb`,
      thumb: `assets/models/thumbs/${model.id}.webp`,
      stats
    };
  });
  const manifest = {
    generated: new Date().toISOString(),
    source: readJson(SOURCE_MANIFEST).source,
    models: merged
  };
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(RUNTIME_MANIFEST, JSON.stringify(manifest, null, 2));
  console.log(`wrote ${path.relative(ROOT, RUNTIME_MANIFEST)}`);
}

async function main() {
  const models = loadModels();
  if (args.one) {
    const model = models.find((item) => item.id === args.one);
    if (!model) throw new Error(`unknown model id: ${args.one}`);
    await convertOne(model);
    return;
  }

  const selected = args.only ? models.filter((model) => model.id === args.only) : models;
  if (!selected.length) throw new Error(`unknown model id: ${args.only}`);
  const queue = [];
  for (const model of selected) {
    const glb = path.join(OUT, `${model.id}.glb`);
    if (!args.force && fs.existsSync(glb)) {
      console.log(`[${model.id}] GLB exists, keeping (use --force to rebuild)`);
      continue;
    }
    queue.push(model);
  }

  const jobs = Math.max(1, Math.min(args.jobs, 4));
  let cursor = 0;
  async function worker() {
    while (cursor < queue.length) {
      const model = queue[cursor++];
      const child = spawn(
        process.execPath,
        [fileURLToPath(import.meta.url), "--one", model.id, ...(args.force ? ["--force"] : [])],
        { stdio: "inherit" }
      );
      await new Promise((resolve, reject) => {
        child.on("error", reject);
        child.on("exit", (code) => (code === 0 ? resolve() : reject(new Error(`${model.id} failed (${code})`))));
      });
    }
  }
  await Promise.all(Array.from({ length: jobs }, () => worker()));
  await buildRuntimeManifest(models);
}

main().catch((error) => {
  console.error(`\n${error.message}`);
  process.exit(1);
});
