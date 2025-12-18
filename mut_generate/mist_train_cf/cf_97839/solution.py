"""
QUESTION:
Write a function called `find_hidden_word` that takes two parameters, `word1` and `word2`, both of which are strings. The function should return a string that consists of the letters in `word1` that are not in `word2`. The order of the letters in the output string should be the same as their order in `word1`.
"""

def find_hidden_word(word1, word2):
    """
    Returns a string consisting of the letters in word1 that are not in word2.
    
    Parameters:
    word1 (str): The first word.
    word2 (str): The second word.
    
    Returns:
    str: A string of letters from word1 that are not in word2.
    """
    hidden_word = ""
    for letter in word1:
        if letter not in word2:
            hidden_word += letter
    return hidden_word