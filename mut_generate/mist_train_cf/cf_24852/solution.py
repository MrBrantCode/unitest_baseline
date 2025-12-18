"""
QUESTION:
Write a function `fibonacci(n)` that generates a Fibonacci sequence up to the nth number. The function should take an integer `n` as input and return a list of Fibonacci numbers, where `n` represents the length of the sequence. The function should handle cases where `n` is less than or equal to 0, returning `None` in such cases.
"""

def fibonacci(n):
    if n <= 0:
        return None 
    
    first = 0
    second = 1
    sequence = [first, second]
    for i in range(2, n):
        next_term = first + second
        sequence.append(next_term)
        first = second
        second = next_term
    return sequence