"""
QUESTION:
Create a function named `fibonacci` that generates the Fibonacci sequence up to the nth position, where n is a user-provided positive integer. The function should handle cases for n <= 0, n == 1, and n == 2 correctly. Optimize the function to efficiently handle large values of n by minimizing redundant calculations.
"""

def fibonacci(n): 
    if n <= 0: 
        return []
    elif n == 1: 
        return [0]
    elif n == 2: 
        return [0, 1]
    else: 
        fib = [0, 1] + [0] * (n - 2)

        for i in range(2, n):
            fib[i] = fib[i - 2] + fib[i - 1]
        
        return fib[:n]  