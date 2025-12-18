"""
QUESTION:
Write a function `calculate_sum` that takes a list of integers as input and returns the sum of all non-negative numbers that are not divisible by 3 and do not contain the digit 5.
"""

def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        if num < 0:
            continue
        if num % 3 == 0 or '5' in str(num):
            continue
        total_sum += num
    return total_sum