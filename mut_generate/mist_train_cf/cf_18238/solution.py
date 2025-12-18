"""
QUESTION:
Write a function `find_median` that takes a list of elements as input and returns the median of the integers in the list. The function should handle both odd and even length lists by returning the middle element for odd lengths and the average of the two middle elements for even lengths. The function should return `None` if the list is empty or if it contains only non-integer elements. The function should be able to handle lists with duplicates and non-integer elements.
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