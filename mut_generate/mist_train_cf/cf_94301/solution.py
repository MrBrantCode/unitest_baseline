"""
QUESTION:
Create a function `fibonacci(n)` that calculates the Fibonacci number at the inputted index `n` with a time complexity of O(n^2), where `n` is the inputted index. The function should handle base cases where `n` is less than or equal to 0, and return "Invalid input" in such cases.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1 or n == 2:
        return 1
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        fib[2] = 1
        for i in range(3, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]