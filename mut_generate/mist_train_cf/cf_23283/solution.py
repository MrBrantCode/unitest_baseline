"""
QUESTION:
Create a function called `longest_consecutive` that takes a string as input and returns the longest consecutive sequence of characters. The sequence should be a string of the same character repeated consecutively in the original string.
"""

def longest_consecutive(string):
    """
    Returns the longest consecutive sequence of characters in a string.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The longest consecutive sequence of characters.
    """
    
    # Initialize variables to store the longest sequence and its length
    max_length = 0
    max_sequence = ''
    
    # Iterate over each unique character in the string
    for char in set(string):
        # Initialize variables to store the current sequence and its length
        current_length = 0
        
        # Iterate over the string to find the longest sequence of the current character
        for i in range(len(string)):
            if string[i] == char:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
                    max_sequence = char * max_length
            else:
                current_length = 0
                
    return max_sequence