"""
QUESTION:
Write a function `is_prime(num)` that checks if a number is prime. The function should take an integer `num` as input and return a boolean value. The function should be efficient and able to handle large numbers by only checking divisors up to the square root of `num`. The function should return `False` for numbers less than 2.
"""

def is_prime(num):
    # 0 and 1 are not prime numbers
    if num < 2:
        return False
    # 2 is the only even prime number
    if num == 2: 
        return True
    # all other even numbers are not primes
    if not num & 1: 
        return False
    # range starts with 3 and only needs to go up the square root of n
    # for all odd numbers
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True