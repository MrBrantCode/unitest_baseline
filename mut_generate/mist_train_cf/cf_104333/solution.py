"""
QUESTION:
Create a function `count_unique_words` that takes a string as input, removes any leading or trailing spaces, and returns the count of unique words in the string. The function should be case-sensitive and consider "programming" and "Programming" as two different words. The input string may contain multiple spaces between words, which should be handled correctly.
"""

def count_unique_words(string):
    """
    Returns the count of unique words in the input string.
    
    The function is case-sensitive and considers "programming" and "Programming" as two different words.
    It correctly handles multiple spaces between words.

    Parameters:
    string (str): The input string.

    Returns:
    int: The count of unique words in the string.
    """
    string = string.strip()
    words = string.split()
    unique_words = set(words)
    return len(unique_words)