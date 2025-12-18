"""
QUESTION:
Create a function named `fibonacci` that takes an integer `index` as input and returns the Fibonacci number at that index. The function should not use recursion. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should handle indices 0 and 1 as base cases.
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