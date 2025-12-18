"""
QUESTION:
Create a function `encode_date` to effectively incorporate date information into a regression model. The input date should be converted into a numerical feature that captures its relevant characteristics. Consider techniques such as creating separate features for day of the week, month, or quarter, cyclical encoding, or deriving features that capture the interval time. The function should be able to handle different types of date information and allow for experimentation with various approaches.
"""

import pandas as pd
import numpy as np

def encode_date(date_series):
    """
    This function encodes a pandas Series of dates into a DataFrame with cyclical features.
    
    Parameters:
    date_series (pandas Series): A pandas Series of datetime objects.
    
    Returns:
    pandas DataFrame: A DataFrame with cyclical features for day of the week, month, and quarter.
    """

    # Create a new DataFrame to store the encoded features
    encoded_features = pd.DataFrame(index=date_series.index)

    # Create cyclical features for day of the week
    encoded_features['day_of_week_sin'] = np.sin(2 * np.pi * date_series.dt.dayofweek / 7)
    encoded_features['day_of_week_cos'] = np.cos(2 * np.pi * date_series.dt.dayofweek / 7)

    # Create cyclical features for month
    encoded_features['month_sin'] = np.sin(2 * np.pi * date_series.dt.month / 12)
    encoded_features['month_cos'] = np.cos(2 * np.pi * date_series.dt.month / 12)

    # Create cyclical features for quarter
    encoded_features['quarter_sin'] = np.sin(2 * np.pi * ((date_series.dt.month - 1) // 3) / 4)
    encoded_features['quarter_cos'] = np.cos(2 * np.pi * ((date_series.dt.month - 1) // 3) / 4)

    return encoded_features