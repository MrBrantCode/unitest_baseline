"""
QUESTION:
Write a function `fibonacci(n)` that prints and returns a list of Fibonacci numbers up to the nth number, generated using a recursive function with memoization. The function should take an integer `n` as input and return a list of integers. Implement the solution using a recursive helper function with memoization to improve efficiency.
"""

def fibonacci(n, mem = {}):
    if n in mem:
        return mem[n]
    if n == 1 or n == 0:
        return n
    else:
        result = fibonacci(n - 1, mem) + fibonacci(n - 2, mem)
        mem[n] = result
        return result

def entrance(n):
    return [fibonacci(i) for i in range(n)]