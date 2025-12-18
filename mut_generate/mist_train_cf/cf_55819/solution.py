"""
QUESTION:
Create a function named `generate_sequence` that generates the first `n` terms of the triangular number sequence, where the `n-th` triangular number is given by the formula `n*(n+1)/2`. The function should return a list of integers. The input `n` is a positive integer and the function should be able to handle `n` up to 20.
"""

def generate_sequence(n):
    seq = []
    for i in range(1, n+1):
        seq.append(int(i*(i+1)/2))
    return seq