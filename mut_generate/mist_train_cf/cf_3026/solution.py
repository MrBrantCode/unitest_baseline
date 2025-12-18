"""
QUESTION:
Implement a function `lcm(a, b)` to find the least common multiple (LCM) of two positive integers `a` and `b` using the prime factorization method with a time complexity of O(log(min(a, b))) or better.
"""

import math

def lcm(a, b):
    lcm = 1
    for i in range(2, int(math.sqrt(min(a, b))) + 1):
        while a % i == 0 and b % i == 0:
            a //= i
            b //= i
            lcm *= i
    if a != b:
        lcm *= a * b
    else:
        lcm *= a
    return lcm