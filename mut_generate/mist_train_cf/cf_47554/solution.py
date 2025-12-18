"""
QUESTION:
Create a function called `calculate_median` that takes a list of floating point numbers as input and returns the median of the numbers. The list will always contain exactly 5 numbers.
"""

def calculate_median(numbers): 
    numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        median = (numbers[length//2] + numbers[length//2-1]) / 2
    else:
        median = numbers[length//2]
    return median