"""
QUESTION:
Write a PostgreSQL query to calculate the median duration of inactive periods for each user in a table named `user_activity` with fields `user_id`, `activity_start`, and `activity_end`, considering only non-zero inactive periods, and handling outliers.
"""

import numpy as np
import pandas as pd

def calculate_median_inactive_periods(df):
    df['inactive_period'] = df['activity_start'] - df.groupby('user_id')['activity_end'].shift(1)
    df = df[df['inactive_period'] > pd.Timedelta(0)]
    return df.groupby('user_id')['inactive_period'].median().reset_index()