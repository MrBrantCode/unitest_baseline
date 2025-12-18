"""
QUESTION:
Implement the `calculateFibonacci` function, which takes an integer `n` as input and returns the `n`th Fibonacci number using an iterative approach. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. The function should handle all non-negative integers `n`.
"""

def calculateFibonacci(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr