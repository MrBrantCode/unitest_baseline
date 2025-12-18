"""
QUESTION:
Write a function `find_max(lst)` that takes a list of integers as input and returns the maximum element in the list. The function must have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(1). Do not use the built-in `max()` function.
"""

def find_max(lst):
    max_element = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    
    return max_element