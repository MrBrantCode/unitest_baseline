"""
QUESTION:
Create a function `sequence_check` that takes a sequence of numbers as input and returns `True` if the sequence adheres to a specific skip-counting rule where the difference between each pair of consecutive numbers is constant, and `False` otherwise.
"""

def sequence_check(seq):
    """
    Checks if the sequence adheres to a specific skip-counting rule 
    where the difference between each pair of consecutive numbers is constant.

    Args:
        seq (list): A list of numbers.

    Returns:
        bool: True if the sequence adheres to the skip-counting rule, False otherwise.
    """
    difference = seq[1] - seq[0]
    for i in range(2, len(seq)):
        if not (seq[i] - seq[i-1]) == difference:
            return False
    return True