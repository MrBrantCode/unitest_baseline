"""
QUESTION:
Construct a function `fibonacci(n)` that generates a Fibonacci sequence with `n` terms. The sequence should start with 0 and 1, and each subsequent term is the sum of the previous two terms. If a term exceeds 1000, the sequence should restart from the initial pair of 0 and 1.
"""

def fibonacci(n):
    sequence = []  
    a, b = 0, 1

    while len(sequence) < n:
        sequence.append(b)
        a, b = b, a + b
        if b > 1000: 
            a, b = 0, 1
            
    return sequence