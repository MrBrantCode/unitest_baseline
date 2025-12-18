"""
QUESTION:
Implement a function `search` that takes a sorted list of distinct integers `items` and an integer `item` as input, and returns the index of the first occurrence of `item` in `items` if it exists, otherwise returns -1. The function should have a time complexity of O(log n) or better and a space complexity of O(1), where n is the length of `items`.
"""

def search(items, item): 
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == item:
            return mid
        elif items[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1