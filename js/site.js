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

    window.matchMedia("(min-width: 981px)").addEventListener("change", function (event) {
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

  /* ---------- Animated stat counters ---------- */
  var counters = document.querySelectorAll("[data-count]");
  var animateCounter = function (element) {
    var target = parseInt(element.getAttribute("data-count"), 10);
    if (isNaN(target)) return;
    var suffix = element.querySelector(".suffix");
    var suffixHTML = suffix ? suffix.outerHTML : "";
    var duration = 1300;
    var startTime = null;

    var step = function (timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var value = Math.round(target * eased);
      element.innerHTML = value.toLocaleString("en-US") + suffixHTML;
      if (progress < 1) window.requestAnimationFrame(step);
    };

    window.requestAnimationFrame(step);
  };

  if (counters.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      counters.forEach(function (counter) {
        counter.innerHTML =
          parseInt(counter.getAttribute("data-count"), 10).toLocaleString("en-US") +
          (counter.querySelector(".suffix") ? counter.querySelector(".suffix").outerHTML : "");
      });
    } else {
      var counterObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCounter(entry.target);
              counterObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.5 }
      );
      counters.forEach(function (counter) {
        counterObserver.observe(counter);
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

  /* ---------- Copy buttons ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", function () {
      var value = button.getAttribute("data-copy");
      var original = button.textContent;
      var done = function () {
        button.textContent = "Copied";
        window.setTimeout(function () {
          button.textContent = original;
        }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(value).then(done).catch(done);
      } else {
        done();
      }
    });
  });

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (element) {
    element.textContent = new Date().getFullYear();
  });
})();
