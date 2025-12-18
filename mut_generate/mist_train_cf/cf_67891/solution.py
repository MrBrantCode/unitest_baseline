"""
QUESTION:
Construct a function named `is_prime` that takes one integer argument, checks whether the number is prime, and returns a boolean value. Then, create a loop that continues to prompt the user for an integer input until a prime number is entered, using the `is_prime` function to check the input. The loop should print an error message for non-prime inputs and display a confirmation message once a prime number is entered.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True