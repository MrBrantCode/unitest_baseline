"""
QUESTION:
Write a function called `remove_duplicate_words` that takes a string as input and returns a new string with all duplicate words removed. The original order of words should be preserved.
"""

def remove_duplicate_words(input_string):
    """
    This function takes a string as input, removes duplicate words, and returns the modified string.
    
    Parameters:
    input_string (str): The input string from which to remove duplicate words.
    
    Returns:
    str: A new string with all duplicate words removed, preserving the original order of words.
    """
    words = input_string.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    modified_string = ' '.join(unique_words)
    return modified_string