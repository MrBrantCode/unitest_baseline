"""
QUESTION:
Create a function `compare_third_characters` that takes two strings as input and returns a boolean indicating whether the character at the third position (index 2) in each string is the same. If either string has a length less than 3, return `False`. Assume Python's 0-based indexing.
"""

def compare_third_characters(word1, word2):
    """
    Compare the third characters of two strings.
    
    Args:
    word1 (str): The first string.
    word2 (str): The second string.
    
    Returns:
    bool: True if the third characters are the same, False otherwise.
    """
    if len(word1) < 3 or len(word2) < 3:
        return False
    return word1[2] == word2[2]