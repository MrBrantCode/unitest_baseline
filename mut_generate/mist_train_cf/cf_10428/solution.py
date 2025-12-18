"""
QUESTION:
Implement a function called `calculate_sum` that calculates the sum of numbers in a given list, ignoring any numbers that are divisible by 3. The list can contain both positive and negative integers.
"""

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if num % 3 != 0:
            total += num
    return total