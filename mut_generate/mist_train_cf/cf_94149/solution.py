"""
QUESTION:
Write a function `sum_divisible_by_three` that takes a list of integers as input, and returns a tuple containing the sum and count of numbers that are divisible by 3 and less than 100.
"""

def sum_divisible_by_three(numbers):
    count = 0
    total = 0
    
    for num in numbers:
        if num % 3 == 0 and num < 100:
            total += num
            count += 1
    
    return total, count