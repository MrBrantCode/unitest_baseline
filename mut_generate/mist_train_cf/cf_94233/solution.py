"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth term using constant space complexity and O(n) time complexity. The function should take an integer `n` as input and return a list containing the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        a, b = 0, 1
        for i in range(2, n):
            fib = a + b
            fib_sequence.append(fib)
            a, b = b, fib
        return fib_sequence