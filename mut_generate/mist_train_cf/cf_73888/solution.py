"""
QUESTION:
Create a function `fibonacci_pairs` that takes a list of integers as input and returns a two-dimensional array. Each sub-array should be a pair of numbers where the second number is the n-th Fibonacci number of the first number. Implement this function in a functional programming style.
"""

def fibonacci_pairs(numbers):
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

    return [[n, fibonacci(n)] for n in numbers]