"""
QUESTION:
Design a function named `find_min_abs_difference` that takes two lists of integers as parameters and returns the minimum absolute difference between two elements of the two lists. The function should have a time complexity of O(nlogn), where n is the total number of elements in both lists combined.
"""

def find_min_abs_difference(list1, list2):
    combined_list = sorted(list1 + list2)
    return min(abs(combined_list[i] - combined_list[i + 1]) for i in range(len(combined_list) - 1))