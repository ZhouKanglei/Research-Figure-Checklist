import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


STYLE = {
    "grid": "#E3E7EC",
    "face": "#F8FAFC",
    "spine": "#000000",
}


PALETTES = {
    "Matplotlib": [
        "#1F77B4",
        "#FF7F0E",
        "#2CA02C",
        "#D62728",
        "#9467BD",
        "#8C564B",
        "#E377C2",
        "#7F7F7F",
        "#BCBD22",
        "#17BECF",
    ],
    "NPG": [
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
    ],
    "Science": [
        "#3B4992",
        "#EE0000",
        "#008B45",
        "#631879",
        "#008280",
        "#BB0021",
        "#5F559B",
        "#A20056",
        "#808180",
        "#1B1919",
    ],
    "Lancet": [
        "#00468B",
        "#ED0000",
        "#42B540",
        "#0099B4",
        "#925E9F",
        "#FDAF91",
        "#AD002A",
        "#ADB6B6",
        "#1B1919",
    ],
}


def setup_axis(ax):
    ax.set_facecolor(STYLE["face"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(STYLE["spine"])
    ax.spines["bottom"].set_color(STYLE["spine"])
    ax.spines["left"].set_linewidth(0.75)
    ax.spines["bottom"].set_linewidth(0.75)
    ax.tick_params(colors="#2A2A2A", labelsize=7, length=5.5, width=0.75, direction="out")
    ax.grid(axis="y", color=STYLE["grid"], linewidth=0.65)
    ax.set_axisbelow(True)


def draw_swatches(ax, colors):
    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, 1)
    for idx, color in enumerate(colors):
        ax.add_patch(
            plt.Rectangle(
                (idx, 0), 1, 1, facecolor=color, edgecolor="white", linewidth=1
            )
        )
        ax.text(
            idx + 0.5,
            -0.10,
            str(idx + 1),
            ha="center",
            va="top",
            color="#4A4A4A",
        )
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)


def draw_grouped_bars(ax, colors):
    setup_axis(ax)
    x = np.arange(3)
    width = 0.2
    values = np.array(
        [
            [0.68, 0.74, 0.78],
            [0.62, 0.70, 0.73],
            [0.71, 0.77, 0.82],
        ]
    )
    for idx in range(3):
        bars = ax.bar(
            x + (idx - 1) * width,
            values[idx],
            width=width,
            color=colors[idx],
            alpha=0.50,
            edgecolor="black",
            linewidth=0.8,
        )
        for bar in bars:
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height + 0.012,
                f"{height:.2f}",
                ha="center",
                va="bottom",
                fontsize=5.8,
                color="#222222",
                rotation=90,
            )
    ax.set_xticks(x)
    ax.set_xticklabels(["D1", "D2", "D3"])
    ax.set_ylim(0.50, 0.90)
    ax.set_yticks(np.arange(0.50, 0.91, 0.10))
    ax.set_ylabel("Score", labelpad=2)
    ax.set_title("Grouped bars", fontsize=8, pad=6, fontweight="bold")


def draw_lines(ax, colors):
    setup_axis(ax)
    x = np.arange(1, 6)
    series = np.array(
        [
            [0.61, 0.64, 0.69, 0.73, 0.76],
            [0.66, 0.67, 0.70, 0.72, 0.74],
            [0.58, 0.63, 0.67, 0.71, 0.75],
        ]
    )
    for idx, y in enumerate(series):
        ax.plot(
            x,
            y,
            color=colors[idx],
            marker="o",
            markersize=5.6,
            markeredgecolor="white",
            markeredgewidth=0.45,
            linewidth=1.35,
        )
    ax.set_xticks(x)
    ax.set_ylim(0.55, 0.80)
    ax.set_yticks(np.arange(0.55, 0.801, 0.05))
    ax.set_ylabel("AUC", labelpad=2)
    ax.set_title("Trend lines", fontsize=8, pad=6, fontweight="bold")


def draw_scatter_heat(ax, colors, seed):
    ax.set_facecolor(STYLE["face"])
    rng = np.random.default_rng(seed)
    for idx, center in enumerate([(-0.8, 0.4), (0.2, 0.9), (0.7, -0.1)]):
        points = rng.normal(loc=center, scale=(0.22, 0.18), size=(32, 2))
        ax.scatter(
            points[:, 0],
            points[:, 1],
            s=20,
            color=colors[idx],
            alpha=0.58,
            edgecolor="white",
            linewidth=0.35,
        )
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1.45, 1.35)
    ax.set_ylim(-0.65, 1.45)
    ax.set_title("Sample clusters", fontsize=8, pad=6, fontweight="bold")
    for spine in ax.spines.values():
        spine.set_color(STYLE["spine"])
        spine.set_linewidth(0.75)


def draw_heatmap(ax, colors):
    ax.set_facecolor(STYLE["face"])
    data = np.array(
        [
            [0.88, 0.12, 0.05, 0.02],
            [0.18, 0.74, 0.14, 0.06],
            [0.08, 0.18, 0.69, 0.17],
            [0.04, 0.07, 0.21, 0.81],
        ]
    )
    cmap = LinearSegmentedColormap.from_list(
        "panel_map", ["#F7F7F7", colors[1], colors[0]]
    )
    ax.imshow(data, cmap=cmap, vmin=0, vmax=1)
    ax.set_xticks(range(4))
    ax.set_yticks(range(4))
    ax.set_xticklabels(["A", "B", "C", "D"], fontsize=6)
    ax.set_yticklabels(["A", "B", "C", "D"], fontsize=6)
    ax.tick_params(length=5.5, width=0.75, direction="out")
    for row in range(data.shape[0]):
        for col in range(data.shape[1]):
            color = "white" if data[row, col] >= 0.62 else "#222222"
            ax.text(
                col,
                row,
                f"{data[row, col]:.2f}",
                ha="center",
                va="center",
                fontsize=5.8,
                color=color,
            )
    ax.set_title("Heatmap", fontsize=8, pad=6, fontweight="bold")
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color(STYLE["spine"])
        spine.set_linewidth(0.75)


def main():
    plt.rcParams.update(
        {
            "font.family": "Arial",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
            "axes.titlesize": 8,
            "axes.labelsize": 7,
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

    fig, axes = plt.subplots(
        nrows=4,
        ncols=5,
        figsize=(10.8, 7.1),
        gridspec_kw={"width_ratios": [1.35, 1.06, 1.0, 1.0, 0.9]},
        constrained_layout=True,
    )

    for row, (name, colors) in enumerate(PALETTES.items()):
        axes[row, 0].set_ylabel(
            name, rotation=0, ha="right", va="center", fontsize=10, fontweight="bold"
        )
        axes[row, 0].yaxis.set_label_coords(-0.08, 0.5)
        draw_swatches(axes[row, 0], colors)
        draw_grouped_bars(axes[row, 1], colors)
        draw_lines(axes[row, 2], colors)
        draw_scatter_heat(axes[row, 3], colors, seed=2026 + row)
        draw_heatmap(axes[row, 4], colors)

    fig.suptitle(
        "Palette behavior across common research-figure panels",
        fontsize=12,
        fontweight="bold",
    )
    fig.savefig("palettes/fig/palette_panel_examples.png", dpi=220, bbox_inches="tight")
    fig.savefig("palettes/fig/palette_panel_examples.svg", bbox_inches="tight")


if __name__ == "__main__":
    main()
