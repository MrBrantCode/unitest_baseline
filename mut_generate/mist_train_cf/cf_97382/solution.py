"""
QUESTION:
Design a function called `fibonacci` that takes an integer parameter `n`. The function should return a tuple containing the Fibonacci sequence up to `n` and the sum of the Fibonacci numbers up to `n`. The function should handle negative indices by returning an empty sequence and a sum of 0.
"""

def fibonacci(n):
    if n < 0:
        return [], 0
    if n == 0:
        return [0], 0
    if n == 1:
        return [0, 1], 1
    
    prev_sequence, prev_sum = fibonacci(n - 1)
    next_fibonacci = prev_sequence[-1] + prev_sequence[-2]
    next_sequence = prev_sequence + [next_fibonacci]
    next_sum = prev_sum + next_fibonacci
    
    return next_sequence, next_sum