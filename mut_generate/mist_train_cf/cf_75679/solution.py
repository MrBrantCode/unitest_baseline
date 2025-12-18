"""
QUESTION:
Create a function named `convert_string_data` that takes a 2D list of string data as input, where the first column contains categorical string data and the other columns contain numerical string data. The function should convert the categorical string data into numerical values and the numerical string data into float values, then return the converted data as a 2D numpy array.
"""

import pandas as pd
import numpy as np

def convert_string_data(X):
    df = pd.DataFrame(X)
    df.iloc[:, 0] = df.iloc[:, 0].astype('category').cat.codes
    return df.values.astype(float)