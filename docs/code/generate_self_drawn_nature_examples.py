from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Wedge
import numpy as np


ROOT = Path(__file__).resolve().parents[2]

STYLE = {
    "grid": "#E3E7EC",
    "face": "#F8FAFC",
    "spine": "#000000",
    "muted": "#4B5563",
    "text": "#222222",
    "border": "#CBD5E1",
}

NPG_HEX = [
    "#E64B35",
    "#4DBBD5",
    "#00A087",
    "#3C5488",
    "#F39B7F",
    "#8491B4",
    "#91D1C2",
    "#DC0000",
    "#7E6148",
    "#B09C85",
]

RED = NPG_HEX[0]
BLUE = NPG_HEX[1]
TEAL = NPG_HEX[2]
NAVY = NPG_HEX[3]
ORANGE = NPG_HEX[4]
PURPLE = NPG_HEX[5]
BROWN = NPG_HEX[8]
GRAY = STYLE["muted"]
LIGHT = STYLE["face"]
DARK = STYLE["text"]
FONT_FAMILY = "Arial"


def configure_matplotlib() -> None:
    plt.rcParams.update(
        {
            "font.family": FONT_FAMILY,
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
            "mathtext.fontset": "cm",
            "axes.linewidth": 0.75,
            "axes.facecolor": STYLE["face"],
            "grid.color": STYLE["grid"],
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 5.5,
            "ytick.major.size": 5.5,
            "xtick.major.width": 0.75,
            "ytick.major.width": 0.75,
            "font.size": 10,
            "axes.labelsize": 11,
            "axes.titlesize": 13,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 10,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def setup_axis(ax: plt.Axes) -> None:
    ax.set_facecolor(STYLE["face"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(STYLE["spine"])
    ax.spines["bottom"].set_color(STYLE["spine"])
    ax.spines["left"].set_linewidth(0.75)
    ax.spines["bottom"].set_linewidth(0.75)
    ax.tick_params(labelsize=9, width=0.75, length=5.5, direction="out")
    ax.grid(axis="y", color=STYLE["grid"], linewidth=0.65)
    ax.set_axisbelow(True)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontfamily(FONT_FAMILY)


def set_y_ticks_as_limits(ax: plt.Axes, ticks) -> None:
    """Use explicit y ticks and make the upper axis limit end on a tick."""
    ticks = np.asarray(ticks, dtype=float)
    ax.set_ylim(float(ticks[0]), float(ticks[-1]))
    ax.set_yticks(ticks)


def annotate_bars(ax: plt.Axes, bars) -> None:
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.08,
            f"{height:.1f}",
            ha="center",
            va="bottom",
            fontsize=9,
            color=DARK,
            fontfamily=FONT_FAMILY,
        )


def save(fig: plt.Figure, relpath: str) -> None:
    path = ROOT / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=220, bbox_inches="tight", pad_inches=0.08, facecolor="white")
    plt.close(fig)


def canvas(width: float = 6.0, height: float = 4.0):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.patch.set_facecolor("white")
    return fig, ax


def title(ax, text: str, x: float = 0.04, y: float = 0.95) -> None:
    ax.text(x, y, text, ha="left", va="top", fontsize=15, fontweight="bold", color=DARK, fontfamily=FONT_FAMILY)


def small_label(ax, text: str, x: float, y: float, color: str = DARK, **kwargs) -> None:
    ax.text(
        x,
        y,
        text,
        ha=kwargs.pop("ha", "center"),
        va=kwargs.pop("va", "center"),
        fontsize=11,
        color=color,
        fontfamily=FONT_FAMILY,
        **kwargs,
    )


def add_panel(ax, x, y, w, h, label, color=LIGHT):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=STYLE["border"], lw=0.8))
    ax.text(
        x + 0.03,
        y + h - 0.04,
        label,
        ha="left",
        va="top",
        fontsize=11,
        fontweight="bold",
        color=DARK,
        fontfamily=FONT_FAMILY,
    )


