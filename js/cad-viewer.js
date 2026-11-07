/* River Valley Robotics - CAD viewer
   Loads the models listed in assets/models/manifest.json (embedded by the
   page build) and draws one at a time with Three.js. */
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { MeshoptDecoder } from "three/addons/libs/meshopt_decoder.module.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

(function () {
  "use strict";

  const dataElement = document.getElementById("cad-models-data");
  if (!dataElement) return;

  let data;
  try {
    data = JSON.parse(dataElement.textContent || "{}");
  } catch (error) {
    return;
  }

  const models = Array.isArray(data.models) ? data.models : [];
  if (!models.length) return;
  const byId = new Map(models.map((model) => [model.id, model]));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const params = new URLSearchParams(window.location.search);
  const isThumbnail = params.get("thumb") === "1";
  const featured = byId.get(data.featured) || models[0];
  const requested = byId.get(params.get("model"));
  let currentId = (requested || featured).id;

  if (isThumbnail) {
    document.documentElement.classList.add("cad-thumb-mode");
    document.body.classList.add("cad-thumb-mode");
  }

  const viewport = document.getElementById("cad-viewport");
  const canvas = document.getElementById("cad-canvas");
  if (!viewport || !canvas) return;

  const nameElement = document.querySelector("[data-cad-name]");
  const classElement = document.querySelector("[data-cad-class]");
  const typeElement = document.querySelector("[data-cad-type]");
  const descriptionElement = document.querySelector("[data-cad-desc]");
  const specsElement = document.querySelector("[data-cad-specs]");
  const statsElement = document.querySelector("[data-cad-stats]");
  const repoLink = document.querySelector("[data-cad-repo]");
  const stepLink = document.querySelector("[data-cad-step]");
  const select = document.getElementById("cad-model-select");
  const positionElement = document.getElementById("cad-position");
  const statusElement = document.getElementById("cad-status");
  const panelKicker = document.getElementById("cad-panel-kicker");
  const viewportLabel = document.getElementById("cad-viewport-label");
  const loadingElement = document.getElementById("cad-loading");
  const loadingLabel = document.getElementById("cad-loading-label");
  const progressBar = document.getElementById("cad-progress-bar");
  const progressText = document.getElementById("cad-progress-pct");
  const errorElement = document.getElementById("cad-error");
  const errorText = document.getElementById("cad-error-text");
  const errorLink = document.getElementById("cad-error-link");
  const fallbackElement = document.getElementById("cad-fallback");
  const fallbackLink = document.getElementById("cad-fallback-link");
  const spinButton = viewport.querySelector('[data-cad-action="spin"]');
  const wireButton = viewport.querySelector('[data-cad-action="wireframe"]');
  const gridButton = viewport.querySelector('[data-cad-action="grid"]');
  const fullButton = viewport.querySelector('[data-cad-action="fullscreen"]');
  const hintElement = document.getElementById("cad-hint");

  if (hintElement && window.matchMedia("(pointer: coarse)").matches) {
    hintElement.textContent = "Drag to orbit \u00b7 Pinch to zoom \u00b7 Two-finger pan";
  }

  const numberFormat = new Intl.NumberFormat("en-US");

  function dimensions(model) {
    const bbox = model.stats && model.stats.bbox;
    if (!bbox) return "Dimensions loading";
    return `${bbox.x}\u00a0\u00d7\u00a0${bbox.y}\u00a0\u00d7\u00a0${bbox.z}\u00a0mm`;
  }

  function statsText(model) {
    return [dimensions(model), `${numberFormat.format((model.stats && model.stats.triangles) || 0)} triangles`].join(
      " \u00b7 "
    );
  }

  function setInfo(model) {
    if (!model) return;
    if (nameElement) nameElement.textContent = model.name;
    if (classElement) classElement.textContent = model.class;
    if (typeElement) typeElement.textContent = model.type;
    if (descriptionElement) descriptionElement.textContent = model.description;
    if (statsElement) statsElement.textContent = statsText(model);
    if (panelKicker) panelKicker.textContent = model.featured ? "Featured build" : "Now viewing";
    if (viewportLabel) viewportLabel.textContent = model.name;

    if (specsElement) {
      const rows = (model.specs || []).map(([label, value]) => {
        const row = document.createElement("div");
        const term = document.createElement("dt");
        const detail = document.createElement("dd");
        term.textContent = label;
        detail.textContent = value;
        row.append(term, detail);
        return row;
      });
      specsElement.replaceChildren(...rows);
    }

    if (repoLink) repoLink.href = model.repoUrl;
    if (stepLink) stepLink.href = model.stepUrl;
    if (fallbackLink) fallbackLink.href = model.stepUrl;
    if (errorLink) errorLink.href = model.stepUrl;
    if (select) select.value = model.id;

    const index = models.findIndex((item) => item.id === model.id);
    if (positionElement) {
      positionElement.textContent = `${String(index + 1).padStart(2, "0")} / ${String(models.length).padStart(2, "0")}`;
    }

    document.querySelectorAll("[data-cad-model]").forEach((card) => {
      const isCurrent = card.getAttribute("data-cad-model") === model.id;
      card.classList.toggle("is-current", isCurrent);
      if (isCurrent) card.setAttribute("aria-current", "true");
      else card.removeAttribute("aria-current");
    });

    if (!isThumbnail) {
      document.title = `${model.name} | 3D CAD lab | River Valley Robotics`;
    }
  }

  function announce(message) {
    if (statusElement) statusElement.textContent = message;
  }

  function setLoading(active, percent) {
    viewport.classList.toggle("is-loading", Boolean(active));
    viewport.setAttribute("aria-busy", String(Boolean(active)));
    if (loadingElement) loadingElement.setAttribute("aria-hidden", String(!active));
    if (loadingLabel) loadingLabel.textContent = "Loading model";
    if (progressBar) progressBar.style.width = `${Math.max(0, Math.min(100, percent || 0))}%`;
    if (progressText) progressText.textContent = `${Math.round(percent || 0)}%`;
  }

  function setProgress(percent) {
    if (progressBar) progressBar.style.width = `${Math.max(0, Math.min(100, percent))}%`;
    if (progressText) progressText.textContent = `${Math.round(percent)}%`;
  }

  function hideError() {
    if (errorElement) errorElement.hidden = true;
  }

  function showError(model, error) {
    if (loadingElement) setLoading(false, 0);
    viewport.classList.remove("is-ready");
    if (errorElement) errorElement.hidden = false;
    if (errorText) {
      errorText.textContent =
        "The model could not be loaded. Check your connection, or open the original STEP file.";
    }
    if (errorLink && model) errorLink.href = model.stepUrl;
    if (model) announce(`${model.name} could not be loaded.`);
    if (error) console.warn("[cad-viewer]", error);
    if (isThumbnail) window.__cadThumbnailError = true;
  }

  function showFallback() {
    if (fallbackElement) fallbackElement.hidden = false;
    viewport.classList.add("is-fallback");
    viewport.classList.remove("is-loading", "is-ready");
    if (canvas) canvas.hidden = true;
    if (select) select.disabled = true;
    document.querySelectorAll("[data-cad-action]").forEach((button) => {
      button.disabled = true;
    });
    if (isThumbnail) window.__cadThumbnailError = true;
  }

  setInfo(byId.get(currentId) || featured);

  /* ---------- Renderer ---------- */
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
      powerPreference: "high-performance",
    });
  } catch (error) {
    showFallback();
    return;
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.setClearColor(0x000000, 0);
  if (fallbackElement) fallbackElement.hidden = true;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(38, 1, 0.01, 200);
  camera.position.set(2.6, 1.8, 3.4);

  const controls = new OrbitControls(camera, canvas);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.rotateSpeed = 0.85;
  controls.zoomSpeed = 1.1;
  controls.panSpeed = 0.8;
  controls.screenSpacePanning = true;
  controls.minDistance = 0.5;
  controls.maxDistance = 12;
  controls.maxPolarAngle = Math.PI / 2 - 0.012;
  controls.target.set(0, 1, 0);
  controls.autoRotate = !reduceMotion.matches && !isThumbnail;
  controls.autoRotateSpeed = 0.9;

  scene.add(new THREE.HemisphereLight(0xe9f8ee, 0x0a120d, 1.1));

  const keyLight = new THREE.DirectionalLight(0xffffff, 2.8);
  keyLight.position.set(4.5, 7, 5.5);
  scene.add(keyLight);

  const fillLight = new THREE.DirectionalLight(0xb8e3c4, 1.55);
  fillLight.position.set(-6, 3.5, 2);
  scene.add(fillLight);

  const rimLight = new THREE.DirectionalLight(0xe8fff0, 2.5);
  rimLight.position.set(-2, 5, -6.5);
  scene.add(rimLight);

  try {
    const environment = new RoomEnvironment();
    const pmrem = new THREE.PMREMGenerator(renderer);
    scene.environment = pmrem.fromScene(environment, 0.04).texture;
    scene.environmentIntensity = 0.45;
    pmrem.dispose();
    environment.dispose?.();
  } catch (error) {
    /* Environment reflections are a nice-to-have. */
  }

  const grid = new THREE.GridHelper(4, 16, 0x79a889, 0x36533f);
  grid.position.y = 0;
  (Array.isArray(grid.material) ? grid.material : [grid.material]).forEach((material) => {
    material.transparent = true;
    material.opacity = 0.42;
    material.depthWrite = false;
  });
  grid.visible = !isThumbnail;
  scene.add(grid);

  function makeShadowTexture() {
    const size = 512;
    const shadowCanvas = document.createElement("canvas");
    shadowCanvas.width = size;
    shadowCanvas.height = size;
    const context = shadowCanvas.getContext("2d");
    if (!context) return null;
    const gradient = context.createRadialGradient(size / 2, size / 2, size * 0.04, size / 2, size / 2, size * 0.5);
    gradient.addColorStop(0, "rgba(0, 0, 0, 0.62)");
    gradient.addColorStop(0.4, "rgba(0, 0, 0, 0.28)");
    gradient.addColorStop(1, "rgba(0, 0, 0, 0)");
    context.fillStyle = gradient;
    context.fillRect(0, 0, size, size);
    const texture = new THREE.CanvasTexture(shadowCanvas);
    texture.colorSpace = THREE.NoColorSpace;
    return texture;
  }

  const shadowTexture = makeShadowTexture();
  if (shadowTexture) {
    const shadow = new THREE.Mesh(
      new THREE.PlaneGeometry(3.4, 3.4),
      new THREE.MeshBasicMaterial({
        map: shadowTexture,
        transparent: true,
        depthWrite: false,
        opacity: 0.7,
      })
    );
    shadow.rotation.x = -Math.PI / 2;
    shadow.position.y = 0.004;
    shadow.renderOrder = 1;
    scene.add(shadow);
  }

  const gltfLoader = new GLTFLoader();
  gltfLoader.setMeshoptDecoder(MeshoptDecoder);
  const meshoptReady = MeshoptDecoder.ready || Promise.resolve();

  const cache = new Map();
  const fitDirection = new THREE.Vector3(1.22, 0.6, 1.52).normalize();
  let currentRoot = null;
  let currentModel = null;
  let loadingId = null;
  let loadToken = 0;
  let abortController = null;
  let wireframe = false;
  let visible = true;
  let needsRender = true;
  let lastWidth = 0;
  let lastHeight = 0;

  function prepareRoot(root) {
    root.rotation.x = -Math.PI / 2;
    root.updateMatrixWorld(true);

    const box = new THREE.Box3().setFromObject(root);
    const size = box.getSize(new THREE.Vector3());
    const maxDimension = Math.max(size.x, size.y, size.z) || 1;
    root.scale.setScalar(2 / maxDimension);
    root.updateMatrixWorld(true);

    const scaledBox = new THREE.Box3().setFromObject(root);
    const center = scaledBox.getCenter(new THREE.Vector3());
    root.position.x -= center.x;
    root.position.z -= center.z;
    root.position.y -= scaledBox.min.y;
    root.updateMatrixWorld(true);

    root.traverse((object) => {
      if (!object.isMesh) return;
      object.frustumCulled = true;
      const materials = Array.isArray(object.material) ? object.material : [object.material];
      materials.forEach((material) => {
        if (!material) return;
        if ("envMapIntensity" in material) material.envMapIntensity = 0.75;
        if (material.map) material.map.anisotropy = Math.min(4, renderer.capabilities.getMaxAnisotropy());
        material.wireframe = wireframe;
        material.needsUpdate = true;
      });
    });
    return root;
  }

  function tightFitDistance(root, center, cameraDir, right, up, horizontalTan, verticalTan) {
    let distance = 0.8;
    const vertex = new THREE.Vector3();
    const relative = new THREE.Vector3();
    root.updateMatrixWorld(true);
    root.traverse((object) => {
      const position = object.isMesh && object.geometry && object.geometry.attributes.position;
      if (!position) return;
      const matrix = object.matrixWorld;
      for (let index = 0; index < position.count; index += 1) {
        vertex.fromBufferAttribute(position, index).applyMatrix4(matrix);
        relative.copy(vertex).sub(center);
        const depth = relative.dot(cameraDir);
        const needed = Math.max(
          Math.abs(relative.dot(right)) / horizontalTan,
          Math.abs(relative.dot(up)) / verticalTan
        ) + depth;
        if (needed > distance) distance = needed;
      }
    });
    return distance;
  }

  function frameModel(root) {
    if (!root) return;
    root.updateMatrixWorld(true);
    const box = new THREE.Box3().setFromObject(root);
    const size = box.getSize(new THREE.Vector3());
    const center = box.getCenter(new THREE.Vector3());
    const target = center.clone();

    const cameraDir = fitDirection.clone().normalize();
    const right = new THREE.Vector3().crossVectors(new THREE.Vector3(0, 1, 0), cameraDir).normalize();
    const up = new THREE.Vector3().crossVectors(cameraDir, right).normalize();
    const verticalTan = Math.tan(THREE.MathUtils.degToRad(camera.fov) / 2);
    const horizontalTan = verticalTan * (camera.aspect || 1.4);
    const distance = Math.max(
      tightFitDistance(root, center, cameraDir, right, up, horizontalTan, verticalTan) * 1.04,
      0.9
    );

    camera.position.copy(target).addScaledVector(cameraDir, distance);
    camera.near = Math.max(0.01, distance / 150);
    camera.far = Math.max(50, distance * 120);
    camera.updateProjectionMatrix();

    controls.target.copy(target);
    controls.minDistance = Math.max(0.35, distance * 0.33);
    controls.maxDistance = Math.max(5, distance * 4.2);
    controls.update();
    if (currentModel && Array.isArray(currentModel.view) && currentModel.view.length === 2) {
      setView(currentModel.view[0], currentModel.view[1]);
    }
    needsRender = true;
  }

  function setView(azimuthDegrees, elevationDegrees) {
    const azimuth = THREE.MathUtils.degToRad(azimuthDegrees);
    const elevation = THREE.MathUtils.degToRad(Math.max(-60, Math.min(80, elevationDegrees)));
    const target = controls.target;
    const distance = camera.position.distanceTo(target) || 4;
    camera.position.set(
      target.x + distance * Math.cos(elevation) * Math.sin(azimuth),
      target.y + distance * Math.sin(elevation),
      target.z + distance * Math.cos(elevation) * Math.cos(azimuth)
    );
    camera.updateProjectionMatrix();
    controls.update();
    needsRender = true;
  }

  function applyWireframe(root, enabled) {
    if (!root) return;
    root.traverse((object) => {
      if (!object.isMesh) return;
      const materials = Array.isArray(object.material) ? object.material : [object.material];
      materials.forEach((material) => {
        if (!material) return;
        material.wireframe = enabled;
        material.needsUpdate = true;
      });
    });
    needsRender = true;
  }

  function disposeRoot(root) {
    if (!root) return;
    const geometries = new Set();
    const materials = new Set();
    const textures = new Set();
    root.traverse((object) => {
      if (object.geometry) geometries.add(object.geometry);
      const list = Array.isArray(object.material) ? object.material : object.material ? [object.material] : [];
      list.forEach((material) => {
        materials.add(material);
        Object.values(material).forEach((value) => {
          if (value && value.isTexture) textures.add(value);
        });
      });
    });
    geometries.forEach((geometry) => geometry.dispose());
    materials.forEach((material) => material.dispose());
    textures.forEach((texture) => texture.dispose());
  }

  function trimCache(keepId) {
    while (cache.size > 3) {
      let evict = null;
      for (const key of cache.keys()) {
        if (key !== keepId && key !== currentId) {
          evict = key;
          break;
        }
      }
      if (!evict) break;
      disposeRoot(cache.get(evict).template);
      cache.delete(evict);
    }
  }

  async function fetchModel(model, token, controller, onProgress) {
    const response = await fetch(model.glb, { signal: controller.signal, credentials: "same-origin" });
    if (!response.ok) throw new Error(`HTTP ${response.status} for ${model.glb}`);
    const declared = Number(response.headers.get("content-length")) || (model.stats && model.stats.glbBytes) || 0;
    if (!response.body || !declared) {
      const buffer = await response.arrayBuffer();
      onProgress(1);
      return buffer;
    }
    const reader = response.body.getReader();
    const chunks = [];
    let received = 0;
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      if (token !== loadToken) throw new DOMException("Superseded", "AbortError");
      chunks.push(value);
      received += value.length;
      onProgress(Math.min(0.94, received / declared));
    }
    const merged = new Uint8Array(received);
    let offset = 0;
    chunks.forEach((chunk) => {
      merged.set(chunk, offset);
      offset += chunk.length;
    });
    return merged.buffer;
  }

  function updateUrl(model) {
    if (isThumbnail) return;
    try {
      const url = new URL(window.location.href);
      url.searchParams.set("model", model.id);
      window.history.replaceState(null, "", url);
    } catch (error) {
      /* The viewer still works if history is restricted. */
    }
  }

  async function loadModel(id, options = {}) {
    const model = byId.get(id);
    if (!model || !renderer) return;
    if (id === currentId && currentRoot) {
      setInfo(model);
      return;
    }
    if (loadingId === id) return;

    if (abortController) abortController.abort();
    abortController = new AbortController();
    const controller = abortController;
    const token = ++loadToken;
    const previous = currentId;
    loadingId = id;

    setInfo(model);
    hideError();
    setLoading(true, 0);
    announce(`Loading ${model.name}.`);
    if (loadingLabel) loadingLabel.textContent = "Loading model";

    try {
      let root;
      const cached = cache.get(id);
      if (cached) {
        root = cached.template.clone(true);
        setProgress(100);
      } else {
        const buffer = await fetchModel(model, token, controller, (progress) => {
          if (token === loadToken) setProgress(progress * 92);
        });
        if (token !== loadToken) return;
        if (loadingLabel) loadingLabel.textContent = "Preparing model";
        setProgress(96);
        await meshoptReady;
        if (token !== loadToken) return;
        const gltf = await gltfLoader.parseAsync(buffer, "");
        if (token !== loadToken) {
          disposeRoot(gltf.scene);
          return;
        }
        root = prepareRoot(gltf.scene);
        cache.set(id, { template: root, used: Date.now() });
        trimCache(id);
        setProgress(100);
      }

      if (token !== loadToken) return;
      if (currentRoot) scene.remove(currentRoot);
      currentRoot = root;
      currentModel = model;
      currentRoot.visible = true;
      applyWireframe(currentRoot, wireframe);
      scene.add(currentRoot);
      frameModel(currentRoot);
      viewport.classList.add("is-ready");
      viewport.classList.remove("is-fallback");
      setLoading(false, 100);
      loadingId = null;
      currentId = id;
      updateUrl(model);
      announce(`Showing ${model.name}. ${model.class}, ${model.type}.`);
      renderer.render(scene, camera);
      needsRender = false;

      if (isThumbnail) {
        setSpin(false, false);
        grid.visible = false;
        const azimuth = params.get("az");
        const elevation = params.get("el");
        if (azimuth !== null) setView(Number(azimuth), Number(elevation === null ? 17 : elevation));
        requestAnimationFrame(() => {
          frameModel(currentRoot);
          if (azimuth !== null) setView(Number(azimuth), Number(elevation === null ? 17 : elevation));
          renderer.render(scene, camera);
          window.__cadThumbnailReady = true;
        });
      }
    } catch (error) {
      if (error && error.name === "AbortError") return;
      if (token !== loadToken) return;
      loadingId = null;
      setLoading(false, 0);
      showError(model, error);
      if (previous && byId.has(previous) && currentRoot) setInfo(byId.get(previous));
    }
  }

  /* ---------- Controls ---------- */
  let autoRotate = controls.autoRotate;

  function setSpin(enabled, announceChange = true) {
    autoRotate = Boolean(enabled) && !reduceMotion.matches;
    controls.autoRotate = autoRotate;
    if (spinButton) {
      spinButton.setAttribute("aria-pressed", String(autoRotate));
      spinButton.setAttribute("aria-label", autoRotate ? "Stop auto-rotate" : "Auto-rotate model");
    }
    if (announceChange && !isThumbnail) {
      announce(autoRotate ? "Auto-rotate on." : "Auto-rotate off.");
    }
    needsRender = true;
  }

  function setWireframe(enabled) {
    wireframe = Boolean(enabled);
    applyWireframe(currentRoot, wireframe);
    if (wireButton) {
      wireButton.setAttribute("aria-pressed", String(wireframe));
      wireButton.setAttribute("aria-label", wireframe ? "Show solid model" : "Show wireframe");
    }
    if (!isThumbnail) announce(wireframe ? "Wireframe on." : "Solid view.");
  }

  function setGrid(enabled) {
    grid.visible = Boolean(enabled);
    if (gridButton) {
      gridButton.setAttribute("aria-pressed", String(grid.visible));
      gridButton.setAttribute("aria-label", grid.visible ? "Hide floor grid" : "Show floor grid");
    }
    needsRender = true;
    if (!isThumbnail) announce(grid.visible ? "Floor grid on." : "Floor grid off.");
  }

  setSpin(!reduceMotion.matches && !isThumbnail, false);
  if (gridButton) gridButton.setAttribute("aria-pressed", "true");

  viewport.querySelectorAll("[data-cad-action]").forEach((button) => {
    button.addEventListener("click", () => {
      const action = button.getAttribute("data-cad-action");
      if (action === "reset" && currentRoot) {
        frameModel(currentRoot);
        if (!isThumbnail) announce("View reset.");
      } else if (action === "spin") {
        setSpin(!autoRotate);
      } else if (action === "wireframe") {
        setWireframe(!wireframe);
      } else if (action === "grid") {
        setGrid(!grid.visible);
      } else if (action === "fullscreen") {
        toggleFullscreen();
      }
    });
  });

  async function toggleFullscreen() {
    if (!document.fullscreenEnabled) {
      if (!isThumbnail) announce("Fullscreen is not available in this browser.");
      return;
    }
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else await viewport.requestFullscreen();
    } catch (error) {
      if (!isThumbnail) announce("Fullscreen could not be opened.");
    }
  }

  function updateFullscreenButton() {
    const active = document.fullscreenElement === viewport;
    if (!fullButton) return;
    fullButton.setAttribute("aria-pressed", String(active));
    fullButton.setAttribute("aria-label", active ? "Exit fullscreen" : "Enter fullscreen");
    const label = fullButton.querySelector("span");
    if (label) label.textContent = active ? "Exit" : "Full";
    requestAnimationFrame(resize);
  }

  document.addEventListener("fullscreenchange", updateFullscreenButton);

  /* ---------- Camera keyboard ---------- */
  viewport.addEventListener("keydown", (event) => {
    const key = event.key;
    let handled = true;
    if (key === "ArrowLeft") controls.rotateLeft(0.14);
    else if (key === "ArrowRight") controls.rotateLeft(-0.14);
    else if (key === "ArrowUp") controls.rotateUp(0.12);
    else if (key === "ArrowDown") controls.rotateUp(-0.12);
    else if (key === "+" || key === "=") controls.dollyIn(0.9);
    else if (key === "-" || key === "_") controls.dollyOut(1.1);
    else if (key === "r" || key === "R" || key === "0") {
      if (currentRoot) frameModel(currentRoot);
      announce("View reset.");
    } else if (key === "a" || key === "A") setSpin(!autoRotate);
    else if (key === "w" || key === "W") setWireframe(!wireframe);
    else if (key === "g" || key === "G") setGrid(!grid.visible);
    else if (key === "f" || key === "F") toggleFullscreen();
    else handled = false;
    if (handled) {
      event.preventDefault();
      needsRender = true;
    }
  });

  canvas.addEventListener("pointerdown", () => {
    viewport.focus({ preventScroll: true });
    if (autoRotate) setSpin(false);
    viewport.classList.add("is-grabbing");
  });
  document.addEventListener("pointerup", () => viewport.classList.remove("is-grabbing"));

  viewport.addEventListener("dblclick", () => {
    if (currentRoot) frameModel(currentRoot);
  });

  /* ---------- Model picker ---------- */
  if (select) {
    select.addEventListener("change", () => {
      const model = byId.get(select.value);
      if (model) loadModel(model.id);
    });
  }

  document.querySelectorAll("[data-cad-prev], [data-cad-next]").forEach((button) => {
    button.addEventListener("click", () => {
      const direction = button.hasAttribute("data-cad-next") ? 1 : -1;
      const index = models.findIndex((model) => model.id === currentId);
      const next = models[(index + direction + models.length) % models.length];
      if (next) loadModel(next.id);
    });
  });

  document.querySelectorAll("[data-cad-model]").forEach((card) => {
    card.addEventListener("click", (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
      event.preventDefault();
      const id = card.getAttribute("data-cad-model");
      loadModel(id);
      const viewer = document.getElementById("viewer");
      if (viewer) {
        viewer.scrollIntoView({
          behavior: reduceMotion.matches ? "auto" : "smooth",
          block: "start",
        });
      }
    });
  });

  /* ---------- Size and render loop ---------- */
  function resize() {
    const width = Math.max(1, Math.round(viewport.clientWidth));
    const height = Math.max(1, Math.round(viewport.clientHeight));
    if (width === lastWidth && height === lastHeight) return;
    lastWidth = width;
    lastHeight = height;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
    needsRender = true;
    renderer.render(scene, camera);
  }

  if ("ResizeObserver" in window) {
    new ResizeObserver(resize).observe(viewport);
  }
  window.addEventListener("resize", resize, { passive: true });
  resize();

  if ("IntersectionObserver" in window && !isThumbnail) {
    new IntersectionObserver(
      (entries) => {
        visible = entries.some((entry) => entry.isIntersecting);
        if (visible) needsRender = true;
      },
      { rootMargin: "120px" }
    ).observe(viewport);
  }

  function animate() {
    requestAnimationFrame(animate);
    if (!visible) return;
    const changed = controls.update();
    if (changed || needsRender) {
      renderer.render(scene, camera);
      needsRender = false;
    }
  }

  reduceMotion.addEventListener("change", (event) => {
    if (event.matches && autoRotate) setSpin(false, false);
  });

  if (!isThumbnail) animate();
  else setSpin(false, false);

  /* Kick off the initial model. */
  const initial = byId.get(currentId) || featured;
  loadModel(initial.id);
})();
