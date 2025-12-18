"""
QUESTION:
Implement the `fibonacci` function that uses dynamic programming and tabulation to compute the nth Fibonacci number. The function should take an integer `n` as input and return the corresponding Fibonacci number. Use an array to store already computed results and avoid multiple computations of the same values.
"""

def fibonacci(n):
    fib_values = [0, 1]

    while len(fib_values) < n + 1:
        fib_values.append(0)

    if n <= 1:
        return n
    else:
        if fib_values[n - 1] == 0:
            fib_values[n - 1] = fibonacci(n - 1)

        if fib_values[n - 2] == 0:
            fib_values[n - 2] = fibonacci(n - 2)

    fib_values[n] = fib_values[n - 2] + fib_values[n - 1]
    return fib_values[n]