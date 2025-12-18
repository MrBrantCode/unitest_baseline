"""
QUESTION:
Create a function named `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence iteratively using a loop, without recursion. The function should take an integer `n` as input and return a list of the Fibonacci sequence.
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
        while len(fib_sequence) < n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence