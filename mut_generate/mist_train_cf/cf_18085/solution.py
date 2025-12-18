"""
QUESTION:
Write a function called `fibonacci(n)` that generates an array of the first `n` Fibonacci numbers without using recursion, with a time complexity of O(n). The function should start with the first two Fibonacci numbers, 0 and 1, and then iteratively calculate the next Fibonacci number by summing the previous two numbers.
"""

def fibonacci(n):
    # Create an array to store Fibonacci numbers
    fib_nums = [0, 1]

    # Calculate and store Fibonacci numbers
    for i in range(2, n):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])

    return fib_nums