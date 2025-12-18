"""
QUESTION:
Implement a function `count_digit_only_primes(n)` that takes an integer `n` where 1 <= n <= 10^9 and returns the total number of digit-only divisors of `n` that are also prime numbers. A digit-only divisor is defined as a divisor of `n` that only consists of the digits present in `n`.
"""

import math

def count_digit_only_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    digits = set(str(n))
    count = 0
    for i in range(1, n+1):
        if n % i == 0 and is_prime(i) and set(str(i)).issubset(digits):
            count += 1
    return count