"""
QUESTION:
Implement a function `is_prime(num)` that checks if a given number is a prime number and use it to print all the prime numbers between 1 and 1000. The function should take an integer `num` as input and return a boolean value indicating whether the number is prime or not. Use a loop to check divisibility from 2 to the square root of the number. The function should return `False` for numbers less than 2.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True