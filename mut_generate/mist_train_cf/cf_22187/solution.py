"""
QUESTION:
Write a function `prime_sum_pairs(n)` that takes an integer `n` as input and prints all pairs of numbers `(i, j)` where `1 ≤ i ≤ n` and `1 ≤ j ≤ n`, such that `i + j` is a prime number. The function should use nested for loops and have a time complexity of O(n^2).
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum_pairs(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if is_prime(i+j):
                print(f"({i}, {j})")