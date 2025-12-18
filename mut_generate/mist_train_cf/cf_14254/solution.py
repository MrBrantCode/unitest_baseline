"""
QUESTION:
Create a function `sum_rows(arr)` that takes a two-dimensional array as input and returns a new array containing the sum of each row in reverse order. The input array will contain sub-arrays of integers.
"""

def sum_rows(arr):
    return [sum(row) for row in arr][::-1]