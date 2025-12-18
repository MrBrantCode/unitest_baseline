"""
QUESTION:
Design a function called `generate_fibonacci(n)` that takes an integer `n` as input and returns a list of the first `n` Fibonacci numbers. The function should implement a multi-step logic where each Fibonacci number is calculated as the sum of the previous two numbers.
"""

def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib = [0, 1]
    
    # Multi-step logic: Sum up the last two Fibonacci numbers and append to the sequence
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return fib[:n]