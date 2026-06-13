import subprocess

import matplotlib.pyplot as plt
import numpy as np


STYLE = {
    "grid": "#E3E7EC",
    "face": "#F8FAFC",
    "spine": "#000000",
    "muted": "#4B5563",
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


FONT_CANDIDATES = [
    ("Arial", "Common choice for English \npaper figures"),
    ("Helvetica", "Common alternative;\nmay fall back on Linux"),
    ("DejaVu Sans", "Common Linux fallback font"),
    ("Latin Modern Math", "Math style reference;\ncheck availability"),
]


def matched_font_name(font_name):
    try:
        result = subprocess.run(
            ["fc-match", "-f", "%{family[0]}", font_name],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() or "unknown"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def setup_axis(ax):
    ax.set_facecolor(STYLE["face"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(STYLE["spine"])
    ax.spines["bottom"].set_color(STYLE["spine"])
    ax.spines["left"].set_linewidth(0.75)
    ax.spines["bottom"].set_linewidth(0.75)
    ax.tick_params(labelsize=8.5, width=0.75, length=5.5, direction="out")
    ax.grid(axis="y", color=STYLE["grid"], linewidth=0.65)
    ax.set_axisbelow(True)


def draw_type_comparison(ax, title, font_name, description):
    actual_font = matched_font_name(font_name)
    family = actual_font if actual_font != "unknown" else font_name
    x = np.arange(3)
    values = np.array([0.68, 0.74, 0.82])

    setup_axis(ax)
    bars = ax.bar(x, values, width=0.42, color=NPG_HEX[:3], alpha=0.50, edgecolor="black", linewidth=0.8)
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.012,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
            fontfamily=family,
            color="#222222",
        )

    ax.set_ylim(0.50, 0.90)
    ax.set_yticks(np.arange(0.50, 0.91, 0.10))
    ax.set_xticks(x)
    ax.set_xticklabels(["D1", "D2", "D3"], fontfamily=family)
    ax.set_ylabel("Score", fontfamily=family, fontsize=10)
    ax.set_title(title, fontfamily=family, fontweight="bold", fontsize=13, pad=8)
    ax.text(
        0.02,
        0.93,
        f"Requested: {font_name} | Matched: {actual_font}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        fontfamily=family,
        color=STYLE["muted"],
    )
    ax.text(
        0.02,
        -0.22,
        description,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=10,
        fontfamily=family,
        color=STYLE["muted"],
        clip_on=False,
    )


def draw_row(ax, requested_font, note):
    actual_font = matched_font_name(requested_font)
    family = actual_font if actual_font != "unknown" else requested_font

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.02, 0.76, requested_font, fontfamily=family, fontsize=14.5, fontweight="bold", color="#111111")
    ax.text(0.02, 0.48, f"Matched font: {actual_font}", fontfamily="Arial", fontsize=10, color=STYLE["muted"])
    ax.text(0.02, 0.22, note, fontfamily="Arial", fontsize=10, color=STYLE["muted"])

    ax.text(
        0.34,
        0.67,
        "Accuracy 0.82  |  Macro-AUC 0.76",
        fontfamily=family,
        fontsize=11.2,
        color="#222222",
    )
    ax.text(
        0.34,
        0.38,
        "x = [1, 2, 3], y = [0.61, 0.70, 0.78]",
        fontfamily=family,
        fontsize=9.4,
        color="#333333",
    )
    ax.text(
        0.72,
        0.58,
        r"$\Delta = y_{t+1} - y_t$",
        fontfamily=family,
        fontsize=13,
        color="#222222",
    )

    ax.plot([0.34, 0.94], [0.13, 0.13], color="#D4D4D4", linewidth=0.8)


def draw_mini_axis(ax):
    x = np.arange(1, 6)
    y = np.array([0.61, 0.64, 0.69, 0.73, 0.76])

    setup_axis(ax)
    ax.plot(x, y, color=NPG_HEX[3], marker="o", markersize=4.8, linewidth=1.6)
    ax.set_xlim(0.8, 5.2)
    ax.set_ylim(0.55, 0.80)
    ax.set_yticks(np.arange(0.55, 0.801, 0.05))
    ax.set_xticks(x)
    ax.set_xlabel("Block", fontfamily="Arial", fontsize=10)
    ax.set_ylabel("AUC", fontfamily="Arial", fontsize=10)
    ax.set_title("Arial in axes and ticks", fontfamily="Arial", fontweight="bold", fontsize=12, pad=8)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontfamily("Arial")


def main():
    plt.rcParams.update(
        {
            "font.family": "Arial",
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
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    fig = plt.figure(figsize=(11.2, 8.2), constrained_layout=True)
    top_fig, bottom_fig = fig.subfigures(2, 1, height_ratios=[1.20, 2.35])

    type_axes = top_fig.subplots(1, 2)
    draw_type_comparison(
        type_axes[0],
        "Sans-serif inside figures",
        "Arial",
        "Clean shapes for small labels, ticks, legends.",
    )
    draw_type_comparison(
        type_axes[1],
        "Serif inside figures",
        "Times New Roman",
        "More decorative strokes; often denser at small sizes.",
    )

    subfigs = bottom_fig.subfigures(1, 2, width_ratios=[2.6, 1.0])
    row_axes = subfigs[0].subplots(4, 1)
    mini_ax = subfigs[1].subplots(1, 1)

    for ax, (font_name, note) in zip(row_axes, FONT_CANDIDATES):
        draw_row(ax, font_name, note)

    draw_mini_axis(mini_ax)
    fig.suptitle("Font choices for research figures", fontsize=15, fontweight="bold", fontfamily="Arial")
    fig.savefig("fonts/fig/font_comparison.png", dpi=220, bbox_inches="tight")
    fig.savefig("fonts/fig/font_comparison.svg", bbox_inches="tight")


if __name__ == "__main__":
    main()
