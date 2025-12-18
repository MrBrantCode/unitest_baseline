"""
QUESTION:
Create a function named `fibonacci(n)` to calculate the Fibonacci series up to `n` numbers. The function should be able to handle large inputs efficiently. It should take an integer `n` as input and return a list of integers representing the Fibonacci series up to `n` numbers. If `n` is less than 1, the function should print an error message and return.
"""

def fibonacci(n):
    if n < 1:
        print("Incorrect input")
        return
    
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
        
    return fib_series