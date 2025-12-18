"""
QUESTION:
Create a function called `identify_outliers` that takes a 1D NumPy array `data` as input and returns the number of outliers in the dataset. An outlier is defined as any data point that lies below Q1 - 1.5*IQR or above Q3 + 1.5*IQR, where Q1 and Q3 are the first and third quartiles, respectively, and IQR = Q3 - Q1.
"""

import numpy as np

def identify_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    outliers = data[(data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR)]
    return len(outliers)