"""
QUESTION:
Create a function `count_odd_greater_than_10_divisible_by_3` that takes an array of integers as input and returns the quantity of odd numbers that are greater than 10 and divisible by 3.
"""

def count_odd_greater_than_10_divisible_by_3(arr):
    count = 0
    for num in arr:
        if num > 10 and num % 3 == 0 and num % 2 != 0:
            count += 1
    return count