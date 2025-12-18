"""
QUESTION:
Write a function named `find_median` that takes two sorted lists of integers as input and returns the median of the combined and sorted list. The function should not assume the lengths of the input lists and should work for both even and odd length lists.
"""

import statistics

def find_median(list1, list2):
    # combining both the lists and sorting
    combined_list = sorted(list1 + list2)
    
    # calculating median
    median_val = statistics.median(combined_list)
    
    return median_val