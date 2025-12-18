"""
QUESTION:
Write a function `sum_array` that takes an array of mixed data types as input and returns the sum of all integer elements in the array. The function should not use any built-in sum functions or libraries and should handle arrays of varying sizes. If the input array contains non-integer elements, the function should skip these elements and only sum the integer values.
"""

def sum_array(arr):
    total = 0
    for element in arr:
        if isinstance(element, int):
            total += element
    return total