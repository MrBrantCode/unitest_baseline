"""
QUESTION:
Create a function named `fibonacci` that generates the nth Fibonacci number using a loop. The function should take an integer `n` as input and return the corresponding Fibonacci number. If `n` is a negative integer, the function should return -1.
"""

def fibonacci(n):
    if n < 0:
        return -1  

    elif n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        fib_n_minus_1 = 1
        fib_n_minus_2 = 0

        for i in range(2, n + 1):
            current_fib = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = current_fib

        return current_fib