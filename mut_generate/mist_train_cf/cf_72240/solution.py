"""
QUESTION:
Create a function `Fibonacci(n)` that generates a list of Fibonacci sequence up to the `n`-th term using recursive method. The function should return a list of integers. Note that the recursive method may not be the most efficient way for large values of `n`.
"""

def Fibonacci(n):
    def Fibonacci_helper(k):
        if k <= 0:
            return 0
        elif k == 1:
            return 1
        else:
            return Fibonacci_helper(k-1) + Fibonacci_helper(k-2)

    fib_sequence = []
    for i in range(n):
        fib_sequence.append(Fibonacci_helper(i))
    return fib_sequence