"""
QUESTION:
Write a function `calculate_mean` that calculates the mean of a list of numbers. The list can contain up to 10^6 numbers, including negative and decimal numbers. The function should use a for loop to iterate over the list.
"""

def calculate_mean(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    mean = total / count
    return mean