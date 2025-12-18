"""
QUESTION:
Create a function `calculate_interquartile_range` that takes a list of three sorted numerical sequences as input and returns a list of their corresponding interquartile ranges. The input sequences should be lists of numbers, and the function should calculate the interquartile range for each sequence individually.
"""

import numpy as np

def calculate_interquartile_range(numeric_sequences):
    iqr_values = []
    for sequence in numeric_sequences:
        q1 = np.percentile(sequence, 25)
        q3 = np.percentile(sequence, 75)
        iqr = q3 - q1
        iqr_values.append(iqr)
    
    return iqr_values