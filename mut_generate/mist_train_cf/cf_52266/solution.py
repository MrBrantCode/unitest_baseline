"""
QUESTION:
Write a function named `sum_penultimate` that takes a list of integers as input, sorts the list in ascending order, and returns the sum of the second largest (penultimate minor) and the second smallest (penultimate major) integers in the list. The list may contain duplicate values and can be of any length greater than 1.
"""

def sum_penultimate(lst):
    sorted_list = sorted(lst)
    penultimate_minor = sorted_list[-2]  # second largest
    penultimate_major = sorted_list[1]  # second smallest
    return penultimate_minor + penultimate_major