"""
QUESTION:
Implement the binary_search function to find the index of a given item in a sorted list of items using the Binary Search algorithm. The function should take two parameters: a sorted list of items and the target item to be searched. If the item is found, return its index; otherwise, return -1. Assume the list is 0-indexed and the input list is already sorted in ascending order.
"""

def entance(items, item): 
    low = 0
    high = len(items) - 1

    while low <= high: 
        mid = (low + high) // 2
        guess = items[mid]
        if guess == item: 
            return mid
        elif guess > item:
            high = mid - 1
        else: 
            low = mid + 1

    return -1