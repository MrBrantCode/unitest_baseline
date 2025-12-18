"""
QUESTION:
Write a function `calculate_mean(numbers)` that calculates the mean of a list of numbers. The list may contain up to 10^6 numbers, including negative numbers, decimal numbers, and numbers greater than 1000. The function should return the mean rounded to two decimal places.
"""

def calculate_mean(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    mean = total_sum / len(numbers)
    return round(mean, 2)