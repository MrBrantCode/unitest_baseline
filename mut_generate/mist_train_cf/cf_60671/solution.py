"""
QUESTION:
Create a function called `sanitize_dataset` that takes a pandas DataFrame as input. The function should iterate through each column in the DataFrame, and for each element, it should attempt to convert the value to a floating-point number. If the conversion is successful, the value should be replaced with the float; otherwise, the value should be replaced with Not Applicable (N/A), represented as `numpy.nan`.
"""

import pandas as pd
import numpy as np

def sanitize_dataset(df):
    """Sanitizes a pandas DataFrame by converting non-numeric strings to np.nan."""
    for col in df.columns:
        df[col] = df[col].apply(lambda x: float(x) if isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.', '', 1).replace('-', '', 1).isdigit()) else np.nan)
    return df