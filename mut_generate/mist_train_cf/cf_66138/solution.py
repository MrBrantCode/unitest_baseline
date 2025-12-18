"""
QUESTION:
Write a function `find_factors` that takes a list of integers as input and returns a list of numbers that must be factors of an integer that ends with the digit zero and has a digit sum that is a multiple of 3. The function should only consider the input numbers 2, 3, 4, 5, 6, 8, and 9.
"""

def find_factors(numbers):
    factors = []
    for num in numbers:
        if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
            factors.append(num)
    return factors