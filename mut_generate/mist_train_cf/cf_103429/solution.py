"""
QUESTION:
Write a function named `first_divisible_by_five` that finds and returns the first element in a given list of numbers that is divisible by 5, larger than 10, and smaller than a specified upper limit. The upper limit should be passed as a parameter to the function.
"""

def first_divisible_by_five(numbers, upper_limit):
    for num in numbers:
        if 10 < num < upper_limit and num % 5 == 0:
            return num
    return None