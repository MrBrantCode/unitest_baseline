"""
QUESTION:
Write a recursive function `fibonacci_sum` that calculates the sum of the first n numbers in the Fibonacci sequence, where each number is multiplied by its corresponding index in the sequence. The function should return the sum.
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