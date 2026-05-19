#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import math
import os

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import to_rgba
from matplotlib.ticker import MaxNLocator

OUT_DIR = Path(__file__).resolve().parent / "output"

FIG1_DATASET_ORDER = ["ISRUC", "HMC"]
TB_ORDER = ["tb6", "tb8", "tb10"]
FIG1_METHOD_ORDER = ["head_only", "seq_lora", "ROSA"]
FIG1_METHOD_LABELS = {
    "head_only": "Head-Only",
    "seq_lora": "SeqLoRA",
    "ROSA": "ROSA",
}

COLORS = {
    "timeblock": "#E64B35",
    "random": "#4DBBD5",
    "grid": "#E3E7EC",
    "spine": "#000000",
}

# Extracted from data/fig1_temporal_partition_plot.csv (include_in_plot=1)
FIG1_ROWS = [
    {
        "dataset": "ISRUC",
        "tb": "tb6",
        "method": "head_only",
        "timeblock_mean": 0.1784597211974247,
        "random_mean": 0.6722809464098498,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb6",
        "method": "seq_lora",
        "timeblock_mean": 0.23984959527946858,
        "random_mean": 0.6829611552424091,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb6",
        "method": "ROSA",
        "timeblock_mean": 0.38206630473958403,
        "random_mean": 0.7343531276495138,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb8",
        "method": "head_only",
        "timeblock_mean": 0.3030385185185185,
        "random_mean": 0.6722809464098498,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb8",
        "method": "seq_lora",
        "timeblock_mean": 0.31016188873626374,
        "random_mean": 0.6702739828926905,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb8",
        "method": "ROSA",
        "timeblock_mean": 0.4579801648512608,
        "random_mean": 0.7764868123659725,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb10",
        "method": "head_only",
        "timeblock_mean": 0.28761151960784316,
        "random_mean": 0.6993613324775352,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb10",
        "method": "seq_lora",
        "timeblock_mean": 0.23118973802577767,
        "random_mean": 0.6614018753072017,
    },
    {
        "dataset": "ISRUC",
        "tb": "tb10",
        "method": "ROSA",
        "timeblock_mean": 0.38870963566014093,
        "random_mean": 0.7460178553756147,
    },
    {
        "dataset": "HMC",
        "tb": "tb6",
        "method": "head_only",
        "timeblock_mean": 0.3042865406427221,
        "random_mean": 0.6538559615003773,
    },
    {
        "dataset": "HMC",
        "tb": "tb6",
        "method": "seq_lora",
        "timeblock_mean": 0.3113465437218903,
        "random_mean": 0.6506425075543516,
    },
    {
        "dataset": "HMC",
        "tb": "tb6",
        "method": "ROSA",
        "timeblock_mean": 0.5193799660640719,
        "random_mean": 0.6834591854101526,
    },
    {
        "dataset": "HMC",
        "tb": "tb8",
        "method": "head_only",
        "timeblock_mean": 0.2997006383737518,
        "random_mean": 0.6209202516556326,
    },
    {
        "dataset": "HMC",
        "tb": "tb8",
        "method": "seq_lora",
        "timeblock_mean": 0.26159740432811296,
        "random_mean": 0.6477951681239036,
    },
    {
        "dataset": "HMC",
        "tb": "tb8",
        "method": "ROSA",
        "timeblock_mean": 0.3724271595900435,
        "random_mean": 0.6886923076923077,
    },
    {
        "dataset": "HMC",
        "tb": "tb10",
        "method": "head_only",
        "timeblock_mean": 0.17945850027367268,
        "random_mean": 0.5910252707581228,
    },
    {
        "dataset": "HMC",
        "tb": "tb10",
        "method": "seq_lora",
        "timeblock_mean": 0.24259135660782468,
        "random_mean": 0.6498745252211113,
    },
    {
        "dataset": "HMC",
        "tb": "tb10",
        "method": "ROSA",
        "timeblock_mean": 0.48004343854448287,
        "random_mean": 0.7159884455437532,
    },
]


