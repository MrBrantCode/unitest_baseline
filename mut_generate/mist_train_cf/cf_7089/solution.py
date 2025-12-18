"""
QUESTION:
Write a function `binary_search` that checks if a specific item exists in a sorted list of lists in Python, with a time complexity of O(log(n)). The function should take two parameters: `lists` (the sorted list of lists) and `target` (the specific item to be searched).
"""

def binary_search(lists, target):
    lists = sorted(lists, key=lambda x: tuple(x))
    low = 0
    high = len(lists) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = lists[mid]

        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False