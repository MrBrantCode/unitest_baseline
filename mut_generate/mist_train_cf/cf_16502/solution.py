"""
QUESTION:
Create a function named `fibonacci_odd` that generates and returns a list of odd Fibonacci numbers up to the nth number in the sequence, using a recursive approach with a maximum recursion depth of 100.
"""

def fibonacci_odd(n):
    def fibonacci(i):
        if i <= 1:
            return i
        return fibonacci(i-1) + fibonacci(i-2)
    
    result = []
    for i in range(n+1):
        fib = fibonacci(i)
        if fib % 2 != 0:
            result.append(fib)
    return result