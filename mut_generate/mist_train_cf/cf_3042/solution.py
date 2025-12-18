"""
QUESTION:
Compute the sum of all elements in an array of non-negative integers using a recursive function. The function should take an array of up to 1000 elements as input and return the total sum. The function name is `sum_array_elements`.
"""

def sum_array_elements(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array_elements(arr[1:])