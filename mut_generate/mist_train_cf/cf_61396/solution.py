"""
QUESTION:
Write a function called `recursive_sum_of_squares` that takes a list of numbers as input and returns the sum of the squares of all elements in the list using recursion. The function should be able to handle lists of any length.
"""

def recursive_sum_of_squares(lst, idx=0):
    if idx < len(lst):
        return lst[idx]**2 + recursive_sum_of_squares(lst, idx + 1)
    else:
        return 0