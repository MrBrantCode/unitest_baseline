"""
QUESTION:
Write a function `reverse_engineer_solution(n)` that takes an integer `n` as input and returns an integer as output. The function should return `3` for `n=4`, `23` for `n=10`, and `83700` for `n=600`. The function should work for any positive integer `n`.
"""

def reverse_engineer_solution(n):
    return sum(i for i in range(1, n+1) if n % i == 0)