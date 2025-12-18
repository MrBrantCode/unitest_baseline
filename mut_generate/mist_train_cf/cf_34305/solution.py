"""
QUESTION:
Implement a function `count_primes` that takes a list of integers `nums` (0 <= len(nums) <= 10^5) as input, where each integer n (0 <= n <= 10^6), and returns the count of prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def count_primes(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for num in nums if is_prime(num))