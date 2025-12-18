"""
QUESTION:
Write a function called `reverse_list` that takes a Python list as input and returns its reversed version without using the built-in `reverse()` method, slicing syntax, or any other built-in function or method to reverse the list. The function should be able to handle lists of any length, including empty lists and lists with one element.
"""

def reverse_list(lst):
    # Check if the list is empty or contains only one element
    if len(lst) < 2:
        return lst
    
    # Swap elements starting from the ends until the middle
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst