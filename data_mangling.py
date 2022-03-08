"""Data mangling functions"""
from enum import Enum

import pandas as pd


class Operation(Enum):
    """The supported operations enumerated."""

    TREADMILL_RUNS_5K = "treadmill_runs_5k"


def mangle_data_frame(operation: Operation, data_frame: pd.DataFrame) -> pd.DataFrame:
    """Delegates to the appropriate mangling function based on the operation."""
    match (operation):
        case "treadmill_runs_5k":
            return treadmill_runs_5k(data_frame)
        case _:
            raise ValueError(f"Unknown operation: {operation}")


def treadmill_runs_5k(data_frame: pd.DataFrame) -> pd.DataFrame:
    """
    Out of the dataframe, I need to:
    - Pick only treadmill running since 2022-01-23 (since that's when I started
      keeping the 5k @ 6:00 pace)
    - Only pick columns for date and heart rate data
    - For easier visualization in Numbers, sort by date ascending
    """
    return (
        data_frame.query("`Activity Type` == 'Treadmill Running'")
        .query("Date >= '2022-01-23'")
        .filter(["Date", "Avg HR", "Max HR"])
        .sort_values(by=["Date"], ascending=True)
    )
