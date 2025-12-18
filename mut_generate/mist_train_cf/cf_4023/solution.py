"""
QUESTION:
Write a function `fibonacci(n)` that prints Fibonacci numbers up to `n` (where `n > 1`) with a time complexity of O(N) and constant space complexity. The function should handle `n` values up to 10^6 and print the numbers modulo 10^9+7.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append((fib[i-1] + fib[i-2]) % (10**9 + 7))
    
    return fib