"""
QUESTION:
Create a function named `fibonacci(n)` that calculates the nth Fibonacci number, where `n` is an integer in the range -1,000,000 to 1,000,000. The function should return the Fibonacci number with the same magnitude as `n` but with opposite sign for negative `n`, and return the result modulo 10^9 + 7.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        sign = -1 if n % 2 == 0 else 1
        return sign * fibonacci(abs(n))
    
    # Initialize the Fibonacci sequence
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1
    
    # Compute the Fibonacci sequence up to the given number
    for i in range(2, n+1):
        fib[i] = (fib[i-1] + fib[i-2]) % (10**9 + 7)
    
    return fib[n]