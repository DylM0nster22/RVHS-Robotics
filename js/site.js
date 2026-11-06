/* River Valley Robotics — site behaviour */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Sticky header ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var setHeaderState = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 16);
    };
    setHeaderState();
    window.addEventListener("scroll", setHeaderState, { passive: true });
  }

  /* ---------- Mobile navigation ---------- */
  var navToggle = document.querySelector(".nav-toggle");
  var mobileNav = document.getElementById("mobile-nav");

  if (navToggle && mobileNav) {
    var pageMain = document.querySelector("main");
    var pageFooter = document.querySelector(".site-footer");

    var closeNav = function (returnFocus) {
      mobileNav.classList.remove("is-open");
      mobileNav.setAttribute("aria-hidden", "true");
      mobileNav.inert = true;
      if (pageMain) pageMain.inert = false;
      if (pageFooter) pageFooter.inert = false;
      navToggle.setAttribute("aria-expanded", "false");
      navToggle.setAttribute("aria-label", "Open menu");
      document.body.classList.remove("no-scroll");
      if (returnFocus) navToggle.focus();
    };

    var openNav = function () {
      mobileNav.inert = false;
      mobileNav.classList.add("is-open");
      mobileNav.setAttribute("aria-hidden", "false");
      if (pageMain) pageMain.inert = true;
      if (pageFooter) pageFooter.inert = true;
      navToggle.setAttribute("aria-expanded", "true");
      navToggle.setAttribute("aria-label", "Close menu");
      document.body.classList.add("no-scroll");
      var firstLink = mobileNav.querySelector("a");
      if (firstLink) firstLink.focus();
    };

    mobileNav.inert = true;
    mobileNav.setAttribute("aria-hidden", "true");

    navToggle.addEventListener("click", function () {
      var isOpen = navToggle.getAttribute("aria-expanded") === "true";
      if (isOpen) closeNav(true);
      else openNav();
    });

    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        closeNav(false);
      });
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && navToggle.getAttribute("aria-expanded") === "true") {
        closeNav(true);
      }
    });

    window.matchMedia("(min-width: 1081px)").addEventListener("change", function (event) {
      if (event.matches) closeNav(false);
    });
  }

  /* ---------- Current navigation item ---------- */
  var path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav a, .mobile-nav a").forEach(function (link) {
    var href = link.getAttribute("href");
    if (href === path) link.setAttribute("aria-current", "page");
  });

  /* ---------- Reveal on scroll ---------- */
  var revealItems = document.querySelectorAll(".reveal");
  if (revealItems.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealItems.forEach(function (item) {
        item.classList.add("is-visible");
      });
    } else {
      var revealObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-visible");
              revealObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
      );
      revealItems.forEach(function (item) {
        revealObserver.observe(item);
      });
    }
  }

  /* ---------- Lightbox ---------- */
  var lightbox = document.getElementById("lightbox");
  var galleryItems = Array.prototype.slice.call(document.querySelectorAll(".gallery-item"));
  var lightboxImg = document.getElementById("lightbox-img");
  var lightboxCaption = document.getElementById("lightbox-caption");
  var lightboxCounter = document.getElementById("lightbox-counter");
  var lightboxIndex = 0;
  var lastFocused = null;

  if (lightbox && galleryItems.length && lightboxImg) {
    var renderLightbox = function () {
      var item = galleryItems[lightboxIndex];
      var full = item.getAttribute("data-full");
      var caption = item.getAttribute("data-caption") || "";
      lightboxImg.src = full;
      lightboxImg.alt = caption;
      if (lightboxCaption) lightboxCaption.textContent = caption;
      if (lightboxCounter) {
        lightboxCounter.textContent =
          String(lightboxIndex + 1).padStart(2, "0") + " / " + String(galleryItems.length).padStart(2, "0");
      }
    };

    var openLightbox = function (index) {
      lightboxIndex = index;
      lastFocused = document.activeElement;
      renderLightbox();
      if (typeof lightbox.showModal === "function") lightbox.showModal();
      else lightbox.setAttribute("open", "");
      var closeButton = lightbox.querySelector("[data-lightbox-close]");
      if (closeButton) closeButton.focus();
    };

    var closeLightbox = function () {
      if (typeof lightbox.close === "function") lightbox.close();
      else lightbox.removeAttribute("open");
      if (lastFocused) lastFocused.focus();
    };

    var moveLightbox = function (direction) {
      lightboxIndex = (lightboxIndex + direction + galleryItems.length) % galleryItems.length;
      renderLightbox();
    };

    galleryItems.forEach(function (item, index) {
      item.addEventListener("click", function () {
        openLightbox(index);
      });
    });

    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox) closeLightbox();
    });

    lightbox.querySelectorAll("[data-lightbox-close]").forEach(function (button) {
      button.addEventListener("click", closeLightbox);
    });
    lightbox.querySelectorAll("[data-lightbox-prev]").forEach(function (button) {
      button.addEventListener("click", function () {
        moveLightbox(-1);
      });
    });
    lightbox.querySelectorAll("[data-lightbox-next]").forEach(function (button) {
      button.addEventListener("click", function () {
        moveLightbox(1);
      });
    });

    lightbox.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        moveLightbox(-1);
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        moveLightbox(1);
      }
    });
  }

  /* ---------- Video player ---------- */
  var videoModal = document.getElementById("video-modal");
  var videoCards = Array.prototype.slice.call(document.querySelectorAll("[data-media]"));
  var videoEl = document.getElementById("video-modal-video");
  var videoEmbed = document.getElementById("video-modal-embed");
  var videoTitle = document.getElementById("video-modal-title");
  var videoMeta = document.getElementById("video-modal-meta");
  var videoDesc = document.getElementById("video-modal-desc");
  var videoLink = document.getElementById("video-modal-link");
  var videoIndex = 0;
  var videoLastFocused = null;

  if (videoModal && videoCards.length && videoEl && videoEmbed && videoTitle) {
    var stopVideo = function () {
      videoEl.pause();
      videoEl.removeAttribute("src");
      videoEl.removeAttribute("poster");
      videoEl.load();
      videoEl.hidden = false;
      videoEmbed.innerHTML = "";
      videoEmbed.hidden = true;
      if (videoLink) {
        videoLink.hidden = true;
        videoLink.removeAttribute("href");
      }
    };

    var renderVideo = function (index, firstOpen) {
      videoIndex = index;
      var card = videoCards[index];
      var title = card.getAttribute("data-title") || "Match video";
      var meta = card.getAttribute("data-meta") || "";
      var desc = card.getAttribute("data-desc") || "";
      var youtube = card.getAttribute("data-youtube");

      stopVideo();
      videoTitle.textContent = title;
      videoMeta.textContent = meta;
      videoDesc.textContent = desc;

      if (youtube) {
        videoEl.hidden = true;
        videoEmbed.hidden = false;
        videoEmbed.innerHTML =
          '<iframe src="https://www.youtube-nocookie.com/embed/' +
          encodeURIComponent(youtube) +
          '?autoplay=1&rel=0&playsinline=1" title="' +
          title.replace(/"/g, "&quot;") +
          ' on YouTube" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe>';
        if (videoLink) {
          videoLink.href = "https://www.youtube.com/watch?v=" + encodeURIComponent(youtube);
          videoLink.hidden = false;
        }
      } else {
        videoEl.poster = card.getAttribute("data-poster") || "";
        videoEl.src = card.getAttribute("data-video-src") || "";
        videoEl.load();
      }

      if (firstOpen) {
        videoLastFocused = document.activeElement;
        if (typeof videoModal.showModal === "function") videoModal.showModal();
        else videoModal.setAttribute("open", "");
        document.body.classList.add("no-scroll");
        var closeButton = videoModal.querySelector("[data-video-close]");
        if (closeButton) closeButton.focus();
      }

      if (!youtube) {
        var playPromise = videoEl.play();
        if (playPromise && playPromise.catch) playPromise.catch(function () {});
      }
    };

    var closeVideo = function () {
      if (typeof videoModal.close === "function") {
        videoModal.close();
      } else {
        videoModal.removeAttribute("open");
        stopVideo();
        document.body.classList.remove("no-scroll");
        if (videoLastFocused) videoLastFocused.focus();
      }
    };

    videoCards.forEach(function (card, index) {
      card.addEventListener("click", function (event) {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
        event.preventDefault();
        renderVideo(index, true);
      });
    });

    videoModal.addEventListener("click", function (event) {
      if (event.target === videoModal) closeVideo();
    });

    videoModal.addEventListener("close", function () {
      stopVideo();
      document.body.classList.remove("no-scroll");
      if (videoLastFocused) videoLastFocused.focus();
    });

    videoModal.querySelectorAll("[data-video-close]").forEach(function (button) {
      button.addEventListener("click", closeVideo);
    });
    videoModal.querySelectorAll("[data-video-prev]").forEach(function (button) {
      button.addEventListener("click", function () {
        renderVideo((videoIndex - 1 + videoCards.length) % videoCards.length, false);
      });
    });
    videoModal.querySelectorAll("[data-video-next]").forEach(function (button) {
      button.addEventListener("click", function () {
        renderVideo((videoIndex + 1) % videoCards.length, false);
      });
    });
  }

  /* ---------- Mailto forms ---------- */
  document.querySelectorAll("form[data-mailto]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var address = form.getAttribute("data-mailto");
      var subject = form.getAttribute("data-subject") || "River Valley Robotics inquiry";
      var lines = [];

      form.querySelectorAll("input, select, textarea").forEach(function (field) {
        if (!field.name || field.type === "submit") return;
        var value = field.value.trim();
        if (!value) return;
        var label =
          field.getAttribute("data-label") ||
          (field.labels && field.labels[0] ? field.labels[0].textContent.trim() : field.name);
        lines.push(label + ": " + value);
      });

      var body = lines.join("\n");
      var mailto = "mailto:" + address + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      window.location.href = mailto;

      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.hidden = false;
        status.innerHTML =
          'Your email app should open with the message ready to send. If it does not, email us at <a href="mailto:' +
          address +
          '">' +
          address +
          "</a>.";
      }
    });
  });

  /* ---------- Tier buttons prefill the sponsor form ---------- */
  document.querySelectorAll("[data-tier]").forEach(function (button) {
    button.addEventListener("click", function () {
      var select = document.getElementById("sponsor-tier");
      if (!select) return;
      var tier = button.getAttribute("data-tier");
      Array.prototype.forEach.call(select.options, function (option) {
        if (option.value.indexOf(tier) === 0) select.value = option.value;
      });
    });
  });

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (element) {
    element.textContent = new Date().getFullYear();
  });
})();
