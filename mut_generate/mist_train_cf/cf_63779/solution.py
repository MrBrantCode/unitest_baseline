"""
QUESTION:
Create a function `generate_sequence` that generates a sequence of numbers starting from 0, incrementing by 5, and ending at a given maximum integer value. The function should take one argument `maximum` and return the generated sequence.
"""

def generate_sequence(maximum):
    sequence = [i for i in range(0, maximum+1, 5)]
    return sequence