"""
QUESTION:
Write a function named `count_even_words_without_a` that takes a string as input and returns the number of words that do not contain the letter 'a' and have an even number of characters.
"""

def count_even_words_without_a(s):
    """
    Returns the number of words in a string that do not contain 'a' and have an even number of characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of words that meet the conditions.
    """
    return sum(1 for word in s.split() if 'a' not in word and len(word) % 2 == 0)