"""
QUESTION:
Create a function `array_prime_or_composite(arr)` that takes an array as input and returns "Prime" if the number of elements in the array is a prime number, and "Composite" otherwise. The function should handle arrays of any length and should be efficient for large inputs.
"""

import math

def array_prime_or_composite(arr):
    array_length = len(arr)
    if array_length <= 1:
        return "Composite"
    if array_length == 2:
        return "Prime"
    if array_length % 2 == 0:
        return "Composite"
    sqrtn = math.isqrt(array_length)
    for divider in range(3, sqrtn + 1, 2):
        if array_length % divider == 0:
            return "Composite"
    return "Prime"