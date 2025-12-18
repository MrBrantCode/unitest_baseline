"""
QUESTION:
Implement a function `fibonacci(n)` to compute the Fibonacci series value at the specified position `n`. The function should use the iterative solution when `n` is even and the recursive solution when `n` is odd. The function should be able to handle edge cases such as `n = 0, 1`, and larger numbers.
"""

def fibonacci(n):
    def fibonacci_iterative(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n+1):
                fib.append(fib[i-1] + fib[i-2])
            return fib[n]

    def fibonacci_recursive(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

    if n % 2 == 0:
        return fibonacci_iterative(n)
    else:
        return fibonacci_recursive(n)