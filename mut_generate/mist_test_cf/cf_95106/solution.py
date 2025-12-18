"""
QUESTION:
Write a function `find_median` that takes a list of integers as input, returns the median of the elements in the list, and handles both odd and even length lists. The function should return the average of the two middle elements for even length lists and handle cases where the list may contain non-integer elements or duplicates. If the list is empty or contains only non-integer elements, the function should return `None`.
"""

def find_median(lst):
    # Check if the list is empty or contains only non-integer elements
    if len(lst) == 0 or not all(isinstance(x, int) for x in lst):
        return None

    # Sort the list in ascending order
    sorted_lst = sorted(lst)

    # Calculate the index of the middle element(s)
    mid = len(sorted_lst) // 2

    # Check if the list has an odd length
    if len(sorted_lst) % 2 == 1:
        return sorted_lst[mid]
    else:
        # Calculate the average of the two middle elements
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2