"""
QUESTION:
Create a function named `Fibonacci` that takes a positive integer `n` and returns the first `n` numbers in the Fibonacci sequence. The function should be efficient for large values of `n` and handle the case when `n` is less than 1.
"""

def Fibonacci(n):
    if n < 1:
        return "Incorrect input --- Please enter a valid positive integer"
    elif n == 1:
        return [0]
    elif n == 2: 
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib