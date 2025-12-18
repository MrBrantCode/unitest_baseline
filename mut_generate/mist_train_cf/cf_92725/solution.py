"""
QUESTION:
Write a function `is_prime_and_divisible_by_6` that takes a list of integers as input and returns a new list containing only the integers that are both divisible by 6 and prime numbers.
"""

def is_prime_and_divisible_by_6(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in nums if num % 6 == 0 and is_prime(num)]