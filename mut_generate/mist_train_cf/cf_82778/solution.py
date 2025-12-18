"""
QUESTION:
Create a function named `find_mode` that takes two lists of numbers as input, combines them into one list, and returns the mode of the combined list using Python's statistics library. The function should handle the list concatenation correctly.
"""

import statistics as stats

def find_mode(list1, list2):
    combined_list = list1 + list2
    mode = stats.mode(combined_list)
    return mode