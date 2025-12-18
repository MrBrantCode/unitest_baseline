"""
QUESTION:
Create a function `is_arithmetic_progression(seq)` that takes a sequence of numbers as input and returns `True` if the sequence is an arithmetic progression and `False` otherwise. The sequence can have negative numbers, gaps between elements, and repeating elements. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def is_arithmetic_progression(seq):
    if len(seq) <= 2:
        return True

    diff = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if seq[i] - seq[i-1] != diff:
            return False

    return True