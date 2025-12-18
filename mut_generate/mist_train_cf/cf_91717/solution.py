"""
QUESTION:
Write a function `fibonacci(n)` that generates an array of the first `n` Fibonacci numbers without using recursion.
"""

def fibonacci(n):
    fib_nums = [0, 1]  # start with the first two Fibonacci numbers

    for i in range(2, n):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])

    return fib_nums[:n]