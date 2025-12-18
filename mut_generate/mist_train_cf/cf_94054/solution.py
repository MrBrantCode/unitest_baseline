"""
QUESTION:
Design a function `calculate_fibonacci(n)` to calculate the Fibonacci sequence up to the nth number. If n is negative, return an error message. If n is a floating-point number, round it to the nearest integer and calculate the Fibonacci sequence up to that rounded integer value.
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