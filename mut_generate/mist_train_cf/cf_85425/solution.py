"""
QUESTION:
Write a function `fibonacci(n, seq=[0, 1])` that generates a Fibonacci sequence where the values do not exceed the given number `n`. The function should be recursive and return a list of Fibonacci numbers.
"""

def fibonacci(n, seq=[0, 1]):
    # Recursive function to generate Fibonacci sequence
    if seq[-1] <= n:
        seq.append(seq[-1] + seq[-2])
        fibonacci(n, seq)  # recursive call with updated sequence
    return seq[:-1]  # return Fibonacci numbers less than or equal to n