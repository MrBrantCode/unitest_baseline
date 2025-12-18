"""
QUESTION:
Write a function `find_max(lst)` that finds and returns the maximum element in a list `lst` of up to 10^6 elements, without using the built-in `max()` function. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list.
"""

def find_max(lst):
    max_element = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] > max_element:
            max_element = lst[i]
    
    return max_element