"""
QUESTION:
Write a function "count_prime_pairs" that takes an array of positive integers as input and returns the count of pairs whose absolute difference is a prime number. The function should have a time complexity of O(n * sqrt(m)), where n is the length of the input array and m is the maximum number in the array.
"""

def count_prime_pairs(nums):
    def is_prime(num):
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in nums if is_prime(num)]
    count = sum(1 for num in nums for prime in primes if is_prime(abs(num - prime)))
    return count