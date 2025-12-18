"""
QUESTION:
Write a function `calculate_difference(list1, list2)` that takes two lists of integers as input and returns a new list containing the non-negative differences between common elements in the two lists, sorted in descending order.
"""

def calculate_difference(list1, list2):
    common_elements = set(list1).intersection(list2)  # find common elements
    difference_list = [abs(x - y) for x in list1 for y in list2 if x == y]
    difference_list.sort(reverse=True)
    return difference_list