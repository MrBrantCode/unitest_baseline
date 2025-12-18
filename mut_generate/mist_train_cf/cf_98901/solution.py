"""
QUESTION:
Write a function named `fibonacci` that generates the nth number in the Fibonacci sequence. The function should implement a tail-recursive approach. If `n` is less than or equal to 1, return `n`, else return the sum of the two preceding numbers.
"""

def fibonacci(n):
    def fib_helper(a, b, count):
        if count == 0:
            return a
        else:
            return fib_helper(b, a + b, count - 1)
    return fib_helper(0, 1, n)