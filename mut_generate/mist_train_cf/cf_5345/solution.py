"""
QUESTION:
Create a function called `fibonacci` that takes a positive integer `n` (n >= 2) as input and returns a list of the first `n` numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones. The sequence should start with 0 and 1. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq