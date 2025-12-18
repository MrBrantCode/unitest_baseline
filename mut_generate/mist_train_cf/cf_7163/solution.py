"""
QUESTION:
Write a function named `fibonacci_sum` that generates the Fibonacci sequence up to a given number `n` and calculates the sum of all the Fibonacci numbers up to `n`. The function should not use recursion and have a time complexity of O(n).
"""

def fibonacci_sum(n):
    fib_seq = [0, 1]
    fib_sum = 1
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        fib_sum += fib_seq[-1]
    return fib_sum