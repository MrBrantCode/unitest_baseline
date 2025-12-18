"""
QUESTION:
Implement a function named `fibonacci_sum` that calculates the sum of the first `n` numbers in the Fibonacci sequence where each number is multiplied by its corresponding 1-based index, using a recursive algorithm. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def fibonacci_sum(index):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    if index <= 0:
        return 0
    else:
        fib_num = fibonacci(index)
        return (fib_num * index) + fibonacci_sum(index - 1)