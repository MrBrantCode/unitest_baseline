"""
QUESTION:
Design a function named `generate_array` that takes a positive integer `n` as input and returns an array of numbers. The array should start with the greatest number less than or equal to `n`, which is `n` itself. The next number in the array should be the next greatest number less than or equal to the last added number, which is `n-1`, and so on, until the array contains all numbers from `n` down to 0.
"""

def generate_array(n):
    array = []
    while n >= 0:
        array.append(n)
        n -= 1
    return array