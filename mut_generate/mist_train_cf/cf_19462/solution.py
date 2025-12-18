"""
QUESTION:
Create a function `reverse_list(lst)` that takes a list of integers as input and returns a new list with the elements of the input list reversed. The function should have a time complexity of O(n) and a space complexity of O(1), and should not modify the original list.
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst.copy()