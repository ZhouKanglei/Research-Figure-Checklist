import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe
import pandas as pd
import numpy as np


def main():
    # Data transcribed from the final table.
    # MAS is intentionally excluded.
    data = [
        {
            "method": "Ours",
            "avg_feature_drift": 0.32415755682889863,
            "avg_margin_ref": 2.303329788573839,
            "avg_margin_final": 3.283776129205498,
            "destructive_rate": 0.1688628599316740,
        },
        {
            "method": "AVQACL",
            "avg_feature_drift": 0.27836013607092713,
            "avg_margin_ref": 0.4645931464385512,
            "avg_margin_final": 0.21778688836794155,
            "destructive_rate": 0.3766314481044127,
        },
        {
            "method": "AV-CIL",
            "avg_feature_drift": 0.5294737306761582,
            "avg_margin_ref": 1.9804624054904505,
            "avg_margin_final": 2.023047881030824,
            "destructive_rate": 0.27616926503340755,
        },
        {
            "method": "iCaRL",
            "avg_feature_drift": 0.5585190691763446,
            "avg_margin_ref": 1.9962249738829476,
            "avg_margin_final": 1.428691119097528,
            "destructive_rate": 0.2755952380952381,
        },
        {
            "method": "SS-IL",
            "avg_feature_drift": 0.39733996899997226,
            "avg_margin_ref": 0.8691858061592576,
            "avg_margin_final": 0.22446426738747957,
            "destructive_rate": 0.43552168815943726,
        },
        {
            "method": "VQACL",
            "avg_feature_drift": 0.5803836141638503,
            "avg_margin_ref": 1.7693628525821925,
            "avg_margin_final": 1.6169217415841304,
            "destructive_rate": 0.28413284132841327,
        },
        {
            "method": "MAFED",
            "avg_feature_drift": 0.4640910673612324,
            "avg_margin_ref": 0.7544363071503288,
            "avg_margin_final": -1.061379758,
            "destructive_rate": 0.7055655296229802,
        },
        {
            "method": "LwF",
            "avg_feature_drift": 0.7356397611582839,
            "avg_margin_ref": 0.7678370619780265,
            "avg_margin_final": -0.899449834,
            "destructive_rate": 0.6642953020134230,
        },
        {
            "method": "EWC",
            "avg_feature_drift": 0.3706450486842470,
            "avg_margin_ref": 1.4758859977950252,
            "avg_margin_final": 0.0017950743303170654,
            "destructive_rate": 0.5059790732436472,
        },
        {
            "method": "Vanilla",
            "avg_feature_drift": 0.9312146237042173,
            "avg_margin_ref": 3.0192138757736355,
            "avg_margin_final": -2.280989451,
            "destructive_rate": 0.7277599142550911,
        },
    ]

    df = pd.DataFrame(data)
    df["net_margin_change"] = df["avg_margin_final"] - df["avg_margin_ref"]

    plt.rcParams.update(
        {
            "font.family": "Arial",
            "font.sans-serif": ["Arial"],
            "figure.facecolor": "white",
            "axes.facecolor": "#fbfbf8",
            "axes.edgecolor": "#222222",
            "axes.labelcolor": "#222222",
            "axes.titlecolor": "#111111",
            "font.size": 14,
            "axes.labelsize": 14,
            "axes.titlesize": 14,
            "xtick.color": "#333333",
            "ytick.color": "#333333",
            "legend.fontsize": 14,
            "legend.title_fontsize": 14,
            "savefig.facecolor": "white",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    # Bubble size encodes destructive rate in the main plot.
    bubble_sizes = 3200 * df["destructive_rate"] + 180

    fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)

    NPG_HEX = [
        "#00A087",  # 绿色
        "#8491B4",  # 灰紫蓝色
        "#91D1C2",  # 薄荷绿色
        "#F39B7F",  # 鲑红色
        "#3C5488",  # 深蓝色
        "#4DBBD5",  # 青蓝色
        "#7E6148",  # 棕色
        "#E64B35",  # 朱红色
        "#B09C85",  # 灰褐色
        "#DC0000",  # 强红色
    ]
    color_map = {
        row["method"]: NPG_HEX[i] for i, row in df.reset_index(drop=True).iterrows()
    }

    ax.axhspan(
        0, df["net_margin_change"].max() + 2.55, color="#eaf4ef", alpha=0.75, zorder=0
    )
    ax.axhspan(
        df["net_margin_change"].min() - 2.55, 0, color="#f8eeee", alpha=0.8, zorder=0
    )
    ax.axhline(0, linestyle=(0, (6, 4)), color="#4a4a4a", linewidth=1.15, zorder=1)
    ax.axvline(
        df["avg_feature_drift"].median(),
        linestyle=":",
        color="#7a7a7a",
        linewidth=1.0,
        zorder=1,
    )

    for i, row in df.iterrows():
        color = color_map[row["method"]]
        ax.scatter(
            row["avg_feature_drift"],
            row["net_margin_change"],
            s=bubble_sizes.iloc[i],
            alpha=0.82,
            color=color,
            edgecolors="#1a1a1a",
            linewidths=1.0,
            zorder=3,
        )

    label_positions = {
        "Ours": (0.360, 1.02, "left"),
        "AVQACL": (0.250, -1.6, "left"),
        "AV-CIL": (0.548, 1.28, "left"),
        "iCaRL": (0.575, -1.68, "left"),
        "SS-IL": (0.35, -0.60, "right"),
        "VQACL": (0.620, 0.54, "left"),
        "MAFED": (0.45, -3.18, "right"),
        "LwF": (0.750, -2.88, "left"),
        "EWC": (0.358, -2.78, "right"),
        "Vanilla": (0.875, -5.34, "right"),
    }
    for _, row in df.iterrows():
        label_x, label_y, ha = label_positions[row["method"]]
        bubble_radius_points = (bubble_sizes.loc[row.name] / 3.141592653589793) ** 0.5
        label = ax.annotate(
            row["method"],
            xy=(row["avg_feature_drift"], row["net_margin_change"]),
            xytext=(label_x, label_y),
            textcoords="data",
            ha=ha,
            va="center",
            color="#1f1f1f",
            # fontsize=10.5,
            fontweight="semibold" if row["method"] == "Ours" else "normal",
            arrowprops={
                "arrowstyle": "-",
                "color": "#575757",
                "lw": 0.8,
                "alpha": 0.72,
                "shrinkA": 4,
                "shrinkB": bubble_radius_points + 2,
            },
            zorder=4,
        )
        label.set_path_effects(
            [pe.withStroke(linewidth=3.2, foreground="white", alpha=0.9)]
        )

    ax.scatter(
        df["avg_feature_drift"],
        df["net_margin_change"],
        s=16,
        color="white",
        edgecolors="none",
        linewidths=0.45,
        zorder=5,
    )

    # ax.set_title("Functional Evolution Map", pad=24, weight="bold", fontsize=18)
    # ax.text(
    #     0.5,
    #     1.025,
    #     "Net margin change = final margin - reference margin; bubble size = destructive rate",
    #     transform=ax.transAxes,
    #     ha="center",
    #     va="bottom",
    #     fontsize=10.5,
    #     color="#444444",
    # )
    ax.set_xlabel("Average Feature Drift")
    ax.set_ylabel("Net Margin Change")
    ax.text(
        0.02,
        0.98,
        "Adaptive evolution",
        transform=ax.transAxes,
        ha="left",
        va="top",
        color="#26734d",
        # fontsize=11,
        weight="semibold",
    )
    ax.text(
        0.02,
        0.02,
        "Destructive evolution",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        color="#a23b3b",
        # fontsize=11,
        weight="semibold",
    )
    ax.text(
        df["avg_feature_drift"].median() + 0.008,
        df["net_margin_change"].min() - 0.32,
        "Median drift",
        color="#696969",
        # fontsize=9.5,
        rotation=90,
        va="bottom",
    )

    x_left_padding = 0.035
    x_right_padding = 0.045
    y_bottom_padding = 0.32
    y_top_padding = 0.38
    ax.set_xlim(
        df["avg_feature_drift"].min() - x_left_padding,
        df["avg_feature_drift"].max() + x_right_padding,
    )
    ax.set_ylim(
        np.floor(df["net_margin_change"].min() - y_bottom_padding),
        np.ceil(df["net_margin_change"].max() + y_top_padding),
    )
    ax.grid(True, color="#d7d7d2", linewidth=0.8, alpha=0.72)
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", which="major", length=8, width=1.1, direction="out")
    ax.tick_params(axis="both", which="minor", length=8, width=1.1, direction="out")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(1.1)
    ax.spines["bottom"].set_linewidth(1.1)

    method_handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="none",
            label=method,
            markerfacecolor=color_map[method],
            markeredgecolor="#1a1a1a",
            markersize=9,
            linewidth=0,
        )
        for method in color_map
        if method in set(df["method"])
    ]
    # method_legend = ax.legend(
    #     handles=method_handles,
    #     title="Method",
    #     bbox_to_anchor=(0.985, 0.985),
    #     loc="upper right",
    #     borderaxespad=0.2,
    #     frameon=True,
    #     framealpha=0.96,
    #     edgecolor="#d0d0cc",
    #     labelspacing=0.55,
    #     handletextpad=0.7,
    # )
    # ax.add_artist(method_legend)

    size_values = [0.2, 0.45, 0.7]
    size_handles = [
        plt.scatter(
            [],
            [],
            s=3200 * value + 180,
            facecolors="#cfcfcf",
            edgecolors="#1a1a1a",
            linewidths=0.9,
            alpha=0.75,
            label=f"{value:.1f}",
        )
        for value in size_values
    ]
    size_legend = ax.legend(
        handles=size_handles,
        title="Destructive rate",
        bbox_to_anchor=(0.98, 1.02),
        loc="upper right",
        borderaxespad=0.4,
        frameon=False,
        framealpha=0.96,
        edgecolor="#d0d0cc",
        labelspacing=2.75,
        handletextpad=2.0,
        borderpad=0.9,
    )
    size_legend._legend_box.sep = 16

    out_path = "functional_evolution_map.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    out_path = "functional_evolution_map.pdf"
    plt.savefig(out_path)
    import os

    os.system(f"pdfcrop {out_path} {out_path}")
    plt.show()

    print(f"Saved to: {out_path}")


if __name__ == "__main__":
    main()
