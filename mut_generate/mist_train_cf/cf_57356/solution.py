"""
QUESTION:
Create a function called `fibonacci` that takes an integer `n` as a parameter and returns a list of the first `n` Fibonacci numbers. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1. If `n` is less than or equal to 0, the function should return an empty list.
"""

def fibonacci(n): 
    a, b = 0, 1
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]

    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)

    return sequence