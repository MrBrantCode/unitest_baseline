"""
QUESTION:
Create a function named "DetectOutliers" that takes as input a one-dimensional dataset of numbers and returns a list of outliers in the dataset. The outliers are defined as data points that fall below Q1 - 1.5*IQR or above Q3 + 1.5*IQR, where Q1 is the 25th percentile, Q3 is the 75th percentile, and IQR is the interquartile range of the dataset.
"""

import numpy as np

def DetectOutliers(dataset):
    Q1 = np.percentile(dataset, 25)
    Q3 = np.percentile(dataset, 75)
    IQR = Q3 - Q1
    multiplier = 1.5
    lower_boundary = Q1 - multiplier * IQR
    upper_boundary = Q3 + multiplier * IQR
    outliers = [data_point for data_point in dataset if data_point < lower_boundary or data_point > upper_boundary]
    return outliers