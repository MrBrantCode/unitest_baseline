"""
QUESTION:
Find the nth prime number in ascending order using a function named `find_nth_prime(n)` that has a time complexity of O(n^2) and only uses O(1) space.
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