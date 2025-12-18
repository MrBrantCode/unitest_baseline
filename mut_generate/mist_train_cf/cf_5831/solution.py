"""
QUESTION:
Implement a function named `reverse_list` that takes a list of integers as input and reverses the order of its elements in place. The function should have a time complexity of O(n), where n is the length of the list, and it should not use any additional data structures, libraries, recursion, or built-in sorting functions.
"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst