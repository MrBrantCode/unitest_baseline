"""
QUESTION:
Write a function named `compute_mean` that takes a string of comma-separated numbers as input, converts it into a list of integers, and returns the mean of the numbers. The input string will only contain integers separated by commas, with optional spaces around the commas.
"""

def compute_mean(input_string):
    numbers = [int(num) for num in input_string.replace(" ", "").split(",")]
    return sum(numbers) / len(numbers)