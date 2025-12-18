"""
QUESTION:
Implement a function `compute_factorial(n)` to calculate the factorial of a given number `n` using a loop, without recursion. The function should return the computed factorial.
"""

def compute_factorial(n):
    if n == 0:
        return 1

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial