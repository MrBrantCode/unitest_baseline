"""
QUESTION:
Create a function called "fibonacci" that takes two parameters: an integer "n" and a dictionary "cache". The function should return the nth Fibonacci number, where n can be any integer. If n is negative, the function should return the Fibonacci number with the same magnitude as n but with opposite sign. The function should return the result modulo 10^9 + 7. The function should use the cache to store previously calculated Fibonacci numbers and return the value from the cache if it exists, instead of recalculating it.
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