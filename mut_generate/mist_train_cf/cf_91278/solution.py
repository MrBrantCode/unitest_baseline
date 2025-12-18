"""
QUESTION:
Compute the Fibonacci sequence up to n, where n is a positive integer less than or equal to 1000. The solution should have a time complexity of O(n) and a space complexity of O(1). Implement the `fibonacci(n)` function to return the Fibonacci sequence as a list of integers.
"""

def fibonacci(n):
    if n <= 0:
        return []

    fib_seq = [0] * n
    fib_seq[0] = 0
    if n > 1:
        fib_seq[1] = 1

    for i in range(2, n):
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2]

    return fib_seq