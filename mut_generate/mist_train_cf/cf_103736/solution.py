"""
QUESTION:
Create a function named `is_prime(num)` that takes an integer `num` as input and returns a boolean indicating whether the number is prime or not. The function should check for primality by iterating up to the square root of the input number. Use this function to print all prime numbers in the range 1-100.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True