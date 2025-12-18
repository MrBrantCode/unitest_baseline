"""
QUESTION:
Write a function named `isPrime` that uses the filter() function to find all prime numbers from an array of numbers. Implement your own algorithm to check for primality without using any built-in methods or functions. The function should return a list of prime numbers.
"""

def isPrime(num):
    # Check if the number is less than 2
    if num < 2:
        return False
    # Check if the number is divisible by any number less than itself
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes(numbers):
    return list(filter(isPrime, numbers))