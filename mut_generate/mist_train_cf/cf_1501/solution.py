"""
QUESTION:
Write a function `find_median` that calculates the median of a given list of integers. The function should handle cases where the list is empty, has an even number of elements, or contains duplicates. It should return the median as a number, or an error message if the list is empty.
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