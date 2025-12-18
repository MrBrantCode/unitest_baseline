"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` and recursively checks if it is a prime number. The function should have a helper parameter `i` with a default value of 2. The function should return `True` if `n` is prime and `False` otherwise. Using this function, prompt the user to enter a positive integer greater than 1, save it as the variable `num`, and print whether the number is prime or not.
"""

def is_prime(n, i=2):
    # Base cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    
    # Recursive case
    return is_prime(n, i + 1)