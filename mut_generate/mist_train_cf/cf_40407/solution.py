"""
QUESTION:
Derive time intervals from a given DataFrame containing latitude, longitude, and timestamp information. Implement a method `_DeriveTimeIntervals(json_df)` that takes a Pandas DataFrame `json_df` with columns `latitudeE7`, `longitudeE7`, and `timestampMs` as input. The method should calculate the time differences between consecutive timestamps in milliseconds, convert these differences to seconds, and return a new DataFrame with an additional column `timeIntervalSec` containing the time intervals. The input DataFrame should be sorted by the `timestampMs` column before calculating the time intervals.
"""

def derive_time_intervals(json_df):
    # Sort the DataFrame based on timestampMs to ensure consecutive timestamps
    json_df = json_df.sort_values(by='timestampMs')

    # Calculate time differences between consecutive timestamps in milliseconds
    time_diff_ms = json_df['timestampMs'].diff()

    # Convert time differences to seconds and create a new column in the DataFrame
    json_df['timeIntervalSec'] = time_diff_ms / 1000

    return json_df