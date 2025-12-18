"""
QUESTION:
Create a function named `reverse_and_factorial` that takes a one-dimensional list of non-negative integers as input, reverses the list, and returns a tuple containing the reversed list and a new list with the factorial of each element in the reversed order. Use the math library's `factorial` function for calculation.
"""

import math

def reverse_and_factorial(arr):
    # reverse the array
    arr = arr[::-1]

    factorial_arr = []
    # calculate factorial for each
    for num in arr:
        factorial_arr.append(math.factorial(num))

    return arr, factorial_arr