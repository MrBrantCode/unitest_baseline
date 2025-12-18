"""
QUESTION:
Write a function named `count_prime_numbers` that takes two integers, `start` and `end`, as input and returns a tuple containing the count and sum of all prime numbers within the range defined by `start` and `end`, inclusively. The function must not use any built-in prime number calculation functions or libraries and should have a time complexity of O(n^2), where n is the length of the range. The input range will always be positive and `start` will always be less than or equal to `end`.
"""

from typing import Tuple

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def count_prime_numbers(start: int, end: int) -> Tuple[int, int]:
    count = 0
    prime_sum = 0
    
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
            prime_sum += num
    
    return count, prime_sum