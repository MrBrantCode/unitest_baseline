"""
QUESTION:
Develop a function named `padovan(n)` to generate the Padovan sequence up to the nth term. The Padovan sequence is defined such that each term is the sum of the two preceding ones with a shift, following the formula p(n) = p(n-2) + p(n-3). The function should return the sequence as a list of integers.
"""

def padovan(n):
    sequence = [0, 1, 1]
    if n <= 2:
        return sequence[:n+1]
    for i in range(3, n+1):
        sequence.append(sequence[i-2] + sequence[i-3])
    return sequence