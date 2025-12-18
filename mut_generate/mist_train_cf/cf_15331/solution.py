"""
QUESTION:
Write a function named `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list.
"""

def sum_of_primes(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in nums if is_prime(num))