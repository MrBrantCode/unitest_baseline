"""
QUESTION:
Given a positive integer n, create an array a with length n^3 consisting of integers. For each i (1 ≤ i ≤ n^3), set a[i] = (i * nth_prime(i) - 1 + (i % nth_prime(i)). Compute the result for all potential tuples (a[i], a[j], a[k], a[l], a[m]): (a[i] * a[j] * a[k] * a[l]) % a[m]. Return the count of tuples where i < j < k < l < m, and the outcome is a prime number. 

Note that you need to create your own functions for nth_prime and is_prime number generation. The code should be able to handle a given n and return the result, however, be aware that the execution time may be high due to the complexity of the problem.
"""

import math
from itertools import combinations

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, math.isqrt(n)+1, 2):
        if n%i == 0:
            return False
    return True

def nth_prime(n):
    count, num = 0, 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def entrance(n):
    N = n ** 3
    a = [(i * nth_prime(i) - 1 + (i % nth_prime(i))) for i in range(1, N+1)]
    return sum(1 for a_tuple in combinations(a, 5) if is_prime((a_tuple[0] * a_tuple[1] * a_tuple[2] * a_tuple[3]) % a_tuple[4]) )