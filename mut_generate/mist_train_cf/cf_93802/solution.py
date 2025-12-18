"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The function should handle the following constraints: 
- If `n` is negative, return the Fibonacci number with the same magnitude as `n` but with opposite sign.
- If `n` is 0 or 1, return `n`.
- For all other values of `n`, calculate the nth Fibonacci number.
- Return the result modulo 10^9 + 7.
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
    fib = [0] * (abs(n)+1)
    fib[0] = 0
    fib[1] = 1
    
    # Compute the Fibonacci sequence up to the given number
    for i in range(2, abs(n)+1):
        fib[i] = (fib[i-1] + fib[i-2]) % (10**9 + 7)
    
    if n < 0:
        return -fib[abs(n)]
    else:
        return fib[n]