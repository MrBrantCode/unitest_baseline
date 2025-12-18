"""
QUESTION:
Implement a function `binary_search` that checks if a specific item exists in a sorted list of lists with a time complexity of O(log(n)). The list of lists is already sorted based on the sub-lists converted into tuples. The function should take two parameters: a sorted list of lists and a target item to search for, and return `True` if the target item exists in the list, and `False` otherwise.
"""

def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = sorted_list[mid]

        if mid_val == target:
            return True
        elif tuple(mid_val) < tuple(target):
            low = mid + 1
        else:
            high = mid - 1

    return False