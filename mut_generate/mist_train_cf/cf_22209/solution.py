"""
QUESTION:
Write a function named `tribonacci_sequence` that generates a sequence of n numbers where each number is the sum of the previous four numbers. The first four numbers should be 0.
"""

def tribonacci_sequence(n):
    sequence = [0] * 4
    for i in range(4, n):
        sequence.append(sum(sequence[-4:]))
    return sequence[:n]