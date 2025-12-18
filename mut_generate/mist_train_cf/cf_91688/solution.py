"""
QUESTION:
Write a recursive function `recursive_sum(lst)` that calculates the sum of all elements in a given list `lst` of integers without using any built-in sum function or loop structure. The function should have a time complexity of O(n), where n is the length of the list.
"""

def entance(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + entance(lst[1:])