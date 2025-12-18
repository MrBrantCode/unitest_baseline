"""
QUESTION:
Implement a function named `is_arithmetic_sequence(sequence)` that takes a list of numbers as input and returns a boolean indicating whether the input sequence is an arithmetic sequence, i.e., a sequence of numbers such that the difference between any two successive members is constant.
"""

def is_arithmetic_sequence(sequence):
    if len(sequence) < 2:
        return True
    diff = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i-1] != diff:
            return False
    return True