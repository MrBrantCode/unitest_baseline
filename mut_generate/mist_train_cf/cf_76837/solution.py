"""
QUESTION:
Write a function `fibonacci(n, m, fib_1=0, fib_2=1)` that recursively prints all Fibonacci numbers within the range from `n` to `m` (inclusive), where `n` and `m` are the lower and upper limits respectively.
"""

def fibonacci(n, m, fib_1=0, fib_2=1):
    if m < n:
        return
    if fib_1 == 0:
        print(fib_1)
        print(fib_2)
    fib_3 = fib_1 + fib_2
    if fib_3 <= m:
        print(fib_3)
        fibonacci(n, m, fib_2, fib_3)