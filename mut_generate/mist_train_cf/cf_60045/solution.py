"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the `n`-th Fibonacci number. The function should be able to handle both positive and negative integers efficiently. If `n` is negative, the function should use the negaFibonacci rules: Fib(-n) = -Fib(n) if n is odd, and Fib(-n) = Fib(n) if n is even.
"""

def fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    
    If n is negative, the function uses the negaFibonacci rules:
    Fib(-n) = -Fib(n) if n is odd, and Fib(-n) = Fib(n) if n is even.
    
    This function uses memoization to efficiently calculate Fibonacci numbers.
    """
    
    cache = {0: 0, 1: 1}
    
    def fib(n):
        if n not in cache:
            if n < 0:
                if n % 2 == 0:
                    cache[n] = fib(-n)
                else:
                    cache[n] = -fib(-n)
            else:
                cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    
    return fib(n)