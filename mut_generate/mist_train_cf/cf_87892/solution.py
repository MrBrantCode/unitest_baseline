"""
QUESTION:
Create a function called `get_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should have a time complexity of O(n^2), where n is the length of the input list. The function should utilize a helper function `is_prime` to check if a number is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_primes(lst):
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return primes