import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd


def main():
    # Data transcribed from the final table.
    # MAS is intentionally excluded.
    data = [
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
        {
            "method": "Ours",
            "avg_feature_drift": 0.32415755682889863,
            "avg_margin_ref": 2.303329788573839,
            "avg_margin_final": 3.283776129205498,
            "destructive_rate": 0.1688628599316740,
        },
    ]

    df = pd.DataFrame(data)
    df["net_margin_change"] = df["avg_margin_final"] - df["avg_margin_ref"]

    # Bubble size encodes destructive rate in the main plot.
    # The legend deliberately uses uniform marker size and only indicates colors.
    bubble_sizes = 2500 * df["destructive_rate"] + 120

    fig, ax = plt.subplots(figsize=(13, 8))

    default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    colors = default_colors[: len(df)]

    for i, row in df.iterrows():
        ax.scatter(
            row["avg_feature_drift"],
            row["net_margin_change"],
            s=bubble_sizes.iloc[i],
            alpha=0.7,
            color=colors[i],
            edgecolors="black",
            linewidths=0.8,
        )

    # Reference line: positive values indicate adaptive functional evolution.
    ax.axhline(0, linestyle="--", linewidth=1)

    ax.set_xlabel("Average Feature Drift")
    ax.set_ylabel("Net Margin Change (avg_margin_final - avg_margin_ref)")

    # Uniform-size legend: color only, not destructive-rate size.
    legend_handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            label=df.iloc[i]["method"],
            markerfacecolor=colors[i],
            markeredgecolor="black",
            markersize=12,
            linewidth=0,
        )
        for i in range(len(df))
    ]

    ax.legend(
        handles=legend_handles,
        title="Method",
        bbox_to_anchor=(1.02, 1.0),
        loc="upper left",
        borderaxespad=0.0,
        frameon=True,
    )

    plt.tight_layout()

    out_path = "functional_evolution_map.png"
    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {out_path}")


if __name__ == "__main__":
    main()
