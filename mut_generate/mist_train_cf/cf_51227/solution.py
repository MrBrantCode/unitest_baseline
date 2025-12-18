"""
QUESTION:
Create a function `scan_array(nums)` that takes a list of integers `nums` as input, and returns a list of all prime numbers present in `nums`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def scan_array(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True

    prime_nums = [n for n in nums if is_prime(n)]
    return prime_nums