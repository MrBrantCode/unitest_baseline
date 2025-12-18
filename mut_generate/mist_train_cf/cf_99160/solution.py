"""
QUESTION:
Write a function named `fibonacci_unconventional(n)` that returns the nth Fibonacci number using a combination of recursive and iterative approaches. The function should not rely on external libraries, be optimized for speed without compromising on readability, and use a multi-step, creative solution.
"""

def fibonacci_unconventional(n):
    def fibonacci(i):
        if i < 2:
            return i
        else:
            a, b = 0, 1
            for _ in range(2, i+1):
                c = a + b
                a, b = b, c
            return b

    if n < 2:
        return n
    else:
        i = 2
        while True:
            fib = fibonacci(i)
            if fib >= n:
                break
            i *= 2
        a, b = fibonacci(i-1), fibonacci(i)
        while i < n:
            c = a + b
            a, b = b, c
            i += 1
        return b