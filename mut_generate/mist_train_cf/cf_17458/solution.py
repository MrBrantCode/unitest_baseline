"""
QUESTION:
Create a function `reverse_list(lst)` that takes a list `lst` as input and reverses its elements in-place without using the reverse() method, built-in Python functions or methods, or creating a new list or additional data structures.
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst