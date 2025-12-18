"""
QUESTION:
Calculate the mean and standard deviation of a given list of numbers and create a frequency distribution table. 

Function name: The solution should be implemented in a Python function.

Input: A list of numbers.

Output: 
- The mean of the input list in decimal form with two decimal places.
- The standard deviation of the input list in decimal form with two decimal places.
- A frequency distribution table showing each unique value in the list and its frequency.

Restrictions: Use Python's numpy library for mean and standard deviation calculations, and use a dictionary to store the frequency distribution.
"""

import numpy as np
from collections import Counter

def entrance(data):
    """
    Calculate the mean and standard deviation of a given list of numbers and create a frequency distribution table.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: A tuple containing the mean, standard deviation, and frequency distribution of the input list.
    """
    # Calculate the mean
    mean = np.mean(data)

    # Calculate the standard deviation
    std_dev = np.std(data)

    # Calculate the frequency distribution
    freq_dist = dict(Counter(data))

    # Return the results
    return round(mean, 2), round(std_dev, 2), freq_dist