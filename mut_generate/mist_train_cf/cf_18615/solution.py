"""
QUESTION:
Create a function named `longest_word` that takes a sentence as input and returns the longest word that does not contain both the letters 'a' and 'b'. If no such word exists, return an empty string. The function should ignore the case where a word contains both 'a' and 'b'.
"""

def longest_word(sentence):
    """
    Returns the longest word that does not contain both the letters 'a' and 'b'.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        str: The longest word that meets the criteria. If no such word exists, an empty string is returned.
    """
    words = sentence.split()
    longest = ''
    for word in words:
        if 'a' not in word.lower() and 'b' not in word.lower():
            if len(word) > len(longest):
                longest = word
    return longest