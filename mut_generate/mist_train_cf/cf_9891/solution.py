"""
QUESTION:
Write a function named `calculate_average` that calculates the average of numbers in a list that are divisible by 3 and greater than 10. The function should take a list of integers as input and return the average as a floating point number.
"""

def calculate_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        if num % 3 == 0 and num > 10:
            total += num
            count += 1

    return total / count if count != 0 else 0