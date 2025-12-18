"""
QUESTION:
Create a function `fibonacci(n)` that generates the first `n` Fibonacci numbers, raises each number to the power of 3, and returns or prints the results. The function should use a loop to calculate the Fibonacci sequence.
"""

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return [number ** 3 for number in fib]