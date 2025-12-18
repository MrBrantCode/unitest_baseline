"""
QUESTION:
Write a function `count_prime_numbers` that takes two integers `start` and `end` as input and returns a tuple containing the count and sum of all prime numbers within the inclusive range `[start, end]`. You cannot use any built-in functions or libraries for prime number calculation, and the function should have a time complexity of O(n^2). The input range will always be positive and `start` will always be less than or equal to `end`.
"""

from typing import Tuple

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def entrance(start: int, end: int) -> Tuple[int, int]:
    count = 0
    prime_sum = 0
    
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
            prime_sum += num
    
    return count, prime_sum