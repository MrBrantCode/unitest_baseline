"""
QUESTION:
Write a recursive function `even_numbers` that takes a list of integers as input and returns a set containing only the even numbers. The function should validate that the input list is not empty and contains only positive integers, raising an exception otherwise. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def even_numbers(lst):
    if len(lst) == 0:
        raise Exception("Input list cannot be empty.")
    if lst[0] < 0:
        raise Exception("Input list must contain only positive integers.")
    if len(lst) == 1:
        if lst[0] % 2 == 0:
            return set([lst[0]])
        else:
            return set()
    else:
        if lst[0] % 2 == 0:
            return set([lst[0]]) | even_numbers(lst[1:])
        else:
            return even_numbers(lst[1:])