def configure() -> None:
    plt.rcParams.update(
        {
            "font.family": "Arial",
            "mathtext.fontset": "cm",
            "font.size": 10.5,
            "axes.labelsize": 10.5,
            "axes.titlesize": 10.5,
            "xtick.labelsize": 10.5,
            "ytick.labelsize": 10.5,
            "legend.fontsize": 10.5,
            "xtick.direction": "out",
            "ytick.direction": "out",
            "xtick.major.size": 5.5,
            "ytick.major.size": 5.5,
            "xtick.major.width": 0.9,
            "ytick.major.width": 0.9,
            "axes.linewidth": 0.9,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def axis_limits(
    values: list[float], pad_frac: float = 0.06, min_pad: float = 0.03
) -> tuple[float, float]:
    vals = [float(v) for v in values if math.isfinite(v)]
    vmin, vmax = min(vals), max(vals)
    span = (vmax - vmin) if vmax > vmin else 1.0
    pad = max(min_pad, pad_frac * span)
    return (vmin - pad, vmax + pad)


def snap_ylim_to_tick(ax: plt.Axes, nbins: int = 5) -> None:
    ymin, ymax = ax.get_ylim()
    loc = MaxNLocator(nbins=nbins)
    ticks = [t for t in loc.tick_values(ymin, ymax) if t >= ymin - 1e-12]
    if not ticks:
        return
    ytop = ticks[-1]
    ax.set_ymargin(0.0)
    ax.set_ylim(ymin, ytop)
    ax.set_yticks([t for t in ticks if t <= ytop + 1e-12])


def plot_fig1() -> None:
    by_key = {(r["dataset"], r["tb"], r["method"]): r for r in FIG1_ROWS}
    all_vals = []
    for r in FIG1_ROWS:
        all_vals.extend([r["timeblock_mean"], r["random_mean"]])
    y_min, y_max = axis_limits(all_vals)

    fig = plt.figure(figsize=(8, 5.5), facecolor="white")
    gs = fig.add_gridspec(
        3,
        3,
        height_ratios=[0.1, 1.0, 1.0],
        left=0.055,
        right=0.992,
        top=0.94,
        bottom=0.11,
        wspace=0.1,
        hspace=0.12,
    )

    # top schematic (horizontal)
    ax0 = fig.add_subplot(gs[0, :])
    ax0.set_axis_off()
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, 1)

    y_line = 0.05
    xs_left = [0.12, 0.20, 0.28, 0.36, 0.44]
    xs_right = [0.65, 0.73, 0.81, 0.89, 0.97]
    labels_top = ["M1", "M2", "M3", "M4", "M5"]
    labels_bottom = ["R3", "R1", "R5", "R2", "R4"]

    ax0.text(
        -0.075,
        0.45,
        "Temporal stream:",
        # color=COLORS["timeblock"],
        ha="left",
        va="center",
        fontsize=10,
        weight="bold",
    )
    ax0.text(
        0.49,
        0.45,
        "Random split:",
        # color=COLORS["random"],
        ha="left",
        va="center",
        fontsize=10,
        weight="bold",
    )

    for i, x in enumerate(xs_left):
        rect = Rectangle(
            (x - 0.026, y_line - 0.032),
            0.05,
            0.9,
            facecolor=to_rgba(COLORS["timeblock"], 0.20),
            edgecolor="#000000",
            linewidth=1.0,
        )
        ax0.add_patch(rect)
        ax0.text(x, 0.45, labels_top[i], ha="center", va="center")
        if i < len(xs_left) - 1:
            ax0.annotate(
                "",
                xy=(xs_left[i + 1] - 0.02, 0.5),
                xytext=(x + 0.02, 0.5),
                arrowprops=dict(arrowstyle="->", color="#000000", lw=1.0),
            )

    for i, x in enumerate(xs_right):
        rect = Rectangle(
            (x - 0.026, y_line - 0.032),
            0.05,
            0.9,
            facecolor=to_rgba(COLORS["random"], 0.20),
            edgecolor="#000000",
            linewidth=1.0,
        )
        ax0.add_patch(rect)
        ax0.text(x, 0.45, labels_bottom[i], ha="center", va="center")
        if i < len(xs_right) - 1:
            ax0.annotate(
                "",
                xy=(xs_right[i + 1] - 0.02, 0.5),
                xytext=(x + 0.02, 0.5),
                arrowprops=dict(arrowstyle="->", color="#000000", lw=1.0),
            )

    ref_ax = None
    for r_i, dataset in enumerate(FIG1_DATASET_ORDER):
        for c_i, tb in enumerate(TB_ORDER):
            ax = (
                fig.add_subplot(gs[r_i + 1, c_i], sharex=ref_ax, sharey=ref_ax)
                if ref_ax
                else fig.add_subplot(gs[r_i + 1, c_i])
            )
            if ref_ax is None:
                ref_ax = ax

            if c_i == 0:
                ax.set_ylabel("Balanced Accuracy")
            ax.text(
                0.03,
                0.97,
                f"{dataset} · {tb}",
                transform=ax.transAxes,
                ha="left",
                va="top",
                weight="bold",
            )
            ax.patch.set_facecolor(f"C{r_i}")
            ax.patch.set_alpha(0.1)
            ax.grid("-.", axis="y", color=COLORS["grid"], linewidth=0.8, alpha=0.95)
            ax.set_axisbelow(True)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_color(COLORS["spine"])
            ax.spines["bottom"].set_color(COLORS["spine"])

            width = 0.34
            x_pos = list(range(len(FIG1_METHOD_ORDER)))
            for m_i, m in enumerate(FIG1_METHOD_ORDER):
                row = by_key.get((dataset, tb, m))
                if row is None:
                    continue
                t = float(row["timeblock_mean"])
                q = float(row["random_mean"])
                ax.bar(
                    m_i - width / 2,
                    t,
                    width=width,
                    color=to_rgba(COLORS["timeblock"], 0.38),
                    edgecolor="#000000",
                    linewidth=1.0,
                    zorder=3,
                )
                ax.bar(
                    m_i + width / 2,
                    q,
                    width=width,
                    color=to_rgba(COLORS["random"], 0.38),
                    edgecolor="#000000",
                    linewidth=1.0,
                    zorder=3,
                )
                ax.text(
                    m_i - width / 2,
                    t + 0.01,
                    f"{t:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=9,
                    color="#000000",
                )
                ax.text(
                    m_i + width / 2,
                    q + 0.01,
                    f"{q:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=9,
                    color="#000000",
                )

            ax.set_xticks(x_pos)
            ax.set_xticklabels([FIG1_METHOD_LABELS[m] for m in FIG1_METHOD_ORDER])
            ax.set_ylim(y_min, y_max)
            if r_i != len(FIG1_DATASET_ORDER) - 1:
                ax.tick_params(axis="x", labelbottom=False)
            if c_i != 0:
                ax.tick_params(axis="y", labelleft=False)
            snap_ylim_to_tick(ax)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "pdf"):
        fig.savefig(
            OUT_DIR / f"fig1_temporal_partition_standalone.{suffix}",
            dpi=300,
            bbox_inches="tight",
        )
    pdf_path = OUT_DIR / "fig1_temporal_partition_standalone.pdf"
    os.system(f"pdfcrop {pdf_path} {pdf_path}")
    plt.close(fig)
    print(f">>> Figure outputs saved to {OUT_DIR}")


if __name__ == "__main__":
    configure()
    plot_fig1()
