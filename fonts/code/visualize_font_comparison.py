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


def setup_axis(ax, fontfamily):
    ax.set_facecolor(STYLE["face"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(STYLE["spine"])
    ax.spines["bottom"].set_color(STYLE["spine"])
    ax.spines["left"].set_linewidth(0.75)
    ax.spines["bottom"].set_linewidth(0.75)
    ax.tick_params(labelsize=11, width=0.75, length=5.5, direction="out")
    ax.grid(axis="y", color=STYLE["grid"], linewidth=0.65)
    ax.set_axisbelow(True)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontfamily(fontfamily)


def draw_type_comparison(ax, title, font_name, description):
    actual_font = matched_font_name(font_name)
    family = actual_font if actual_font != "unknown" else font_name
    x = np.arange(3)
    values = np.array([0.68, 0.74, 0.82])

    setup_axis(ax, family)
    bars = ax.bar(x, values, width=0.42, color=NPG_HEX[:3], alpha=0.50, edgecolor="black", linewidth=0.8)
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.012,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=12,
            fontfamily=family,
            color="#222222",
        )

    ax.set_ylim(0.50, 0.90)
    ax.set_yticks(np.arange(0.50, 0.91, 0.10))
    ax.set_xticks(x)
    ax.set_xticklabels(["D1", "D2", "D3"], fontfamily=family, fontsize=12)
    for label in ax.get_yticklabels():
        label.set_fontfamily(family)
        label.set_fontsize(11)
    ax.set_ylabel("Score", fontfamily=family, fontsize=13)
    ax.set_title(title, fontfamily=family, fontweight="bold", fontsize=17, pad=10)
    ax.text(
        0.02,
        0.98,
        f"Requested: {font_name} \nMatched: {actual_font}",
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=12,
        fontfamily=family,
        color=STYLE["muted"],
    )
    ax.text(
        0.02,
        -0.20,
        description,
        transform=ax.transAxes,
        ha="left",
        va="top",
        fontsize=12,
        fontfamily=family,
        color=STYLE["muted"],
        clip_on=False,
    )

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

    fig, type_axes = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True)
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

    fig.suptitle("Sans-serif vs. serif fonts inside research figures", fontsize=18, fontweight="bold", fontfamily="Arial")
    fig.savefig("fonts/fig/font_comparison.png", dpi=220, bbox_inches="tight")


if __name__ == "__main__":
    main()
