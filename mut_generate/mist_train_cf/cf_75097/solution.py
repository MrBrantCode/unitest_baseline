"""
QUESTION:
Write a function named `five_largest_primes(nums)` that takes a list of integers as input and returns the 5 largest prime numbers in the list. If the list contains less than 5 prime numbers, return a message "Less than 5 prime numbers in the list."
"""

def five_largest_primes(nums):
    def is_prime(n):
        if n > 1:
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for possible in range(3, int(n ** 0.5) + 1, 2):
                if n % possible == 0:
                    return False
            return True
        return False

    primes = [num for num in nums if is_prime(num)]
    primes.sort()
    return primes[-5:] if len(primes) >= 5 else "Less than 5 prime numbers in the list"