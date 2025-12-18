"""
QUESTION:
Create a function `get_prime_numbers` that takes a list of integers as input and returns a list containing only the prime numbers in the input list. The function should have a time complexity of O(n^2), where n is the length of the input list.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes