"""
QUESTION:
Define a function `filter_numbers` that takes a list of integers as input and returns a new list containing only the integers that are divisible by 6, are prime numbers, and have a digit sum greater than 10.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_numbers(nums):
    return [num for num in nums if num % 6 == 0 and is_prime(num) and sum(int(digit) for digit in str(num)) > 10]