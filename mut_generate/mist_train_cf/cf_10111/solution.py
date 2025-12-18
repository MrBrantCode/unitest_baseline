"""
QUESTION:
Implement a function `binary_search(lst, number)` that searches for a given number in a sorted list of integers. The list is sorted in ascending order, and the function should have a time complexity of O(log n), where n is the length of the list. Return True if the number is found, and False otherwise.
"""

def entrance(lst, number):
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