(function () {
  function renderMermaid() {
    if (typeof mermaid === "undefined") {
      return;
    }

    mermaid.initialize({
      startOnLoad: false,
      theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default",
    });

    document.querySelectorAll(".mermaid").forEach(function (element) {
      element.removeAttribute("data-processed");
    });

    mermaid.run({
      querySelector: ".mermaid",
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderMermaid);
  } else {
    renderMermaid();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(renderMermaid);
  }
})();