def axis_avoid():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.linspace(0, 10, 8)
    y = np.array([2.0, 2.4, 2.2, 3.1, 3.6, 3.3, 4.1, 4.5])
    ax.plot(x, y, marker="o", lw=2.5, color=BLUE)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("Missing scale and units", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/axis-avoid-missing-ticks.png")


def axis_recommended():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.linspace(0, 10, 8)
    y = np.array([2.0, 2.4, 2.2, 3.1, 3.6, 3.3, 4.1, 4.5])
    ax.plot(x, y, marker="o", lw=2.5, color=BLUE)
    set_y_ticks_as_limits(ax, np.arange(1.5, 5.01, 0.5))
    ax.set_xlabel("Training time (h)")
    ax.set_ylabel("Accuracy (%)")
    ax.grid(True, color=STYLE["grid"], lw=0.65)
    ax.set_title("Readable axis labels", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/axis-recommended-labels.png")


def accuracy_avoid_truncated_axis():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.arange(3)
    values = np.array([0.82, 0.86, 0.88])
    bars = ax.bar(x, values, width=0.46, color=[BLUE, ORANGE, TEAL], edgecolor="black", linewidth=0.75)
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.002,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
            color=DARK,
            fontfamily=FONT_FAMILY,
        )
    set_y_ticks_as_limits(ax, np.arange(0.80, 0.901, 0.02))
    ax.set_xticks(x, ["A", "B", "C"])
    ax.set_ylabel("Accuracy")
    ax.set_title("Truncated axis exaggerates differences", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/axis-avoid-truncated.png")


def accuracy_recommended_full_scale():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.arange(3)
    values = np.array([0.82, 0.86, 0.88])
    bars = ax.bar(x, values, width=0.46, color=[BLUE, ORANGE, TEAL], edgecolor="black", linewidth=0.75)
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.025,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
            color=DARK,
            fontfamily=FONT_FAMILY,
        )
    set_y_ticks_as_limits(ax, np.arange(0, 1.01, 0.2))
    ax.set_xticks(x, ["A", "B", "C"])
    ax.set_ylabel("Accuracy")
    ax.set_title("Full scale shows actual differences", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/axis-recommended-full-scale.png")


def labels_avoid():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    rng = np.random.default_rng(4)
    x = rng.normal(0.5, 0.11, 22)
    y = rng.normal(0.5, 0.10, 22)
    ax.scatter(x, y, s=60, color=TEAL)
    for i, (xi, yi) in enumerate(zip(x, y), 1):
        ax.text(xi, yi, f"sample {i}", fontsize=8.5, color=DARK, fontfamily=FONT_FAMILY)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Labels cover the data", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/labels-avoid-overlap.png")


def labels_recommended():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.array([0.18, 0.32, 0.47, 0.63, 0.80])
    y = np.array([0.35, 0.58, 0.44, 0.72, 0.50])
    ax.scatter(x, y, s=70, color=TEAL)
    for i, (xi, yi) in enumerate(zip(x, y), 1):
        ax.annotate(f"S{i}", (xi, yi), xytext=(xi + 0.04, yi + 0.06), textcoords="data",
                    arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.75), fontsize=10, fontfamily=FONT_FAMILY)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Labels are sparse and offset", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/labels-recommended-rearranged.png")


