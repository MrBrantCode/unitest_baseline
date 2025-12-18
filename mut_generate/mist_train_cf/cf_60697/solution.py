"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth position, where the sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should return a list of integers. The input `n` is a positive integer greater than or equal to 1, representing the position up to which to generate the Fibonacci sequence.
"""

def fibonacci(n):
    fib_seq = [0, 1]  # starting two numbers of the Fibonacci sequence
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])  # add the sum of the last two numbers to the sequence
    return fib_seq