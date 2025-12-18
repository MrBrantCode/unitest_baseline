"""
QUESTION:
Create a function called `fibonacci(n)` that takes a positive integer `n` (n ≥ 1) as input and returns the nth term in the Fibonacci sequence, where each term is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list[n-1]