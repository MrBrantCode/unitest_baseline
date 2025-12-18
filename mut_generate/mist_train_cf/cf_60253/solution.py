"""
QUESTION:
Define the function M(j) as the smallest prime number p such that p^2 is divisible by (j!)^9876543210. Then, define the function T(v) as the sum of M(j) for all j from 20 to v, inclusive. The value of T(2000) is given as 1234567890123456789. 

Write a function T(v) that calculates T(v) modulo 10^18.
"""

def T(v):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True

    def next_prime(n):
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while (not is_prime(n)):
            n += 2
        return n

    total = 0
    for j in range(20, v + 1):
        total += next_prime(j)
    return total % (10 ** 18)