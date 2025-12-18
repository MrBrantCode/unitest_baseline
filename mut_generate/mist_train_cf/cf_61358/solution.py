"""
QUESTION:
Implement a function `validate_and_categorize(n)` that takes an integer `n` as input, validates whether the input is a positive integer, and categorizes numbers from 2 to `n` into prime and composite numbers. The function should return two lists: one for prime numbers and the other for composite numbers. If the input is invalid, the function should return an error message.
"""

def validate_and_categorize(n):
    if type(n) is not int or n <= 0:  # error handling part
        return "Error: The input is invalid"

    prime_numbers = []
    composite_numbers = []

    for i in range(2, n+1):
        for j in range(2, i):
            if (i % j) == 0:  # number is composite
                composite_numbers.append(i)
                break
        else:  # number is prime 
            prime_numbers.append(i)

    return prime_numbers, composite_numbers