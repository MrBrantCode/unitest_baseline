"""
QUESTION:
Create a function `calculate_difference(list1, list2)` that takes two lists of integers as input and returns a new list containing the differences between the common elements of the two lists. The difference should be calculated by subtracting the element in `list2` from the element in `list1`, and only non-negative differences should be included in the output list. The output list should be sorted in descending order.
"""

def calculate_difference(list1, list2):
    common_elements = set(list1).intersection(list2)  # find common elements
    difference_list = [x - y for x, y in zip(list1, list2) if x - y >= 0 and x in common_elements]
    difference_list.sort(reverse=True)
    return difference_list