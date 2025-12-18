"""
QUESTION:
Write a function named `fibonacci` that generates an array of the first `n` Fibonacci numbers. The function should not use recursion. The output array should contain the first `n` numbers in the Fibonacci sequence.
"""

def fibonacci(n):
    fib_nums = [0, 1]  

    for i in range(2, n):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])

    return fib_nums[:n]