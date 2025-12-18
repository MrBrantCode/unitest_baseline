"""
QUESTION:
Design a function `load_and_clean_csv` that takes a filename and an optional default value, loads the CSV file into a numpy array, handles missing data by converting non-numeric values to NaN and filling them with the default value, and returns the cleaned array. Additionally, create a function that computes the absolute magnitude of the deviation between two matrices using numpy's `abs` and subtraction functions. The matrices should be loaded from two separate CSV files and the function should handle cases where the matrices have different dimensions or contain non-numeric data.
"""

import pandas as pd
import numpy as np

def load_and_clean_csv(filename, default_value=0):
    df = pd.read_csv(filename, header=None)
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.fillna(default_value)
    return df.values