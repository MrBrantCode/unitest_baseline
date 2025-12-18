"""
QUESTION:
Design a function called `triadic(seq)` that constructs a list of triadic sequences originating from a given sequence of integers. A triadic sequence includes three consecutive elements from the input sequence. 

The function should handle any sequence of integers and include error handling to check if the input sequence has at least three elements. If the sequence has less than three elements, the function should print an error message and return without constructing any sequences.
"""

def triadic(seq):
    """
    This function constructs a list of triadic sequences originating from a given sequence of integers.
    A triadic sequence includes three consecutive elements from the input sequence.

    Args:
        seq (list): A list of integers.

    Returns:
        list: A list of triadic sequences. Each triadic sequence is a list of three consecutive integers.
    """
    # Check if seq has at least 3 elements
    if len(seq) < 3:
        print("The input sequence must have at least 3 elements.")
        return
    else:
        return [[seq[i], seq[i+1], seq[i+2]] for i in range(len(seq)-2)]