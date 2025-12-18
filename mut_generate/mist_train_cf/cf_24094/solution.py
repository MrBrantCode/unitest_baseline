"""
QUESTION:
Write a function `calculate_average` that takes a list of numbers as input and returns their average. The function should iterate over the list, sum up all the numbers, and divide the sum by the count of numbers. The function should not use any built-in sum or average functions. The input list is guaranteed to be non-empty.
"""

def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)