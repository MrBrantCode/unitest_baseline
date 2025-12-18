"""
QUESTION:
Write a function called `sum_divisible_by_3` that takes an array of integers as input and returns the sum of the elements that are divisible by 3 and greater than 5.
"""

def sum_divisible_by_3(arr):
    sum = 0
    for num in arr:
        if num % 3 == 0 and num > 5:
            sum += num
    return sum