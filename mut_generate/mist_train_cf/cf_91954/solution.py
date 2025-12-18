"""
QUESTION:
Write a function `recursive_sum` that calculates the sum of a list of integers using a recursive approach, without utilizing built-in sum functions or operators. The function should be able to handle edge cases such as empty lists, single-element lists, and lists containing negative numbers, and should not use any additional data structures or variables beyond the function call stack.
"""

def recursive_sum(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    return lst[0] + recursive_sum(lst[1:])