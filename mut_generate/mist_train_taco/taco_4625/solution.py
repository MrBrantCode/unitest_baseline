"""
QUESTION:
a number can be said dual prime. if the number is prime and the sum of digits of the number is also a prime number.
If a number is dual prime then print YES else print NO

SAMPLE INPUT
2
13
11

SAMPLE OUTPUT
NO
YES
"""

import math

def prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif not n & 1:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

def is_dual_prime(n):
    if not prime(n):
        return "NO"
    
    sum_of_digits = sum(int(digit) for digit in str(n))
    
    if prime(sum_of_digits):
        return "YES"
    else:
        return "NO"