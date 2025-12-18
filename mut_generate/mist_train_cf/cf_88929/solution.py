"""
QUESTION:
Create a function named `find_primes(n)` that takes an integer `n` as input and returns a list of prime numbers less than `n`. The function should raise a custom exception if the input is not a positive integer greater than 1. The solution should have a time complexity of O(n^1.5) or better and a space complexity of O(n).
"""

def find_primes(n):
    if not isinstance(n, int) or n <= 1:
        raise Exception("Input must be a positive integer greater than 1.")
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes