"""
QUESTION:
Create a recursive function `print_fibonacci_sequence(n)` that prints the Fibonacci sequence up to the nth term without using any loops or temporary variables. The Fibonacci sequence is defined as `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`, with base cases `fibonacci(0) = 0` and `fibonacci(1) = 1`.
"""

def print_fibonacci_sequence(n):
    def fibonacci(k):
        if k <= 0:
            return 0
        elif k == 1:
            return 1
        else:
            return fibonacci(k-1) + fibonacci(k-2)
    
    if n <= 0:
        return
    else:
        print_fibonacci_sequence(n-1)
        print(fibonacci(n))