import argparse
import pandas as pd


def read_csv_to_df(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    return df


def write_df_to_csv(file_name: str, df: pd.DataFrame):
    with open(file_name, "w") as f:
        # Set index=False to drop the index column
        f.write(df.to_csv(index=False))


def mangle_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Out of the dataframe, I need to:
    - Pick only treadmill running since 2022-01-23 (since that's when I started
      keeping the 5k @ 6:00 pace)
    - For easier visualization in Numbers, sort by date ascending
    - Only pick columns for date and heart rate data
    """
    filtered_rows_df = df[
        (df["Activity Type"] == "Treadmill Running") & (df["Date"] >= "2022-01-23")
    ]
    sorted_rows_df = filtered_rows_df.sort_values(by=["Date"], ascending=True)
    filtered_columns_df = sorted_rows_df[["Date", "Avg HR", "Max HR"]]
    return filtered_columns_df


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path to input file", required=True)
    parser.add_argument(
        "-o", "--output", help="path to output file", default="output/Output.csv"
    )
    args = parser.parse_args()
    return args


def main() -> int:
    args = parse_args()
    df = read_csv_to_df(args.input)
    mangled_df = mangle_df(df)
    print(mangled_df)  # Just handy for instantly seeing the output
    write_df_to_csv(args.output, mangled_df)


"""
TODO:
- Look into pandas and how to chain df operations more nicely
- Row/column filtering by command line args
"""

if __name__ == "__main__":
    main()
