"""
QUESTION:
Write a function `binary_search` that takes a sorted list of integers `lst` and a target number `number` as input. The function should return `True` if the target number exists in the list and `False` otherwise. The function must have a time complexity of O(log n), where n is the length of the list. The input list will always be sorted in ascending order.
"""

def binary_search(lst, number):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == number:
            return True
        elif lst[mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return False