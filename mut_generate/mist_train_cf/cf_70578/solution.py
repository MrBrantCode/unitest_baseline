"""
QUESTION:
Generate a function named `lucas_sequence` that takes an integer `n` as input and returns a list of the first `n` Lucas numbers. The Lucas numbers are a sequence where each element is the sum of the two preceding elements, starting with 2 and 1.
"""

def lucas(n):
    """Return first n elements of Lucas numbers sequence."""
    if n == 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]
    else:
        sequence = [2, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence