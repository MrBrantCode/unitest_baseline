"""
QUESTION:
Write a function named `find_median` that takes a list of integers as input and returns the median of the list. The function should handle cases where the list is empty, has an even number of elements, or contains duplicates. If the list is empty, return the string "Error: The list is empty."
"""

def find_median(lst):
    if not lst:
        return "Error: The list is empty."

    sorted_lst = sorted(lst)
    length = len(sorted_lst)

    if length % 2 == 1:
        middle_index = length // 2
        return sorted_lst[middle_index]
    else:
        middle_index_1 = length // 2 - 1
        middle_index_2 = length // 2
        return (sorted_lst[middle_index_1] + sorted_lst[middle_index_2]) / 2