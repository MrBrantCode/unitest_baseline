"""
QUESTION:
Write a recursive function `sum_even` that takes a list of integers as input and returns the sum of all even numbers in the list. The function should handle the case where the input list is empty and return 0 in this case. The solution should be implemented in a single line of code.
"""

def sum_even(lst):
    return 0 if not lst else (lst[0] if lst[0] % 2 == 0 else 0) + sum_even(lst[1:])