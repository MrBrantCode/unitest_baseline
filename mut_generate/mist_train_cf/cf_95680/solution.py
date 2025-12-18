"""
QUESTION:
Write a function called `reverse_list` that takes a list of integers as input, returns a new list with the elements of the input list reversed, and has a time complexity of O(n) and space complexity of O(1). The function should not modify the original list.
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst.copy()