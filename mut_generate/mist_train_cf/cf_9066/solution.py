"""
QUESTION:
Write a function called `calculate_median` that takes a list of numbers as input and returns the median of the list. The list can contain any number of elements.
"""

def calculate_median(lst):
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    mid = length // 2
    
    if length % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
        
    return median