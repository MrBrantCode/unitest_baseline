"""
QUESTION:
Create a function named `sum_of_prime_numbers` that accepts an alphanumeric string as input. The function should return the sum of all the prime number digits (2, 3, 5, 7) present in the string, ignoring all non-prime digits and letters, regardless of their case.
"""

def sum_of_prime_numbers(string):
    prime_digits = ['2', '3', '5', '7']
    return sum(int(digit) for digit in string if digit in prime_digits)