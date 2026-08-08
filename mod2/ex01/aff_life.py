import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def aff_life(df: pd.DataFrame):
    """
    Plots the life expectancy projection for Portugal over time.

    Args:
        df (pd.DataFrame): DataFrame containing life expectancy
        data indexed by country.
    """
    country_data = df.loc["Portugal"]

    index = country_data.index
    values = country_data.values

    plt.plot(index, values)

    plt.title("Portugal Life expectancy Projections")

    plt.xlabel("Year")

    plt.ylabel("Life expectancy")

    # plt.show()
    plt.xticks(country_data.index[::40])
    plt.savefig("plot_result")


def main():
    """Main function to test loading a dataset."""
    df = load("life_expectancy_years.csv")

    aff_life(df)


if __name__ == "__main__":
    main()
