import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def projection_life(df_income: pd.DataFrame, df_life: pd.DataFrame) -> None:
    """
    Plots a scatter plot of Life Expectancy
    vs GDP per Capita for the year 1900.

    Args:
        df_income (pd.DataFrame): DataFrame
        with income data indexed by country.
        df_life (pd.DataFrame): DataFrame with
        life expectancy data indexed by country.
    """
    income_1900 = df_income["1900"]
    life_1900 = df_life["1900"]

    plt.scatter(income_1900, life_1900)

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    # Apply a logarithmic scale
    plt.xscale("log")

    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

    plt.savefig("projection_1900.png")


def main():
    """Main function to test loading a dataset."""
    df_income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    df_life = load("life_expectancy_years.csv")

    if df_income is not None and df_life is not None:
        projection_life(df_income, df_life)


if __name__ == "__main__":
    main()
