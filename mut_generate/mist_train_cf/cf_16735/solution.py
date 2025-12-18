"""
QUESTION:
Write a function named `sum_positive_even` that calculates the sum of the positive even elements in an array, excluding any elements that are divisible by 3 or 5. The input array will contain a mix of positive and negative integers.
"""

def sum_positive_even(arr):
    sum = 0
    for num in arr:
        if num > 0 and num % 2 == 0 and num % 3 != 0 and num % 5 != 0:
            sum += num
    return sum