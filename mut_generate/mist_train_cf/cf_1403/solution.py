"""
QUESTION:
Create a recursive function `fibonacci_sum` that calculates the sum of the Fibonacci sequence up to the nth term, excluding any term that is divisible by both 5 and 3. The function should take an integer `n` as input and return the sum.
"""

def fibonacci_sum(n):
    a, b = 0, 1
    sum = 0
    for _ in range(n):
        if a % 5 != 0 or a % 3 != 0:
            sum += a
        a, b = b, a + b
    return sum