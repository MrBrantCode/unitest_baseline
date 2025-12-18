"""
QUESTION:
Develop a function called `find_median` that takes an arbitrary-sized list of integers as input and returns the median of the list. The function should handle lists with both an even and odd number of elements, returning the average of the two middle elements in the case of an even number of elements. The function should also handle invalid input types (non-list and non-integer values) and empty lists, returning an error message in these cases. The solution should utilize an efficient sorting algorithm with a time complexity of O(n log n).
"""

import numpy as np

def find_median(num_list):
    if not isinstance(num_list, list):
        return "Error: Input is not a list."
    if not all(isinstance(i, int) for i in num_list):
        return "Error: List contains non-integer values."
    if len(num_list) == 0:
        return "Error: The list is empty."
    
    num_list.sort()
    
    middle_index = len(num_list)//2
    if len(num_list)%2==0:
        return (num_list[middle_index-1] + num_list[middle_index]) / 2.0
    else:
        return num_list[middle_index]