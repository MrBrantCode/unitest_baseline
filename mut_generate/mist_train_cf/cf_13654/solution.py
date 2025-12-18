"""
QUESTION:
Create a function `fibonacci(n)` that calculates the nth Fibonacci number. The function should accept a positive integer `n` and return the corresponding Fibonacci number. The solution must have a time complexity of O(n) and a space complexity of O(1).
"""

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    prev_1 = 0
    prev_2 = 1
    fib_num = 0

    for _ in range(3, n + 1):
        fib_num = prev_1 + prev_2
        prev_1, prev_2 = prev_2, fib_num

    return fib_num