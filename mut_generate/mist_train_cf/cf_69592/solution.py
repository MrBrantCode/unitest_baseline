"""
QUESTION:
Create a function `fibonacci_sequence(n)` that generates the Fibonacci sequence up to the nth number and returns it as a string where the numbers are 'fused' together. The Fibonacci sequence is defined by the numerical relationship where each subsequent number is the sum of the two preceding ones. The input parameter `n` is a positive integer and represents the length of the Fibonacci sequence to be generated.
"""

def fibonacci_sequence(n):
    fib = [1, 1]
    sequence = '11'
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
        sequence += str(fib[-1])
    return sequence