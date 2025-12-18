"""
QUESTION:
Create a function `check_sequence(seq)` that checks if the length of the input sequence `seq` is within the range of 5 to 20 characters (inclusive). The function should return `True` if the sequence length is within the specified range and `False` otherwise.
"""

def check_sequence(seq):
    if len(seq) >= 5 and len(seq) <= 20:
        return True
    else:
        return False