"""
QUESTION:
Design a function `calculate_fibonacci(n)` to generate the Fibonacci sequence up to a given number `n`. The function should handle cases where `n` is negative by returning an error message, and cases where `n` is a floating-point number by rounding it to the nearest integer and calculating the Fibonacci sequence up to the rounded integer value.
"""

import math

def calculate_fibonacci(n):
    if n < 0:
        return "Error: n must be a non-negative integer."
    
    rounded_n = round(n)
    
    fibonacci_sequence = []
    
    if rounded_n == 0:
        fibonacci_sequence.append(0)
    elif rounded_n == 1:
        fibonacci_sequence.extend([0, 1])
    else:
        a, b = 0, 1
        fibonacci_sequence.extend([0, 1])
        
        for i in range(2, rounded_n + 1):
            next_fibonacci = a + b
            fibonacci_sequence.append(next_fibonacci)
            a, b = b, next_fibonacci
    
    return fibonacci_sequence