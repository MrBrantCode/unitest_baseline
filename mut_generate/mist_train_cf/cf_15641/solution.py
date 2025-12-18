"""
QUESTION:
Write a function `fibonacci_sum(n)` that calculates the sum of the first n Fibonacci numbers using recursion. The function should only accept positive integers as input and return the sum. The implementation should have a time complexity of O(n) without using any additional data structures or variables other than the input and return variables.
"""

def fibonacci_sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    return sum([fibonacci(i) for i in range(n+1)])