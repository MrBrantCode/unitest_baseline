"""
QUESTION:
Write a function `calc_val(nbrs)` that calculates the sum of all numbers in the input list `nbrs` and returns the result. The function should correctly iterate over the list and add each number to the result. The input list `nbrs` is a list of numbers. The function should be written in Python.
"""

def calc_val(nbrs):
    result = 0
    for num in nbrs:
        result += num
    return result