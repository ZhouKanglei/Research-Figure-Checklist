(function () {
  function normalize(text) {
    return (text || "").replace(/\s+/g, "");
  }

  function expandCaseNavigation() {
    var labels = document.querySelectorAll(".md-nav__link[for]");

    labels.forEach(function (label) {
      if (normalize(label.textContent) !== "案例分析") {
        return;
      }

      var input = document.getElementById(label.getAttribute("for"));
      if (input) {
        input.checked = true;
      }

      var item = label.closest(".md-nav__item");
      if (!item) {
        return;
      }

      item
        .querySelectorAll("input.md-nav__toggle")
        .forEach(function (toggle) {
          toggle.checked = true;
        });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", expandCaseNavigation);
  } else {
    expandCaseNavigation();
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(expandCaseNavigation);
  }
})();
