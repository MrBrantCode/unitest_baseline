"""
QUESTION:
Write a function `detect_outliers` that takes a pandas DataFrame and a column name as input, detects outliers in that column using the interquartile range (IQR) method, and returns a DataFrame of the outlier rows. The IQR method considers data points to be outliers if they are below Q1 - 1.5*IQR or above Q3 + 1.5*IQR, where Q1 is the 25th percentile, Q3 is the 75th percentile, and IQR is the interquartile range.
"""

import numpy as np
import pandas as pd

def detect_outliers(df, col):
    q1 = np.percentile(df[col], 25)
    q3 = np.percentile(df[col], 75)
    iqr = q3 - q1
        
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound) ]
    
    return outliers