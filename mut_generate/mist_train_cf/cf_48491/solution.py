"""
QUESTION:
Write a function called `count_valid_words` that takes a string of text as input and returns the number of words that do not contain the letter 'a' and have an even number of characters. The function should split the input string into individual words and iterate over each word to apply the specified conditions.
"""

def count_valid_words(text):
    """
    Counts the number of words in a given text that do not contain the letter 'a' and have an even number of characters.
    
    Parameters:
    text (str): The input string of text.
    
    Returns:
    int: The number of valid words.
    """
    words = text.split()
    total_words = 0
    for word in words:
        if 'a' not in word and len(word) % 2 == 0:
            total_words += 1
    return total_words