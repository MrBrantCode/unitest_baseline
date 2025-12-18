"""
QUESTION:
Write a function `fibonacci(n)` that generates the first n terms of the Fibonacci sequence using dynamic programming and returns the sequence along with its sum, given that n is a prime number and n > 0. The function should not take any other input besides n.
"""

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib = [0, 1]  # Store Fibonacci sequence
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return [fib, sum(fib)]