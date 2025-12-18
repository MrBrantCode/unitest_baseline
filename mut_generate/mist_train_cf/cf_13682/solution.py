"""
QUESTION:
Write a function `is_arithmetic_sequence(sequence)` that checks if the given sequence is an arithmetic sequence with a time complexity of O(n) and a space complexity of O(1). The sequence can contain negative numbers and has a length of up to 10^6.
"""

def is_arithmetic_sequence(sequence):
    if len(sequence) < 2:
        return True

    difference = sequence[1] - sequence[0]

    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i-1] != difference:
            return False

    return True