"""
QUESTION:
Write a function named `sum_of_primes` that takes an array of integers as input and returns the sum of all prime numbers in the array. The function should be able to handle arrays containing positive integers.
"""

def sum_of_primes(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(x for x in arr if is_prime(x))