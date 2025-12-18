"""
QUESTION:
Write a function called `calculate_correlation` that calculates the correlation between different Credit Default Swap (CDS) spreads. The function should take two lists of CDS spread values as input and return their correlation coefficient, which is a number between -1 and 1 that measures the strength and direction of the linear relationship between the two CDS spreads.
"""

import numpy as np

def calculate_correlation(list1, list2):
    """
    Calculate the correlation coefficient between two lists of CDS spread values.

    Parameters:
    list1 (list): The first list of CDS spread values.
    list2 (list): The second list of CDS spread values.

    Returns:
    float: The correlation coefficient, which is a number between -1 and 1.
    """
    return np.corrcoef(list1, list2)[0, 1]