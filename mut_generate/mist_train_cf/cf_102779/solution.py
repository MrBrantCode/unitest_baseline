"""
QUESTION:
Write a function named `sum_divisible_by_3` that takes a list of integers as input and returns the sum of all numbers in the list that are divisible by 3 and less than 100.
"""

def sum_divisible_by_3(numbers):
    total = 0
    for num in numbers:
        if num % 3 == 0 and num < 100:
            total += num
    return total