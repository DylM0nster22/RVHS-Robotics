/* River Valley Robotics — live donor wall
 *
 * sponsors.html is built with a snapshot of the Hack Club Bank donations feed.
 * This script refreshes that snapshot in the browser, so a new public gift
 * appears on the wall without rebuilding the site. If the request fails (school
 * network, blocked request, HCB outage) the built-in snapshot stays in place.
 */
(function () {
  "use strict";

  var wall = document.querySelector("[data-donor-wall]");
  if (!wall) return;

  var api = wall.getAttribute("data-donor-api");
  var ledger = wall.getAttribute("data-donor-ledger") || "";
  var list = wall.querySelector("[data-donor-list]");
  var meta = document.querySelector("[data-donor-meta]");
  var fallback = document.querySelector("[data-donor-fallback]");
  var levels = [];

  try {
    levels = JSON.parse(wall.getAttribute("data-donor-levels") || "[]");
  } catch (error) {
    levels = [];
  }

  if (!api || !list || !levels.length) return;
  if (typeof fetch !== "function") return;

  var SKIP_STATUS = { failed: 1, refunded: 1, reversed: 1, cancelled: 1, canceled: 1 };
  var EMPTY_TEXT = "No public gifts yet. The first name on the wall could be yours.";

  var levelFor = function (cents) {
    for (var i = 0; i < levels.length; i += 1) {
      if (cents >= levels[i].min * 100) return levels[i];
    }
    return levels[levels.length - 1];
  };

  var initials = function (name) {
    var words = String(name)
      .replace(/[^0-9A-Za-z .&'-]/g, " ")
      .split(" ")
      .filter(function (word) {
        return word;
      });
    if (!words.length) return "?";
    if (words.length === 1) return words[0].charAt(0).toUpperCase();
    return (words[0].charAt(0) + words[words.length - 1].charAt(0)).toUpperCase();
  };

  var safeUrl = function (value) {
    var text = String(value || "").trim();
    return /^(https?:\/\/|\/|assets\/)/i.test(text) ? text : "";
  };

  var settingsFor = function (name, config) {
    if (!config || !config.sponsors) return {};
    var wanted = String(name).toLowerCase();
    var keys = Object.keys(config.sponsors);
    for (var i = 0; i < keys.length; i += 1) {
      if (keys[i].toLowerCase() === wanted) {
        var value = config.sponsors[keys[i]];
        return value && typeof value === "object" ? value : {};
      }
    }
    return {};
  };

  var aggregate = function (donations, config) {
    var seen = {};
    var rows = [];

    donations.forEach(function (donation) {
      if (!donation || typeof donation !== "object") return;
      if (SKIP_STATUS[String(donation.status || "").toLowerCase()]) return;

      var cents = Number(donation.amount_cents) || 0;
      if (cents <= 0) return;

      var donor = donation.donor || {};
      var name = String(donor.name || "").trim();
      var anonymous = Boolean(donor.anonymous) || !name;
      var key = anonymous ? "__anonymous__" : name.toLowerCase();
      var row = seen[key];

      if (!row) {
        row = seen[key] = {
          name: anonymous ? "Anonymous" : name,
          cents: 0,
        };
        rows.push(row);
      }
      row.cents += cents;
    });

    var donors = [];

    rows.forEach(function (row) {
      var settings = settingsFor(row.name, config);
      if (settings.hide) return;

      var display = String(settings.display || row.name).trim() || row.name;
      var tier = levelFor(row.cents);
      var forced = String(settings.tier || "").trim().toLowerCase();

      if (forced) {
        for (var i = 0; i < levels.length; i += 1) {
          if (levels[i].label.toLowerCase() === forced || levels[i].slug === forced) {
            tier = levels[i];
            break;
          }
        }
      }

      donors.push({
        name: display,
        initials: initials(display),
        tier: tier,
        cents: row.cents,
        logo: safeUrl(settings.logo),
        url: safeUrl(settings.url),
      });
    });

    donors.sort(function (a, b) {
      if (b.tier.min !== a.tier.min) return b.tier.min - a.tier.min;
      if (b.cents !== a.cents) return b.cents - a.cents;
      return a.name.localeCompare(b.name);
    });

    return donors;
  };

  var buildCard = function (donor) {
    var card = document.createElement("li");
    card.className = "donor-card";
    card.setAttribute("data-tier", donor.tier.slug);

    if (donor.logo) {
      var logo = document.createElement("img");
      logo.className = "donor-logo";
      logo.src = donor.logo;
      logo.alt = "";
      logo.width = 96;
      logo.height = 56;
      logo.loading = "lazy";
      logo.decoding = "async";
      card.appendChild(logo);
    } else {
      var mark = document.createElement("span");
      mark.className = "donor-mark";
      mark.setAttribute("aria-hidden", "true");
      mark.textContent = donor.initials;
      card.appendChild(mark);
    }

    var body = document.createElement("span");
    body.className = "donor-body";

    var name;
    if (donor.url) {
      name = document.createElement("a");
      name.href = donor.url;
      name.target = "_blank";
      name.rel = "noopener sponsored";
    } else {
      name = document.createElement("span");
    }
    name.className = "donor-name";
    name.textContent = donor.name;
    body.appendChild(name);

    card.appendChild(body);
    return card;
  };

  var tierNote = function (tier) {
    if (tier.note) return tier.note;
    if (tier.min > 0) return "$" + tier.min.toLocaleString("en-US") + " and up";

    var next = null;
    levels.forEach(function (level) {
      if (level.min > 0 && (next === null || level.min < next)) next = level.min;
    });
    return next === null ? "any gift" : "under $" + next.toLocaleString("en-US");
  };

  var groupByTier = function (donors) {
    var groups = [];
    var bySlug = {};

    donors.forEach(function (donor) {
      var group = bySlug[donor.tier.slug];
      if (!group) {
        group = bySlug[donor.tier.slug] = { tier: donor.tier, donors: [] };
        groups.push(group);
      }
      group.donors.push(donor);
    });

    return groups;
  };

  var buildTier = function (group) {
    var tier = group.tier;
    var section = document.createElement("section");
    section.className = "donor-tier";
    section.setAttribute("data-tier", tier.slug);
    section.setAttribute("aria-labelledby", "donor-tier-" + tier.slug);

    var head = document.createElement("div");
    head.className = "donor-tier-head";

    var heading = document.createElement("h3");
    heading.className = "donor-tier-name";
    heading.id = "donor-tier-" + tier.slug;
    heading.textContent = tier.label;
    head.appendChild(heading);

    var note = document.createElement("span");
    note.className = "donor-tier-note";
    note.textContent = tierNote(tier);
    head.appendChild(note);

    var count = document.createElement("span");
    count.className = "donor-tier-count";
    count.textContent =
      group.donors.length + (group.donors.length === 1 ? " donor" : " donors");
    head.appendChild(count);

    section.appendChild(head);

    var grid = document.createElement("ul");
    grid.className = "donor-grid";
    group.donors.forEach(function (donor) {
      grid.appendChild(buildCard(donor));
    });
    section.appendChild(grid);

    return section;
  };

  var render = function (donors) {
    var frag = document.createDocumentFragment();
    var groups = groupByTier(donors);

    if (!groups.length) {
      var empty = document.createElement("p");
      empty.className = "donor-wall-empty";
      empty.textContent = EMPTY_TEXT;
      frag.appendChild(empty);
    } else {
      groups.forEach(function (group) {
        frag.appendChild(buildTier(group));
      });
    }

    list.textContent = "";
    list.appendChild(frag);

    if (meta) {
      meta.textContent = "";
      if (donors.length) {
        meta.appendChild(
          document.createTextNode(
            donors.length +
              (donors.length === 1 ? " public donor" : " public donors") +
              " \u00b7 live from "
          )
        );
        if (ledger) {
          var ledgerLink = document.createElement("a");
          ledgerLink.href = ledger;
          ledgerLink.target = "_blank";
          ledgerLink.rel = "noopener";
          ledgerLink.textContent = "Hack Club Bank";
          meta.appendChild(ledgerLink);
        }
      } else {
        meta.appendChild(document.createTextNode("No public gifts yet. "));
        if (ledger) {
          var emptyLink = document.createElement("a");
          emptyLink.href = ledger;
          emptyLink.target = "_blank";
          emptyLink.rel = "noopener";
          emptyLink.textContent = "See the ledger";
          meta.appendChild(emptyLink);
        }
      }
    }

    if (fallback) fallback.hidden = true;
  };

  var getJSON = function (url) {
    var options = { cache: "no-store", headers: { Accept: "application/json" } };

    if ("AbortController" in window) {
      var controller = new AbortController();
      options.signal = controller.signal;
      setTimeout(function () {
        controller.abort();
      }, 8000);
    }

    return fetch(url, options).then(function (response) {
      if (!response.ok) throw new Error("HTTP " + response.status);
      return response.json();
    });
  };

  var configRequest = getJSON("assets/data/donors.json").catch(function () {
    return null;
  });

  var fetchAll = function () {
    var all = [];

    var loadPage = function (page) {
      return getJSON(api + "&page=" + page).then(function (batch) {
        if (!Array.isArray(batch) || !batch.length) return all;
        all = all.concat(batch);
        if (batch.length < 100 || page >= 3) return all;
        return loadPage(page + 1);
      });
    };

    return loadPage(1);
  };

  Promise.all([fetchAll(), configRequest])
    .then(function (results) {
      render(aggregate(results[0], results[1]));
    })
    .catch(function () {
      /* Keep the snapshot rendered at build time. */
    });
})();
