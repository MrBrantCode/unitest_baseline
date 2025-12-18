"""
QUESTION:
Create a function named `smallest_prime` that takes an array of natural numbers as input and returns the smallest prime number within the array. The function should handle arrays containing multiple prime numbers and return the lowest numerical value among them. Assume the input array will contain only natural numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def smallest_prime(array):
    primes = [x for x in array if is_prime(x)]
    return min(primes)