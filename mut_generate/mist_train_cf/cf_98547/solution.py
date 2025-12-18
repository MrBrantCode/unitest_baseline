"""
QUESTION:
Generate a sequence with the function `generate_sequence` that starts from a given number with a common difference of -1 between each term. The sequence should only include terms with an absolute value greater than 5. The function should return the nth term of the sequence. The initial number should be 20, and the value of n should be 10.
"""

def generate_sequence(initial_number, n):
    """
    Generate a sequence starting from the initial number with a common difference of -1 
    between each term. The sequence only includes terms with an absolute value greater 
    than 5. The function returns the nth term of the sequence.

    Args:
    initial_number (int): The initial number of the sequence.
    n (int): The term number to be returned.

    Returns:
    int: The nth term of the sequence.
    """
    sequence_term = initial_number
    count = 0
    while count < n:
        while abs(sequence_term) <= 5:
            sequence_term -= 1
        count += 1
        sequence_term -= 1
    return sequence_term + 1