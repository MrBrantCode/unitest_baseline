"""
QUESTION:
Create a function named `filter_and_sort` that takes a list of numbers (`old_list`) and a number (`threshold`) as input parameters. The function should return a new list containing all elements from `old_list` that are greater than the `threshold` value, sorted in descending order. The input list and threshold values are not fixed and will be provided at runtime.
"""

def filter_and_sort(old_list, threshold):
    return sorted([x for x in old_list if x > threshold], reverse=True)