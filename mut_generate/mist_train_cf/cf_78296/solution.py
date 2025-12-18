"""
QUESTION:
Write a function named `lcm_for_numbers` that takes a variable number of arguments and returns the least common multiple of all the numbers. The function should use a helper function named `gcd` to calculate the greatest common divisor of two numbers, and another helper function `lcm` to calculate the least common multiple of two numbers. Assume that the input numbers are positive integers.
"""

from functools import reduce

# Function to compute gcd (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to compute lcm (Least Common Multiple)
def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_for_numbers(*numbers):
    return reduce(lcm, numbers)