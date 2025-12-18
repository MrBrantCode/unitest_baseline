"""
QUESTION:
Create a function `fibonacci` that takes two parameters: an integer `n` and a dictionary `cache`. The function should return the nth Fibonacci number. 

The function should handle negative values of `n` by returning the Fibonacci number with the same magnitude as `n` but with opposite sign. The function should also return the result modulo 10^9 + 7.

Before calculating a new Fibonacci number, the function should check if it exists in the cache. If it does, return the value from the cache instead of recalculating it. If it doesn't exist, calculate the Fibonacci number and add it to the cache before returning the value.

Restrictions: `n` must be greater than or equal to -1,000,000 and less than or equal to 1,000,000.
"""

def fibonacci(n, cache):
    if n in cache:
        return cache[n]
    
    if n == 0:
        cache[0] = 0
        return 0
    elif n == 1:
        cache[1] = 1
        return 1
    
    sign = 1 if n > 0 else -1
    n = abs(n)
    
    fib_minus_2 = 0
    fib_minus_1 = 1
    
    for i in range(2, n+1):
        fib = (fib_minus_2 + fib_minus_1) % (10**9 + 7)
        cache[i] = fib
        
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
    
    return fib * sign