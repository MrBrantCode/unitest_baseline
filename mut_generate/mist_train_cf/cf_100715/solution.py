"""
QUESTION:
Create a Python function named `evaluate_expression` that takes a string representing a mathematical expression and returns a tuple containing the result of the expression and a list of all the prime numbers used in the expression. The function must use a helper function named `is_prime` to check whether a number is prime.
"""

import re

def evaluate_expression(expr):
    # Define the helper function is_prime()
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    # Initialize the list of prime numbers used in the expression
    primes = []

    # Evaluate the expression using eval()
    result = eval(expr)

    # Check each number in the expression to see if it is prime
    for num in re.findall(r'\d+', expr):
        if is_prime(int(num)):
            primes.append(int(num))

    # Return the result and list of prime numbers
    return result, primes