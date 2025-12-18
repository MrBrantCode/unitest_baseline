"""
QUESTION:
Develop a function `sum_others(arr)` that takes an array of integers as input and returns an array where each element at index `i` is the sum of all integers in the input array except the integer at index `i`. The input array will contain integers. The function should not use any external libraries and should be implemented in pure Python.
"""

def sum_others(arr):
    return [sum(arr) - x for x in arr]