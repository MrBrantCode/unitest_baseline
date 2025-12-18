"""
QUESTION:
Write a recursive function named `recursive_sum` that calculates the sum of all elements in a given list of integers, without using the built-in sum() function or any loop structure. The function should have a time complexity of O(n), where n is the length of the list.
"""

def recursive_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + recursive_sum(lst[1:])