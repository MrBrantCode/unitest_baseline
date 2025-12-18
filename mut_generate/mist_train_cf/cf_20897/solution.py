"""
QUESTION:
Create a function `sumPositiveIntegers` that takes an array of positive integers as input and returns the sum of the integers greater than 1000. The function should only accept arrays of integers and does not perform error checking on the input type.
"""

def sumPositiveIntegers(numbers):
    return sum(num for num in numbers if num > 1000)