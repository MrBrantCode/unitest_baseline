"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using a recursive algorithm without any additional variables or data structures. The function must have a time complexity of O(n) and a space complexity of O(1). The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
"""

def fibonacci(n):
    def fib_helper(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        return fib_helper(x-1) + fib_helper(x-2)

    memo = {0: 0, 1: 1}
    def fib_helper_memo(x):
        if x not in memo:
            memo[x] = fib_helper_memo(x-1) + fib_helper_memo(x-2)
        return memo[x]
    
    return fib_helper_memo(n)