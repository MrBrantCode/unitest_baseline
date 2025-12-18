"""
QUESTION:
Write a function named `sum_of_primes` that takes an array of integers as input, and returns the sum of all prime numbers in the array. The input array will contain at least one prime number and at most 1000 elements.
"""

def sum_of_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in arr if is_prime(num))