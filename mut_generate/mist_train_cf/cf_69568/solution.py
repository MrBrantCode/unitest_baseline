"""
QUESTION:
Create a function named `check_sequence` that takes a list of numbers `seq` as input. The function should determine whether the input sequence is arithmetic, geometric, both, or neither, and calculate the common difference for arithmetic sequences or the common ratio for geometric sequences. If the sequence is too short (less than 2 elements), the function should return a message indicating this. The function should return a tuple containing a string describing the type of sequence and the common difference or ratio (if applicable), or `None` if it does not exist.
"""

def check_sequence(seq):
    if len(seq) < 2:
        return 'The sequence is too short', None
    diff = seq[1] - seq[0]
    ratio = seq[1] / seq[0]
    is_arithmetic = all([seq[i] - seq[i-1] == diff for i in range(2, len(seq))])
    is_geometric = all([seq[i] / seq[i-1] == ratio for i in range(2, len(seq))])
    if is_arithmetic and is_geometric:
        return 'The sequence is both arithmetic and geometric', diff, ratio
    elif is_arithmetic:
        return 'The sequence is arithmetic', diff, None
    elif is_geometric:
        return 'The sequence is geometric', None, ratio
    else:
        return 'The sequence is neither arithmetic nor geometric', None, None