def colourblind_avoid():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.arange(4)
    bars_a = ax.bar(x - 0.18, [3, 4, 5, 4], width=0.36, color=RED, label="A")
    bars_b = ax.bar(x + 0.18, [2.8, 3.8, 4.8, 3.9], width=0.36, color=TEAL, label="B")
    annotate_bars(ax, bars_a)
    annotate_bars(ax, bars_b)
    set_y_ticks_as_limits(ax, np.arange(0, 6.1, 1))
    ax.set_xticks(x, ["G1", "G2", "G3", "G4"])
    ax.legend(frameon=False)
    ax.set_title("Red and green are easy to confuse", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/colourblind-avoid-red-green.png")


def colourblind_recommended():
    fig, ax = plt.subplots(figsize=(5.6, 3.5))
    setup_axis(ax)
    x = np.arange(4)
    bars_a = ax.bar(x - 0.18, [3, 4, 5, 4], width=0.36, color=BLUE, label="A")
    bars_b = ax.bar(x + 0.18, [2.8, 3.8, 4.8, 3.9], width=0.36, color=ORANGE, hatch="//", label="B")
    annotate_bars(ax, bars_a)
    annotate_bars(ax, bars_b)
    set_y_ticks_as_limits(ax, np.arange(0, 6.1, 1))
    ax.set_xticks(x, ["G1", "G2", "G3", "G4"])
    ax.legend(frameon=False)
    ax.set_title("Hue and pattern separate groups", loc="left", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/colourblind-recommended-contrast.png")


def legend_avoid():
    fig, ax = canvas()
    title(ax, "Legend encoded as colored words")
    for i, (name, color) in enumerate([("control", BLUE), ("method", ORANGE), ("baseline", TEAL)]):
        ax.plot([0.18, 0.82], [0.70 - i * 0.16, 0.62 - i * 0.16], lw=3, color=color)
        ax.text(0.10, 0.70 - i * 0.16, name, color=color, fontsize=11, ha="left", va="center", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures-extra/legend-avoid-coloured-text.png")


def legend_recommended():
    fig, ax = canvas()
    title(ax, "Legend uses swatches and black text")
    for i, (name, color) in enumerate([("Control", BLUE), ("Method", ORANGE), ("Baseline", TEAL)]):
        y = 0.72 - i * 0.16
        ax.add_patch(Rectangle((0.12, y - 0.025), 0.06, 0.05, facecolor=color, edgecolor="none"))
        ax.text(0.21, y, name, color=DARK, fontsize=11, ha="left", va="center", fontfamily=FONT_FAMILY)
        ax.plot([0.45, 0.82], [y, y + 0.04], lw=3, color=color)
    save(fig, "docs/fig/nature-preparing-figures-extra/legend-recommended-colour-boxes.png")


def patterns_avoid():
    fig, ax = canvas()
    title(ax, "Dense pattern fill")
    center = (0.50, 0.46)
    vals = [90, 80, 70, 120]
    start = 0
    colors = ["#DDDDDD", "#BBBBBB", "#999999", "#777777"]
    hatches = ["////", "\\\\\\\\", "xxxx", "...."]
    for v, c, h in zip(vals, colors, hatches):
        ax.add_patch(Wedge(center, 0.32, start, start + v, facecolor=c, edgecolor=DARK, hatch=h, lw=1.0))
        start += v
    save(fig, "docs/fig/nature-preparing-figures-extra/patterns-avoid-pie.png")


def patterns_recommended():
    fig, ax = canvas()
    title(ax, "Solid colors with labels")
    center = (0.50, 0.46)
    vals = [90, 80, 70, 120]
    start = 0
    colors = [BLUE, ORANGE, TEAL, PURPLE]
    for i, (v, c) in enumerate(zip(vals, colors)):
        ax.add_patch(Wedge(center, 0.32, start, start + v, facecolor=c, edgecolor="white", lw=1.5))
        ang = np.deg2rad(start + v / 2)
        small_label(ax, f"{i + 1}", center[0] + 0.21 * np.cos(ang), center[1] + 0.21 * np.sin(ang), color="white", fontweight="bold")
        start += v
    save(fig, "docs/fig/nature-preparing-figures-extra/patterns-recommended-solid.png")


def contrast_avoid():
    fig, ax = canvas()
    ax.add_patch(Rectangle((0, 0), 1, 1, facecolor="#DDE7F2", edgecolor="none"))
    title(ax, "Low contrast text")
    ax.text(0.5, 0.52, "Important label", fontsize=24, color="#AAB7C4", ha="center", va="center", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/contrast-avoid-low.png")


def contrast_recommended():
    fig, ax = canvas()
    ax.add_patch(Rectangle((0, 0), 1, 1, facecolor="#F8FAFC", edgecolor="none"))
    title(ax, "High contrast text")
    ax.text(0.5, 0.52, "Important label", fontsize=24, color=DARK, ha="center", va="center", fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/contrast-recommended-high.png")


def icons_avoid():
    fig, ax = canvas()
    title(ax, "Decorative icons only")
    xs = [0.22, 0.40, 0.58, 0.76]
    markers = ["*", "P", "X", "D"]
    colors = [BLUE, ORANGE, TEAL, PURPLE]
    for x, m, c in zip(xs, markers, colors):
        ax.scatter([x], [0.52], s=900, marker=m, color=c)
    save(fig, "docs/fig/nature-preparing-figures/icons-avoid-decorative.png")


def icons_recommended():
    fig, ax = canvas()
    title(ax, "Text labels identify categories")
    xs = [0.22, 0.40, 0.58, 0.76]
    labels = ["Data", "Model", "Loss", "Output"]
    colors = [BLUE, ORANGE, TEAL, PURPLE]
    for x, lab, c in zip(xs, labels, colors):
        ax.add_patch(Circle((x, 0.58), 0.055, facecolor=c, edgecolor="none"))
        ax.text(x, 0.42, lab, ha="center", va="center", fontsize=10.5, color=DARK, fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures/icons-recommended-text-labels.png")


def protein_avoid():
    fig, ax = canvas()
    title(ax, "Colored labels on busy background")
    rng = np.random.default_rng(2)
    pts = rng.normal([0.5, 0.47], [0.18, 0.12], size=(90, 2))
    ax.plot(pts[:, 0], pts[:, 1], color=PURPLE, lw=0.8, alpha=0.75)
    ax.text(0.42, 0.55, "site A", color=NPG_HEX[6], fontsize=11, fontweight="bold", fontfamily=FONT_FAMILY)
    ax.text(0.62, 0.39, "site B", color=ORANGE, fontsize=11, fontweight="bold", fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures-extra/protein-avoid-coloured-labels.png")


def protein_recommended():
    fig, ax = canvas()
    title(ax, "Black labels with keylines")
    rng = np.random.default_rng(2)
    pts = rng.normal([0.5, 0.47], [0.18, 0.12], size=(90, 2))
    ax.plot(pts[:, 0], pts[:, 1], color=PURPLE, lw=0.8, alpha=0.75)
    ax.annotate("site A", (0.45, 0.55), xytext=(0.28, 0.73), arrowprops=dict(arrowstyle="-", color=DARK, lw=0.75), fontsize=11, fontfamily=FONT_FAMILY)
    ax.annotate("site B", (0.62, 0.40), xytext=(0.72, 0.23), arrowprops=dict(arrowstyle="-", color=DARK, lw=0.75), fontsize=11, fontfamily=FONT_FAMILY)
    save(fig, "docs/fig/nature-preparing-figures-extra/protein-recommended-keylines.png")


def panels_avoid():
    fig, ax = canvas()
    title(ax, "Random panel placement")
    specs = [(0.10, 0.55, 0.28, 0.22, "c"), (0.50, 0.62, 0.35, 0.18, "a"), (0.18, 0.20, 0.22, 0.25, "d"), (0.58, 0.24, 0.26, 0.22, "b")]
    for x, y, w, h, lab in specs:
        add_panel(ax, x, y, w, h, lab)
    save(fig, "docs/fig/nature-preparing-figures/panels-avoid-random.png")


def panels_recommended():
    fig, ax = canvas()
    title(ax, "Ordered grid panels")
    for i, lab in enumerate(["a", "b", "c", "d"]):
        x = 0.12 + (i % 2) * 0.40
        y = 0.52 - (i // 2) * 0.30
        add_panel(ax, x, y, 0.32, 0.22, lab)
    save(fig, "docs/fig/nature-preparing-figures/panels-recommended-ordered.png")


def font_avoid():
    fig, ax = canvas()
    title(ax, "Inconsistent decorative fonts")
    ax.text(0.5, 0.62, "Panel A", fontfamily="fantasy", fontsize=20, ha="center", color=DARK)
    ax.text(0.5, 0.45, "Result label", fontfamily="cursive", fontsize=17, ha="center", color=DARK)
    ax.text(0.5, 0.30, "axis title", fontfamily="monospace", fontsize=15, ha="center", color=DARK)
    save(fig, "docs/fig/nature-preparing-figures/font-avoid-nonstandard.png")


def font_recommended():
    fig, ax = canvas()
    title(ax, "Consistent standard font")
    for y, text, size, weight in [(0.62, "Panel A", 24, "bold"), (0.45, "Result label", 20, "normal"), (0.30, "axis title", 18, "normal")]:
        ax.text(0.5, y, text, fontfamily=FONT_FAMILY, fontsize=size, fontweight=weight, ha="center", color=DARK)
    save(fig, "docs/fig/nature-preparing-figures/font-recommended-standard.png")


def font_samples():
    samples = [
        ("docs/fig/nature-preparing-figures-extra/font-sans-serif-body.png", "Sans-serif body text", FONT_FAMILY, "Regular labels remain readable."),
        ("docs/fig/nature-preparing-figures-extra/font-bold-labels.png", "Bold panel label", FONT_FAMILY, "a  Main result"),
        ("docs/fig/nature-preparing-figures-extra/font-courier-code.png", "Monospace code label", "DejaVu Sans Mono", "model = fit(data)"),
        ("docs/fig/nature-preparing-figures-extra/font-symbol-greek.png", "Scientific symbols", FONT_FAMILY, "alpha + beta -> gamma"),
    ]
    for path, heading, family, text in samples:
        fig, ax = canvas(5.4, 2.2)
        title(ax, heading)
        ax.text(0.5, 0.42, text, fontfamily=family, fontsize=18, ha="center", va="center", color=DARK, fontweight="bold" if "Bold" in heading else "normal")
        save(fig, path)


def sizing_single():
    fig, ax = canvas(5.0, 3.2)
    title(ax, "Single-column figure")
    ax.add_patch(Rectangle((0.28, 0.24), 0.44, 0.48, facecolor=LIGHT, edgecolor=DARK, lw=1.4))
    ax.add_patch(FancyArrowPatch((0.28, 0.15), (0.72, 0.15), arrowstyle="<->", mutation_scale=14, color=DARK))
    small_label(ax, "one column width", 0.50, 0.08)
    save(fig, "docs/fig/nature-preparing-figures/sizing-single-column.png")


def sizing_double():
    fig, ax = canvas(6.4, 3.2)
    title(ax, "Double-column figure")
    ax.add_patch(Rectangle((0.12, 0.24), 0.76, 0.48, facecolor=LIGHT, edgecolor=DARK, lw=1.4))
    for x in [0.34, 0.56]:
        ax.plot([x, x], [0.24, 0.72], color=STYLE["border"], lw=0.75)
    ax.add_patch(FancyArrowPatch((0.12, 0.15), (0.88, 0.15), arrowstyle="<->", mutation_scale=14, color=DARK))
    small_label(ax, "two column width", 0.50, 0.08)
    save(fig, "docs/fig/nature-preparing-figures/sizing-double-column.png")


def text_editability():
    fig, ax = canvas()
    title(ax, "Outlined text becomes shapes")
    ax.text(0.5, 0.52, "TEXT", fontsize=34, ha="center", va="center", color="none", path_effects=[], fontweight="bold", fontfamily=FONT_FAMILY)
    ax.text(0.5, 0.52, "TEXT", fontsize=34, ha="center", va="center", color=STYLE["face"], fontweight="bold", fontfamily=FONT_FAMILY,
            bbox=dict(facecolor="#9CA3AF", edgecolor="none", pad=8))
    ax.plot([0.28, 0.72], [0.32, 0.32], color=RED, lw=3)
    small_label(ax, "not editable", 0.5, 0.22, color=RED)
    save(fig, "docs/fig/nature-preparing-figures/text-avoid-outlined.png")

    fig, ax = canvas()
    title(ax, "Text remains editable")
    ax.text(0.5, 0.52, "TEXT", fontsize=34, ha="center", va="center", color=DARK, fontweight="bold", fontfamily=FONT_FAMILY)
    ax.add_patch(Rectangle((0.30, 0.42), 0.40, 0.18, facecolor="none", edgecolor=BLUE, lw=1.5, linestyle="--"))
    small_label(ax, "text layer", 0.5, 0.28, color=BLUE)
    save(fig, "docs/fig/nature-preparing-figures/text-recommended-editable.png")


def microscopy_like(path: str, title_text: str, mode: str) -> None:
    fig, ax = canvas(5.2, 3.5)
    title(ax, title_text)
    rng = np.random.default_rng(7)
    img = np.zeros((180, 260, 3), dtype=float)
    for _ in range(45):
        cx, cy = rng.integers(20, 240), rng.integers(20, 160)
        rr = rng.integers(5, 18)
        yy, xx = np.ogrid[:180, :260]
        mask = (xx - cx) ** 2 + (yy - cy) ** 2 < rr ** 2
        color = np.array([0.1, 0.9, 0.55]) if mode != "cmyk" else np.array([0.28, 0.46, 0.34])
        img[mask] = np.maximum(img[mask], color * rng.uniform(0.5, 1.0))
    if mode == "lowres":
        img = img[::12, ::12].repeat(12, axis=0).repeat(12, axis=1)
    ax.imshow(img, extent=(0.16, 0.84, 0.20, 0.76), interpolation="nearest" if mode == "lowres" else "bilinear")
    if mode == "flat":
        ax.text(0.28, 0.68, "cell", color="white", fontsize=10, alpha=0.55, fontfamily=FONT_FAMILY)
        ax.plot([0.58, 0.76], [0.27, 0.27], color="white", lw=3, alpha=0.55)
    if mode == "editable":
        ax.annotate("cell", (0.45, 0.55), xytext=(0.25, 0.70), color="white",
                    arrowprops=dict(arrowstyle="-", color="white", lw=0.9), fontsize=11, fontfamily=FONT_FAMILY)
        ax.plot([0.58, 0.76], [0.27, 0.27], color="white", lw=3)
        small_label(ax, "20 um", 0.67, 0.22, color="white")
    save(fig, path)


def checklist_images():
    microscopy_like("checklists/fig/nature-preparing-figures/colour-space-avoid-cmyk.png", "Muted color conversion", "cmyk")
    microscopy_like("checklists/fig/nature-preparing-figures/colour-space-recommended-rgb.png", "RGB preserves bright signal", "rgb")
    microscopy_like("checklists/fig/nature-preparing-figures/resolution-avoid-low.png", "Low resolution pixelates details", "lowres")
    microscopy_like("checklists/fig/nature-preparing-figures/resolution-recommended-high.png", "High resolution keeps details", "rgb")
    microscopy_like("checklists/fig/nature-preparing-figures/scale-bar-avoid-flattened.png", "Flattened annotation layer", "flat")
    microscopy_like("checklists/fig/nature-preparing-figures/scale-bar-recommended-editable.png", "Editable annotation layer", "editable")


def main() -> None:
    configure_matplotlib()
    axis_avoid()
    axis_recommended()
    accuracy_avoid_truncated_axis()
    accuracy_recommended_full_scale()
    labels_avoid()
    labels_recommended()
    colourblind_avoid()
    colourblind_recommended()
    legend_avoid()
    legend_recommended()
    patterns_avoid()
    patterns_recommended()
    contrast_avoid()
    contrast_recommended()
    icons_avoid()
    icons_recommended()
    protein_avoid()
    protein_recommended()
    panels_avoid()
    panels_recommended()
    font_avoid()
    font_recommended()
    font_samples()
    sizing_single()
    sizing_double()
    text_editability()
    checklist_images()


if __name__ == "__main__":
    main()
