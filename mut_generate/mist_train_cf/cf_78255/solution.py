"""
QUESTION:
Write a function named `multiply_list` that takes a non-empty list of integers `lst` and a non-zero integer `n` as input. The function should return a new list where each integer is the product of the input integer `n` and the corresponding integer from the list. The function should be optimized to handle large lists efficiently and should work correctly for lists containing negative integers or zeros.
"""

def multiply_list(n, lst):
    for i in range(len(lst)):
        lst[i] *= n
    return lst