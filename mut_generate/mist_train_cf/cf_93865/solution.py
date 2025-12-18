"""
QUESTION:
Write a function named `calculate_mean` that takes a list of numbers as input, calculates the mean using a for loop, and returns the result. The input list may contain up to 10^6 numbers, including negative numbers and decimal numbers.
"""

def calculate_mean(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    mean = total / count
    return mean