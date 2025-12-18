"""
QUESTION:
Construct a function named `pattern(n)` that generates a string pattern based on the Fibonacci sequence. The function should take an integer `n` as input, representing the number of Fibonacci sequence numbers to include in the pattern. The pattern is formed by concatenating the Fibonacci numbers in sequence. The function should return the resulting string pattern.
"""

def pattern(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return ''.join(map(str, fib))