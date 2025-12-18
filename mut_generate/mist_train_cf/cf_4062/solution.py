"""
QUESTION:
Create a function `is_arithmetic_progression(seq)` to determine whether a given sequence is an arithmetic progression or not. The sequence can be of any length and may contain negative numbers, gaps between elements, or repeating elements. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sequence.
"""

def is_arithmetic_progression(seq):
    if len(seq) <= 2:
        return True

    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False

    return True