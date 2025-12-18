"""
QUESTION:
Implement a function `ValidWordSquare(words)` that takes a list of strings `words` as input and returns `True` if the input list forms a valid word square and `False` otherwise. A valid word square is defined as a sequence of words where the kth row and column yield the same string. 

The input list `words` contains at least 1 and at most 500 strings, each string has a length between 1 and 500, and all strings only contain lowercase English letters.
"""

def valid_word_square(words):
    """
    This function checks if the input list of strings forms a valid word square.
    
    A valid word square is defined as a sequence of words where the kth row and column yield the same string.
    
    Args:
    words (list): A list of strings.
    
    Returns:
    bool: True if the input list forms a valid word square, False otherwise.
    """
    
    for i in range(len(words)):  
        # Check every word in the list
        for j in range(len(words[i])):
            # For each word, check the words[j] (jth letter)
            if j >= len(words) or i >= len(words[j]):
                # If lengths are unequal
                return False
            if words[i][j] != words[j][i]:
                # Checking for 'ith' word equal to 'ith' letter of all words
                return False
    # If none of the conditions met, return True
    return True