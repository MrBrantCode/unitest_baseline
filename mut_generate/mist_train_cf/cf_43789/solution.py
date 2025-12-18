"""
QUESTION:
Write a function `solve(n)` that calculates the sum of all prime integers that can be formed by taking the unique combinations of steps (from 1 to n) to ascend a staircase with n steps. The function should generate all possible stair-climbing methods, interpret these methods as integers, check if each integer is prime, and then compute the sum of these prime integers.
"""

import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    combinations = list(itertools.product(range(1, n+1), repeat=n))
    total = 0
    for combination in combinations:
        if sum(combination) == n:  
            num = int(''.join(map(str, combination)))  
            if is_prime(num):
                total += num
    return total