"""
QUESTION:
Write a function called `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers from the original array. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. The function should not modify the original array.
"""

def filter_primes(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in arr if is_prime(num)]