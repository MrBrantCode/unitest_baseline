"""
QUESTION:
Develop a function named `analyze_unique_elements` that takes two unsorted arrays of integers as input. The function should return the unique elements from the combined array, their count, the mean of the unique elements, and their standard deviation. The function should also handle potential exceptions.
"""

import numpy as np

def analyze_unique_elements(arr1, arr2):
    try:
        # Create a unique list of elements from both arrays
        unique_elems = list(set(arr1 + arr2))
        count_unique = len(unique_elems)
        mean_unique = np.mean(unique_elems)
        std_dev_unique = np.std(unique_elems)
        return unique_elems, count_unique, mean_unique, std_dev_unique
    except Exception as e:
        print(f"An error occurred: {e}")