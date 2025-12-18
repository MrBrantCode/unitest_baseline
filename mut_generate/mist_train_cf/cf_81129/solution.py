"""
QUESTION:
Develop a function `fibonacci_sequence(n)` that generates a Fibonacci sequence of length `n`, where `n` is a positive integer. The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it. Implement another function `golden_ratio(fib)` that calculates the approximated golden ratios from the given Fibonacci sequence `fib`. The function should return a list of ratios, each calculated by dividing a number in the sequence by its preceding number, starting from the third number.
"""

def fibonacci_sequence(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def golden_ratio(fib):
    ratios = []
    for i in range(2, len(fib)):
        ratios.append(fib[i] / fib[i-1])
    return ratios