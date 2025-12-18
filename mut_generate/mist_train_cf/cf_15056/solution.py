"""
QUESTION:
Write a function `fibonacci(index)` that calculates the Fibonacci number at the given index without using recursion. The function should handle non-negative integer indices and return the corresponding Fibonacci number.
"""

def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        fib_nums = [0, 1]
        for i in range(2, index + 1):
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        return fib_nums[index]