"""
QUESTION:
Write a function `is_prime_sum` that takes a list of strings representing positive integers. The function should convert these strings to integers, calculate their sum, and check if the sum is a prime number. Return `True` if the sum is a prime number and `False` otherwise. The length of the input list can be up to 10^6.
"""

import math

def is_prime_sum(lst):
    total = sum(int(num) for num in lst)
    if total <= 1:
        return False
    return all(total % i != 0 for i in range(2, int(math.sqrt(total)) + 1))