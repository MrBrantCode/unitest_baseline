"""
QUESTION:
Write a function called `reverse_list` that takes a list of unique positive integers as input and reverses its order without using built-in list reversal functions or methods (e.g., `reverse()` or slicing with negative steps). The function should have a time complexity of O(n), where n is the length of the input list, and it should only use basic operations and control flow statements.
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst