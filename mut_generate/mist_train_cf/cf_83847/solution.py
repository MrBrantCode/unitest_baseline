"""
QUESTION:
Design a function `Fibonacci_Recursive(n)` that takes a non-negative integer `n` as input and returns the nth Fibonacci number using recursion. The function should handle the base cases where `n` equals 0 or 1 and return 0 or 1, respectively. For `n` greater than 1, the function should return the sum of the Fibonacci numbers of `n-1` and `n-2`.
"""

def Fibonacci_Recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursive(n-1) + Fibonacci_Recursive(n-2)