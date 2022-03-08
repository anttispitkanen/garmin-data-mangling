import pandas as pd
from main import mangle_df


def test_mangle_df_filters_out_other_activity_types():
    df = pd.DataFrame(
        {
            "Activity Type": ["Treadmill Running", "Running", "Strength Training"],
            "Date": ["2022-02-01", "2022-02-24", "2022-02-25"],
            "Avg HR": [100, 200, 300],
            "Max HR": [200, 300, 400],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Date": ["2022-02-01"],
            "Avg HR": [100],
            "Max HR": [200],
        }
    )
    pd.testing.assert_frame_equal(
        mangle_df(df).reset_index(drop=True), expected_df.reset_index(drop=True)
    )


def test_mangle_df_filters_out_dates_before_cutoff():
    df = pd.DataFrame(
        {
            "Activity Type": [
                "Treadmill Running",
                "Treadmill Running",
                "Treadmill Running",
                "Treadmill Running",
            ],
            "Date": ["2022-01-01", "2022-01-22", "2022-01-23", "2022-01-24"],
            "Avg HR": [100, 200, 300, 400],
            "Max HR": [200, 300, 400, 500],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Date": ["2022-01-23", "2022-01-24"],
            "Avg HR": [300, 400],
            "Max HR": [400, 500],
        }
    )
    pd.testing.assert_frame_equal(
        mangle_df(df).reset_index(drop=True),
        expected_df.reset_index(drop=True),
    )


def test_mangle_df_sorts_by_date_ascending():
    df = pd.DataFrame(
        {
            "Activity Type": [
                "Treadmill Running",
                "Treadmill Running",
            ],
            "Date": ["2022-01-24", "2022-01-23"],
            "Avg HR": [400, 300],
            "Max HR": [500, 400],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Date": ["2022-01-23", "2022-01-24"],
            "Avg HR": [300, 400],
            "Max HR": [400, 500],
        }
    )
    pd.testing.assert_frame_equal(
        mangle_df(df).reset_index(drop=True),
        expected_df.reset_index(drop=True),
    )
