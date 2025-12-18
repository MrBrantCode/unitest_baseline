"""
QUESTION:
Create a function `compare_words` that takes two strings as input and returns the string that is greater in lexical order, considering lowercase letters as greater than uppercase letters.
"""

def compare_words(word1, word2):
    if word1 > word2:
        return word1
    else:
        return word2