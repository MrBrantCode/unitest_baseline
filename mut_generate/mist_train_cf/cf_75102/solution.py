"""
QUESTION:
Design a function named `find_next_in_sequence` that takes a list of integers as input and returns the next number in a linear arithmetic sequence. The sequence is assumed to be a list of numbers in which the difference between any two consecutive numbers is constant. The function should check if the input sequence is linear and return the next number if it is. If the sequence is not linear, the function should return a message indicating this.
"""

def find_next_in_sequence(seq):
    """
    This function takes a list of integers as input and returns the next number in a linear arithmetic sequence.
    If the sequence is not linear, it returns a message indicating this.

    Args:
        seq (list): A list of integers.

    Returns:
        int or str: The next number in the sequence if it's linear, otherwise a message indicating it's not linear.
    """

    # Calculate the difference between subsequent numbers
    diffs = [j-i for i, j in zip(seq[:-1], seq[1:])]
    
    # Assume the difference is constant
    const_diff = diffs[0]

    # Check that the difference is indeed constant
    for diff in diffs:
        if diff != const_diff:
            return "Sequence is not linear."

    # Return the next item in the sequence
    return seq[-1] + const_diff