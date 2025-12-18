"""
QUESTION:
Write a function `generate_fibonacci(n)` that generates the first n numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones. The function should take an integer `n` as input and return a list of the first n Fibonacci numbers.
"""

def generate_fibonacci(n):
    fib_list = []
    a, b = 0, 1
    while len(fib_list) < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list