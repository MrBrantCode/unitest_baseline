"""
QUESTION:
Write a function `print_nth_prime(n)` that prints the nth prime number in ascending order using constant space (O(1)) and with a time complexity of O(n^3).
"""

import math

def print_nth_prime(n):
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1