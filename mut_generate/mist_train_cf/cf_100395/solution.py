"""
QUESTION:
Write a function `calculate_average` that takes an array of integers as input and returns the average of even numbers with a factor of 3. The function should return 0 if no such numbers are found.
"""

def calculate_average(numbers):
    count = 0
    total_sum = 0

    for number in numbers:
        if number % 2 == 0 and number % 3 == 0:
            count += 1
            total_sum += number

    return total_sum / count if count > 0 else 0