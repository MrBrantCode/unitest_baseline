"""
QUESTION:
Create a function `fibonacci_sum` that takes an integer `n` as input and returns the sum of the Fibonacci sequence up to the nth number. The function should have a time complexity of O(n) and should not use recursion.
"""

def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib_sum = 1
    fib_prev = 1

    for i in range(2, n):
        fib_next = fib_sum + fib_prev
        fib_sum += fib_next
        fib_prev = fib_next

    return fib_sum