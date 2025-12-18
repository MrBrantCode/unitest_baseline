"""
QUESTION:
Write a function called `sum_of_cubes` that takes a positive integer as input and returns the sum of the cubes of each digit in the number, with a time complexity of O(n), where n is the number of digits in the input number.
"""

def sum_of_cubes(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit**3
        n //= 10
    return total