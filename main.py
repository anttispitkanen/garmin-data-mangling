"""Main module."""
import argparse

import pandas as pd

from .data_mangling import mangle_data_frame


def read_csv_to_data_frame(file_name: str) -> pd.DataFrame:
    """Reads a CSV file into a Pandas DataFrame."""
    data_frame = pd.read_csv(file_name)
    return data_frame


def write_data_frame_to_csv(file_name: str, data_frame: pd.DataFrame):
    """Writes a Pandas DataFrame to a CSV file."""
    with open(file_name, "w", encoding="utf-8") as file:
        # Set index=False to drop the index column
        file.write(data_frame.to_csv(index=False))


def parse_args():
    """Parses the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path to input file", required=True)
    parser.add_argument(
        "-o", "--output", help="path to output file", default="output/Output.csv"
    )
    parser.add_argument("-O", "--operation", help="operation to perform", required=True)
    args = parser.parse_args()
    return args


def main() -> int:
    """Main function."""
    args = parse_args()
    data_frame = read_csv_to_data_frame(args.input)
    mangled_data_frame = mangle_data_frame(args.operation, data_frame)
    print(mangled_data_frame)  # Just handy for instantly seeing the output
    write_data_frame_to_csv(args.output, mangled_data_frame)


if __name__ == "__main__":
    main()
