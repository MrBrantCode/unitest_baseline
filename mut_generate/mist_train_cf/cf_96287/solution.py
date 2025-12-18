"""
QUESTION:
Create a function called `replace_and_sort` that takes an array of integers as input. The function should replace all odd numbers in the array with 0 and all even numbers with their square root rounded to the nearest integer. The function should then return a new array containing the modified numbers in descending order with no duplicates. The length of the new array should be equal to the number of unique values in the original array.
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