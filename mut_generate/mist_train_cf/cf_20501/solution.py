"""
QUESTION:
Write a function named `multiply_array` that takes an array of integers as input and returns their product as a floating-point number. The function should handle negative numbers and the case where the product exceeds the range of a floating-point number, returning positive or negative infinity accordingly. If the input array is empty, the function should return 1.0.
"""

def multiply_array(arr):
    if len(arr) == 0:
        return 1.0

    product = 1.0
    for num in arr:
        product *= num

    if product > 1.7976931348623157e+308:
        return float('inf')
    elif product < -1.7976931348623157e+308:
        return float('-inf')
    else:
        return product