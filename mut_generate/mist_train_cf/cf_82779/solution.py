"""
QUESTION:
Design a function named `generate_lucas_sequence` that generates the Lucas sequence up to a given integer `n`. The Lucas sequence is defined as a series of numbers where the first two numbers are 2 and 1, and each subsequent number is the sum of the previous two. The function should return an array of Lucas sequence values where the last value is less than or equal to `n`. If `n` is less than 1, the function should return an empty array.
"""

def generate_lucas_sequence(n):
    if n < 1:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]
    else:
        sequence = [2, 1]
        while sequence[-1] + sequence[-2] <= n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence