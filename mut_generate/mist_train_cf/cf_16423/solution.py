"""
QUESTION:
Write a function called `fibonacci` that takes an integer `n` as input and returns a list of Fibonacci numbers up to the nth term. The function should use constant space complexity and have a time complexity of O(n).
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