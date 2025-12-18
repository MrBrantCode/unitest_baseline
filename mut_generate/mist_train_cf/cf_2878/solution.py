"""
QUESTION:
Write a function `convert_to_hex_sorted` that takes a list of integers as input, converts each integer into its hexadecimal representation (padding with zeros to ensure a minimum length of 4 digits), checks if the hexadecimal number is both prime and a perfect square, and returns a sorted list of such numbers in ascending order.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return math.isqrt(n)**2 == n

def convert_to_hex_sorted(nums):
    hex_list = []
    for num in nums:
        hex_num = hex(num)[2:].zfill(4)
        if is_prime(int(hex_num, 16)) and is_perfect_square(int(hex_num, 16)):
            hex_list.append(hex_num)
    return sorted(hex_list)