"""
QUESTION:
Write a function `advanced_prime_sum(n, m)` that takes two positive integers `n` and `m` as input and returns the sum of all `n`-digit prime numbers whose digit sum is a prime number, are not divisible by 5, have an odd number of digits in them, do not contain repetitive digits, and whose cube is less than `m`.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrtn = math.isqrt(n)
    for divisor in range(3, sqrtn + 1, 2):
        if n % divisor == 0:
            return False
    return True

def contains_duplicates(s):
    return len(set(s)) != len(s)

def advanced_prime_sum(n, m):
    min_num = 10**(n-1)
    max_num = 10**n
    return sum(num for num in range(min_num, max_num) 
               if is_prime(num) and not contains_duplicates(str(num)) 
               and is_prime(sum(int(i) for i in str(num))) 
               and num % 5 != 0 and len(str(num)) % 2 != 0 and num**3 < m)