"""
QUESTION:
Implement a function `search` that takes a list of integers `items` and an integer `item` as input and returns the index of the first occurrence of `item` in `items` if it exists, otherwise returns -1. The function should have a time complexity of O(n) or better, where n is the length of `items`. The list `items` contains at most 10^6 integers, and each element in `items` is an integer between -10^6 and 10^6.
"""

def search(items, item): 
    for i in range(len(items)): 
        if items[i] == item:
            return i 
    return -1