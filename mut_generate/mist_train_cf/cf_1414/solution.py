"""
QUESTION:
Write a function named `is_prime(num)` to check if a number is prime and then use this function to store the first 1000 prime numbers in a list. Finally, print these prime numbers in reverse order. The `is_prime(num)` function should return False for numbers less than 2 and True if a number is only divisible by 1 and itself.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True