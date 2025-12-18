"""
QUESTION:
Create a function `calculate_even_sum` that calculates the sum of all the even numbers in a given array. The function should take an array of integers as input and return the sum of the even numbers.
"""

def calculate_even_sum(numbers):
    return sum(num for num in numbers if num % 2 == 0)