"""
QUESTION:
Design a function called `find_primes` that takes a list of integers as input and returns a list of prime numbers found in the input list. A prime number is a number that has exactly two distinct positive divisors: 1 and itself. The function should not modify the input list and should return a new list containing only the prime numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True

def find_primes(numbers):
    primes = [number for number in numbers if is_prime(number)]
    return primes