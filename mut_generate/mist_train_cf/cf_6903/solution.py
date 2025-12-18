"""
QUESTION:
Write a function `is_arithmetic_sequence` that checks if a given sequence is a strictly increasing or decreasing arithmetic sequence. The sequence can have a length of up to 10^18, a common difference of up to 10^9, and may contain negative numbers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the sequence.
"""

def is_arithmetic_sequence(seq):
    """
    Checks if a given sequence is a strictly increasing or decreasing arithmetic sequence.

    Args:
    seq (list): The input sequence to check.

    Returns:
    bool: True if the sequence is a strictly increasing or decreasing arithmetic sequence, False otherwise.
    """
    n = len(seq)
    if n <= 1:
        return True
    diff = seq[1] - seq[0]
    for i in range(1, n - 1):
        if seq[i + 1] - seq[i] != diff:
            return False
    return True