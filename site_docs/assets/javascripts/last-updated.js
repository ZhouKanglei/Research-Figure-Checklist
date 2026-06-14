(function () {
  function formatDate(value) {
    var date = new Date(value);
    if (Number.isNaN(date.getTime())) {
      return "";
    }
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "long",
      day: "2-digit",
    }).format(date);
  }

  function renderLastUpdated() {
    var footer = document.querySelector(".md-copyright");
    if (!footer) {
      return;
    }

    var text = formatDate(document.lastModified);
    if (!text) {
      return;
    }

    var existing = footer.querySelector(".site-last-updated");
    if (!existing) {
      existing = document.createElement("span");
      existing.className = "site-last-updated";
      existing.innerHTML =
        '<span class="site-last-updated__label">Last updated on</span> ' +
        '<span class="site-last-updated__date"></span>';
      footer.appendChild(existing);
    }

    var dateNode = existing.querySelector(".site-last-updated__date");
    if (dateNode) {
      dateNode.textContent = text;
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderLastUpdated);
  } else {
    renderLastUpdated();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(renderLastUpdated);
  }
})();
