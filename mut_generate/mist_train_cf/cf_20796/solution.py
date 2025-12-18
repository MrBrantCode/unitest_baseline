"""
QUESTION:
Create a function `replace_and_sort(arr)` that takes an array of integers as input and returns a new array with the following conditions:
- Replace all odd numbers with 0.
- Replace all even numbers with their square root rounded to the nearest integer.
- Sort the new array in descending order.
- Remove any duplicate values from the new array.
- Ensure the length of the new array is equal to the number of unique values in the original array.
"""

import math

def replace_and_sort(arr):
    unique_nums = set()

    for num in arr:
        if num % 2 == 1:
            unique_nums.add(0)
        else:
            unique_nums.add(math.isqrt(num))

    sorted_nums = sorted(list(unique_nums), reverse=True)
    return sorted_nums