"""
QUESTION:
Design an algorithm to identify and display all prime quadruplets within a specified range. A prime quadruplet is a set of four prime numbers of the form (p, p+2, p+6, p+8) where p is a prime number and p+2, p+6, and p+8 are also prime numbers. Additionally, the numbers in between these prime numbers (p+1, p+3, p+5, p+7) should not be prime. The algorithm should be efficient in terms of time and space complexity.

The function should be named `find_quadruplets` and take two parameters: `lower` and `upper`, representing the range of numbers to search for prime quadruplets. The function should print all prime quadruplets found in the range. 

The solution should be written in Python and should use an optimized approach to check for primality.
"""

from math import sqrt

def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    square_root = int(sqrt(n)) + 1
    for f in range(5, square_root, 6):
        if n % f == 0 or n % (f + 2) == 0: return False
    return True

def find_quadruplets(lower, upper):
    for i in range(lower, upper-8):
        if is_prime(i) and is_prime(i+2) and is_prime(i+6) and is_prime(i+8):
            if not is_prime(i+1) and not is_prime(i+3) and not is_prime(i+5) and not is_prime(i+7):
                print([i, i+2, i+6, i+8])