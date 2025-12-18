"""
QUESTION:
Write a function `modified_fib(n, start1, start2)` that generates a Fibonacci series of length `n` starting from `start1` and `start2`. The function should return a list of integers representing the Fibonacci series. The function should handle cases where `n` is less than or equal to 0, and should run efficiently for large inputs.
"""

def modified_fib(n, start1, start2):
    if n <= 0:
        return []
    elif n == 1:
        return [start1]
    else:
        fib_seq = [start1, start2]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-2] + fib_seq[i-1])
        return fib_seq