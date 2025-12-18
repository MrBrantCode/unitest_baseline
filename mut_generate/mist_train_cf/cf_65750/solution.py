"""
QUESTION:
Write a function named `gcd` that takes two distinct integers as input and returns their Greatest Common Divisor using the Euclidean Algorithm, without using any built-in GCD functionality. The function should be able to handle any two positive integers.
"""

def gcd(number_1, number_2):
    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1