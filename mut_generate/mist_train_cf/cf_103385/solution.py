"""
QUESTION:
Create a function named `count_primes` that takes an array of integers as input and returns the number of prime numbers in the array.
"""

def count_primes(nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in nums:
        if is_prime(num):
            count += 1
    return count