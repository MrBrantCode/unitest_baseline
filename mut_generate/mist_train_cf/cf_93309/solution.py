"""
QUESTION:
Implement a function `search` that takes a list of integers `items` and an integer `item` as input. The function should return the index of the first occurrence of `item` in `items` if it exists, otherwise returns -1. The function should have a time complexity of O(n) or better, where n is the length of `items`.
"""

def search(items, item):
    for i in range(len(items)):
        if items[i] == item:
            return i
    return -1