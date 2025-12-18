"""
QUESTION:
Write a function named `print_nth_prime` that prints the nth prime number in ascending order. The function should use O(1) space and have a time complexity of O(n^3). The function takes one argument `n`, which is the position of the prime number to be printed.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def entance(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1