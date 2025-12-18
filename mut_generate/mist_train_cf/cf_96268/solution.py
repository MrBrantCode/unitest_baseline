"""
QUESTION:
Write a function `find_nth_prime(n)` that finds the nth prime number in ascending order. The function should use O(1) space and have a time complexity of O(n^2). The input `n` is a positive integer representing the position of the prime number to be found.
"""

import math

def find_nth_prime(n):
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

        num += 1

    return num - 1