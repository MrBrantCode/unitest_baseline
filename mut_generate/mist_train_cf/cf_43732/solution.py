"""
QUESTION:
Write a function called `isPrime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number or not. The function should be used to find all prime numbers between 0 and 1000, and then determine the number of twin prime pairs in this range, where twin prime pairs are pairs of prime numbers that differ by 2. The function should be efficient and handle large ranges of numbers.
"""

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True