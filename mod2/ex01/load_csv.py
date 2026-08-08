import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV dataset, sets 'country' as index if present,

    prints its dimensions, and returns the DataFrame.
    """
    try:
        df = pd.read_csv(path)
        if "country" in df.columns:
            df = df.set_index("country")

        dimensions = df.shape

        print(f"Loading dataset of dimensions {dimensions}")

        return df

    except Exception as msg:
        print(f"Error: {msg}")
    return None


def main():
    """Main function to test loading a dataset."""
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
