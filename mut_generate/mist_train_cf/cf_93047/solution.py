"""
QUESTION:
Write a function named `last_three_primes` that takes a list of integers as input and returns the last three prime numbers found in the list in reverse order. If there are less than three prime numbers in the list, return all of them. Assume that the input list is not empty and contains at least one prime number.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def last_three_primes(numbers):
    primes = []
    for num in reversed(numbers):
        if is_prime(num):
            primes.append(num)
        if len(primes) == 3:
            break
    return primes