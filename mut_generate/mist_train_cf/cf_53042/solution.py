"""
QUESTION:
Write a function named `print_and_sum_primes(N, M)` that takes two integers `N` and `M` as input, where `1 ≤ N < M ≤ 10^5`, and prints all prime numbers between `N` and `M` (inclusive) and returns the sum of these prime numbers. Optimize the function to achieve the best possible time complexity.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

def print_and_sum_primes(N, M):
    prime_sum = 0
    for num in range(N, M+1):
        if is_prime(num):
            print(num)
            prime_sum += num
    return prime_sum