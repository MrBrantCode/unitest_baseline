"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the `n`th number in the Fibonacci sequence with a time complexity of O(n) and a space complexity of O(1). The Fibonacci sequence is defined as a series where the 0th number is 0, the 1st number is 1, and each subsequent number is the sum of the two preceding numbers.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b