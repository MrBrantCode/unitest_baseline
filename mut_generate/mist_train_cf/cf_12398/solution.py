"""
QUESTION:
Create a function called `reverse_list` that takes a list of integers as input and returns the list in reverse order. The function should not use any built-in list reversal methods or additional data structures, and it should have a time complexity of O(n), where n is the length of the list.
"""

def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst