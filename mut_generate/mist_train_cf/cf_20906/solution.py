"""
QUESTION:
Create a function `multiply_by_index` that takes an array of integers as input. The function should multiply each element in the array by its 0-based index and return the sum of the resulting values.
"""

def multiply_by_index(arr):
    return sum(i * x for i, x in enumerate(arr))