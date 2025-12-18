"""
QUESTION:
Write a function `sum_array_elements` that calculates the sum of all elements in a given list of integers. The function should take one argument, a list of integers, and return the sum of its elements. The list will contain only integers.
"""

def sum_array_elements(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i]
    return result