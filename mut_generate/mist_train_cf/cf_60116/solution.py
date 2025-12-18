"""
QUESTION:
Write a function `is_subsequence(seq1, seq2)` that checks if sequence `seq1` appears in exactly the same order within sequence `seq2`. The function should return `True` if `seq1` is a subsequence of `seq2`, and `False` otherwise. The function should be able to handle sequences of varying lengths.
"""

def is_subsequence(seq1, seq2):
    """
    Checks if sequence seq1 appears in exactly the same order within sequence seq2.
    
    Args:
        seq1 (list): The sequence to check.
        seq2 (list): The sequence in which to check.
    
    Returns:
        bool: True if seq1 is a subsequence of seq2, False otherwise.
    """
    iter_seq1 = iter(seq1)
    iter_seq2 = iter(seq2)
    for num in iter_seq2:
        if num == next(iter_seq1, None):
            if next(iter_seq1, None) is None:
                return True
    return False