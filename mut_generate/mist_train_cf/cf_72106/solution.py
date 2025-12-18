"""
QUESTION:
Construct a function named `construct_sequence` that generates a 12-character sequence consisting only of the letters 'x', 'y', and 'z', with no repeating pairs.
"""

def construct_sequence(n=12):
    """
    Generates a sequence of 'n' characters consisting only of 'x', 'y', and 'z' 
    with no repeating pairs.

    Args:
        n (int): The length of the sequence (default is 12).

    Returns:
        str: A sequence of 'n' characters.
    """
    next_char = {'x': 'y', 'y': 'z', 'z': 'x'}  
    sequence = []
    current_char = 'x'  

    for _ in range(n):  
        sequence.append(current_char)  
        current_char = next_char[current_char]  

    return "".join(sequence)