"""
QUESTION:
Write a function named `count_prime_with_digit_3` that takes a list of integers as input and returns the count of prime numbers that contain the digit 3.
"""

def count_prime_with_digit_3(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in nums:
        if '3' in str(num) and is_prime(num):
            count += 1
    return count