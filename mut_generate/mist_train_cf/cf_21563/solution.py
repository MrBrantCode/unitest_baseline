"""
QUESTION:
Create a function called `fibonacci` that generates the first n Fibonacci numbers with a time complexity of O(n).
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n-1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence