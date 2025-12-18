"""
QUESTION:
Write a function called `fibonacci_recursive` that takes an integer `n` as input and returns the Fibonacci sequence up to the nth number using recursion. The function should return a list of integers representing the Fibonacci sequence. If `n` is less than or equal to 0, the function should return an empty list.
"""

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n-1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq