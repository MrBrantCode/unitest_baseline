"""
QUESTION:
Write a function named `sum_positive_even` that takes an array of integers as input. The function should return the sum of the positive even elements that are not divisible by 3. The function should be able to handle both positive and negative integers.
"""

def sum_positive_even(arr):
    total = 0
    for num in arr:
        if num > 0 and num % 2 == 0 and num % 3 != 0:
            total += num
    return total