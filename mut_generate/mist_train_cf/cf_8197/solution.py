"""
QUESTION:
Implement a function `search` that takes a sorted list of distinct integers `items` and an integer `item` as input. The function should return the index of the first occurrence of `item` in `items` if it exists, otherwise returns -1. The function should have a time complexity of O(log n) or better, where n is the length of `items`, and a space complexity of O(1). The list `items` contains at most 10^6 integers, and each element is an integer between -10^6 and 10^6.
"""

def search(items, target): 
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1