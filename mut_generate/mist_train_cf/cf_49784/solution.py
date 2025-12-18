"""
QUESTION:
Write a function `identify_outliers(matrix)` that takes a 2D matrix of quantitative data values as input. The function should identify and return the coordinate positions (row and column values) of any outliers in the data, where an outlier is defined as a value that is more than two standard deviations from the mean of its row or column. If there are multiple outliers, return all identifications in ascending order by their row and column values. If the data shows no identifiable outlier, return the string "The data presents an unbroken uniformity".
"""

import numpy as np

def identify_outliers(matrix):
    matrix = np.array(matrix)
    
    # Calculate mean and standard deviation for rows and columns
    row_means = np.mean(matrix, axis=1)
    row_stds = np.std(matrix, axis=1)
    col_means = np.mean(matrix, axis=0)
    col_stds = np.std(matrix, axis=0)

    # Check for outliers in rows and columns
    outliers = []
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            if (np.abs(matrix[row, column] - row_means[row]) > 2 * row_stds[row]) or (np.abs(matrix[row, column] - col_means[column]) > 2 * col_stds[column]):
                outliers.append((row, column))
                
    return sorted(outliers) or "The data presents an unbroken uniformity"