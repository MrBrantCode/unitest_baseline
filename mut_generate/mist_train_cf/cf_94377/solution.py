"""
QUESTION:
Write a function named `sum_positive_even` that takes an array of integers as input and returns the sum of its positive even elements that are not divisible by 3 or 5.
"""

def sum_positive_even(arr):
    sum = 0
    for num in arr:
        if num > 0 and num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
            sum += num
    return sum