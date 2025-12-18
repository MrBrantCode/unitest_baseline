"""
QUESTION:
Design a function `modified_fibonacci(n, memo={})` to calculate the nth number in a modified Fibonacci sequence where each number is the sum of the previous three numbers. Implement the function using recursion and memoization. The function should handle inputs where n is an integer greater than or equal to 0.
"""

def modified_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        res = modified_fibonacci(n - 1, memo) + modified_fibonacci(n - 2, memo) + modified_fibonacci(n - 3, memo)
        memo[n] = res
        return res