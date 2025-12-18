"""
QUESTION:
Write a function `reverse_list` that takes a list as input and reverses it in-place, without using built-in list functions or additional memory space. The function should return the reversed list.
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    
    return lst