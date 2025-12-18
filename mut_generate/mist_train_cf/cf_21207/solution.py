"""
QUESTION:
Write a function named `is_prime_and_square` that takes a list of integers as input and prints the square of each number in the list, but only if the number is prime. The input list should be iterated using a for loop and the prime check should be performed using a helper function.
"""

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_prime_and_square(numbers):
    """Prints the square of each number in the list, but only if the number is prime."""
    for num in numbers:
        if is_prime(num):
            print(num ** 2)