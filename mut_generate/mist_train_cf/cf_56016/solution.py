"""
QUESTION:
Write a function `tribonacci(n)` that returns the nth number in the Tribonacci sequence, where the sequence starts with [0, 0, 1] and each subsequent number is the sum of the previous three numbers.
"""

def tribonacci(n):
    sequence = [0, 0, 1]
    while len(sequence) < n + 1:
        sequence.append(sum(sequence[-3:]))
    return sequence[n]