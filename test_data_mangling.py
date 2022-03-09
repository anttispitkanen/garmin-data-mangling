"""Tests for the data mangling functions."""
import pandas as pd

from data_mangling import treadmill_runs_5k


def test_treadmill_runs_5k_filters_out_other_activity_types():
    """Test that treadmill_runs_5k() filters out other activity types."""
    data_frame = pd.DataFrame(
        {
            "Activity Type": ["Treadmill Running", "Running", "Strength Training"],
            "Date": ["2022-02-01", "2022-02-24", "2022-02-25"],
            "Avg HR": [100, 200, 300],
            "Max HR": [200, 300, 400],
        }
    )
    expected_data_frame = pd.DataFrame(
        {
            "Date": ["2022-02-01"],
            "Avg HR": [100],
            "Max HR": [200],
        }
    )
    pd.testing.assert_frame_equal(
        treadmill_runs_5k(data_frame).reset_index(drop=True),
        expected_data_frame.reset_index(drop=True),
    )


def test_treadmill_runs_5k_filters_out_dates_before_cutoff():
    """Test that treadmill_runs_5k() filters out dates before the cutoff."""
    data_frame = pd.DataFrame(
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
    expected_data_frame = pd.DataFrame(
        {
            "Date": ["2022-01-23", "2022-01-24"],
            "Avg HR": [300, 400],
            "Max HR": [400, 500],
        }
    )
    pd.testing.assert_frame_equal(
        treadmill_runs_5k(data_frame).reset_index(drop=True),
        expected_data_frame.reset_index(drop=True),
    )


def test_treadmill_runs_5k_sorts_by_date_ascending():
    """Test that treadmill_runs_5k() sorts by date ascending."""
    data_frame = pd.DataFrame(
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
    expected_data_frame = pd.DataFrame(
        {
            "Date": ["2022-01-23", "2022-01-24"],
            "Avg HR": [300, 400],
            "Max HR": [400, 500],
        }
    )
    pd.testing.assert_frame_equal(
        treadmill_runs_5k(data_frame).reset_index(drop=True),
        expected_data_frame.reset_index(drop=True),
    )
