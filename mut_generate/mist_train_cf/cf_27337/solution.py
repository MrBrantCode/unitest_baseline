"""
QUESTION:
Implement a function `factorial_recursive(n)` that takes a non-negative integer `n` as input and returns its factorial using recursion. The function should handle the base case where `n` is 0. The function should not use loops or iterative methods.
"""

def entrance(n: int) -> int:
    if n == 0:  
        return 1
    else:
        return n * entrance(n - 1) 