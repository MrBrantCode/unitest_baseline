"""
QUESTION:
Write a function `generate_fibonacci` that generates a Fibonacci sequence. The function should take one argument, `n`, which is the number of elements in the sequence. The sequence should start with 0 and 1, and each subsequent element should be the sum of the previous two elements.
"""

def generate_fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence