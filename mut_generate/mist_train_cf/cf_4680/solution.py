"""
QUESTION:
Write a function called `calculate_mean_average` that takes a list of numbers as input and returns the mean average of the positive integers in the list. The function should return an error message if the list is empty or if it contains non-integer elements. It should ignore any negative integers in the list and only consider positive integers for the calculation.
"""

def calculate_mean_average(numbers):
    if len(numbers) == 0:
        return "Error: List is empty."
    sum_of_numbers = 0
    count = 0
    for num in numbers:
        if isinstance(num, int) and num > 0:
            sum_of_numbers += num
            count += 1
        elif not isinstance(num, int):
            return "Error: List contains non-integer elements."
    if count == 0:
        return "Error: No positive integers found in the list."
    mean_average = sum_of_numbers / count
    return mean_average