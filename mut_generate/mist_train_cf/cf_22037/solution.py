"""
QUESTION:
Write a function named `sort_prime_composite` that takes a list of positive integers as input and returns a tuple of two lists. The first list contains the prime numbers in ascending order and the second list contains the composite numbers in descending order. Note that 1 is considered neither prime nor composite.
"""

def sort_prime_composite(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = sorted([num for num in nums if is_prime(num)])
    composites = sorted([num for num in nums if not is_prime(num) and num != 1], reverse=True)
    
    return (primes, composites)