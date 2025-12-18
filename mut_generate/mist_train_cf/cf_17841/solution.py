"""
QUESTION:
Write a function `compute_summation(numbers)` that takes a list of numbers as input and returns the sum of the numbers that are positive, not divisible by 3, and less than or equal to 10.
"""

def compute_summation(numbers):
    total = 0
    for num in numbers:
        if num > 0 and num % 3 != 0 and num <= 10:
            total += num
    return total