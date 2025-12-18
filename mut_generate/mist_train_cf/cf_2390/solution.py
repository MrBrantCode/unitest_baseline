"""
QUESTION:
Create a function `nth_prime_fibonacci(n)` that prints the Nth prime Fibonacci number. The function should handle N up to 1000, have a time complexity of O(N log N) or better, and use a space complexity of O(1) or O(log N). The function should also utilize a prime number generator with a time complexity of O(N log log N) or better.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime_fibonacci(n):
    if n == 1:
        return 2
    if n == 2:
        return 3

    count = 2
    i = 3
    j = 2
    while count < n:
        temp = i
        i += j
        j = temp

        if is_prime(i):
            count += 1

    return i