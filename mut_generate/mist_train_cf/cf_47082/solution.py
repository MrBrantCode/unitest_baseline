"""
QUESTION:
Develop a function named `get_sequences` that takes a string `s` as input. The function should identify all sequences of characters in the string that start with the letter 'a' and end with the letter 'b', regardless of the characters in between. If the input sequence lacks the letters 'a' or 'b', or if no sequences are found, the function should return a suitable error notification. The function should be able to handle multiple sequences within the same string.
"""

def get_sequences(s):
    """
    This function identifies all sequences of characters in the string that start with the letter 'a' and end with the letter 'b', 
    regardless of the characters in between.

    Args:
        s (str): The input string.

    Returns:
        list or str: A list of sequences starting with 'a' and ending with 'b', or an error notification if 'b' is not found after 'a' or no sequences are found.
    """
    start = -1  # Initialize to an impossible value
    sequences = []
    for i in range(len(s)):
        if s[i] == 'a':  # Start point of our sequence
            start = i
        elif s[i] == 'b' and start != -1:  # End point of our sequence and also checking if 'a' started tracking or not
            sequences.append(s[start:i+1]) 
            start = -1  # Reset start point
    if start != -1:  # Check if 'b' is not found after 'a'
        return "Error: 'b' not found after 'a'"
    elif not sequences:  # Check if no sequences found
        return "Error: No sequences found starting with 'a' and ending in 'b'"
    else:
        return sequences