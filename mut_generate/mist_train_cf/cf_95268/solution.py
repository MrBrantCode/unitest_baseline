"""
QUESTION:
Create a function called `longest_word` that takes a sentence as input and returns the longest word that does not contain both the letters 'a' and 'b'.
"""

def longest_word(sentence):
    """
    This function takes a sentence as input and returns the longest word that does not contain both the letters 'a' and 'b'.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    str: The longest word that does not contain both 'a' and 'b'.
    """
    words = sentence.split()
    longest = ''
    for word in words:
        if 'a' in word and 'b' in word:
            continue
        if len(word) > len(longest):
            longest = word
    return longest