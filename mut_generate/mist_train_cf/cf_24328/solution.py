"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns an array of the first `n` numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n > 2:
        fib_nums = [0, 1]
        for i in range(2, n):
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        return fib_nums