"""
QUESTION:
Write a function named `prime_sum` that takes a list of integers as input. The function should calculate the sum of all prime numbers in the list that are greater than 100 and less than 1000. The function should return the sum of these prime numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(lst):
    primes = [num for num in lst if 100 < num < 1000 and is_prime(num)]
    return sum(primes)