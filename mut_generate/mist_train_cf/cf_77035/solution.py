"""
QUESTION:
Create a function named `fibonacci_in_list` that takes a list of integers as input and returns a new list containing only the Fibonacci numbers from the input list. A Fibonacci number is a number in the sequence where a number is the addition of the last two numbers, usually starting with 0 and 1.
"""

def fibonacci_in_list(nums):
    def is_fib(n):
        if n < 2:
            return True
        a, b = 0, 1
        while a <= n:
            if a == n:
                return True
            a, b = b, a + b
        return False

    return [n for n in nums if is_fib(n)]