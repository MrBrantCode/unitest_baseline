"""
QUESTION:
Write a recursive function `fibonacci` that takes an integer `n` as input and returns the n-th Fibonacci number without using memoization. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. Analyze the time complexity of your solution and explain your answer.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)