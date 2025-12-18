"""
QUESTION:
Create a function named `fibonacci_series` that takes an integer `n` as input and returns an array containing the Fibonacci series up to the nth element. The function should handle cases where `n` is less than or equal to 0 by returning an error message, and it should return the first two elements `[0, 1]` when `n` is 2. For `n` greater than 2, the function should generate the Fibonacci series up to the nth element.
"""

def fibonacci_series(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq