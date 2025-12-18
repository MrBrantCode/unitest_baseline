"""
QUESTION:
Write a function named `sum_of_primes` that takes an array of integers as input and returns the sum of the prime numbers in the array. The function should consider only positive integers greater than 1 as prime numbers. Implement a prime number checking algorithm such as the Sieve of Eratosthenes for efficiency.
"""

def sum_of_primes(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in nums if is_prime(num)]
    return sum(primes)