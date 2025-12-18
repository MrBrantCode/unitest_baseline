"""
QUESTION:
Write a function named `is_prime` that takes an integer input `n` and returns `True` if the number is prime, `False` otherwise. The function should also handle erroneous values effectively, such as non-integer inputs, and return a custom error message. Optimize the function to handle large numbers efficiently by only checking factors up to the square root of `n`. The function should return an error message if `n` is not a positive integer greater than 1.
"""

def is_prime(n):
    # Error handling for non-integer or negative input
    if type(n) != int or n < 0:
        return "Invalid input. Please input a positive integer greater than 1."
    if n in [0, 1]:
        return False
    # Optimization: Only need to check factors up to sqrt(n)
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True