"""
QUESTION:
Create a function named `least_common` that takes a list of integers as input and returns a list of the least common numbers in ascending order. The input list should be generated randomly with a length between 50 and 100, and its elements should be random integers between 1 and 50. The function should handle any errors or exceptions and include appropriate comments and documentation. The function should return all least common numbers if there are multiple.
"""

import random
from collections import Counter

def least_common(lst):
    """
    This function finds the least common numbers in a given list and returns them in ascending order.

    Parameters:
    lst (list): A list of integers.

    Returns:
    list: A list of the least common numbers in ascending order.
    """

    # Count the frequency of each number in the list
    frequency_dict = Counter(lst)

    # Find the minimum frequency
    least_freq = min(frequency_dict.values())

    # Create a list of numbers with the least frequency and sort it in ascending order
    least_freq_list = sorted([num for num, freq in frequency_dict.items() if freq == least_freq])

    return least_freq_list