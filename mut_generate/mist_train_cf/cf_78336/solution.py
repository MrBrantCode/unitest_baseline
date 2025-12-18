"""
QUESTION:
Design a function named `linear_search` that takes an unsorted array and an item as input and returns the index of the item if found in the array, or -1 if not found. The function should have a time complexity of O(n).
"""

def linear_search(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i
    return -1