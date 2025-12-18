"""
QUESTION:
Write a function named `calculate_average` that takes a list of numbers as input, uses a for loop to calculate the sum of the numbers in the list, and then returns the average of the sum. The function should not use built-in sum or average functions.
"""

def calculate_average(numbers):
    sum_of_numbers = 0
    for num in numbers:
        sum_of_numbers += num
    return sum_of_numbers / len(numbers)