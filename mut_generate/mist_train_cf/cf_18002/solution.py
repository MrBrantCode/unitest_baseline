"""
QUESTION:
Write a function `sum_of_cubes` that calculates the sum of the cubes of all the digits in a given positive integer. The function should take an integer as input, and return the sum of the cubes of its digits. The input integer is guaranteed to be positive.
"""

def sum_of_cubes(n):
    sum_of_cubes = 0
    while n > 0:
        digit = n % 10
        sum_of_cubes += digit ** 3
        n //= 10
    return sum_of_cubes