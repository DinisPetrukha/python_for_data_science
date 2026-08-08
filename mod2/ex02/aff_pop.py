import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def clean_pop(val):
    """Converts population string formatted values
    (e.g., '29M', '10k') to numeric float."""
    if isinstance(val, str):
        if val.endswith('M'):
            return float(val[:-1]) * 1_000_000
        elif val.endswith('k'):
            return float(val[:-1]) * 1_000
        elif val.endswith('B'):
            return float(val[:-1]) * 1_000_000_000
    return float(val)


def add_pop(df: pd.DataFrame) -> None:
    """
    Plots and compares population trends from 1800 to 2050 for
    France and Belgium.

    Args:
        df (pd.DataFrame): DataFrame containing population data
        indexed by country.
    """
    df_subset = df.loc[:, "1800":"2050"]

    campus_data = df_subset.loc["France"].apply(clean_pop)
    other_data = df_subset.loc["Portugal"].apply(clean_pop)

    plt.plot(campus_data.index, campus_data.values, label="France")

    plt.plot(other_data.index, other_data.values, label="Portugal")

    plt.legend()

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.legend(loc="lower right")
    plt.xticks(campus_data.index[::40])

    positions = [20_000_000, 40_000_000, 60_000_000]
    labels = ["20M", "40M", "60M"]
    plt.yticks(positions, labels)

    # 6. Save graph to file
    plt.savefig("pop_comparison.png")


def main():
    """Main function to test loading a dataset."""
    df = load("population_total.csv")
    add_pop(df)


if __name__ == "__main__":
    main()
