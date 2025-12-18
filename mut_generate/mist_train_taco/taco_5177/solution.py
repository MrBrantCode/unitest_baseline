"""
QUESTION:
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: `a = 1, b = 2, c = 3` etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""

def find_highest_scoring_word(words_string: str) -> str:
    """
    Finds the highest scoring word in a given string of words.

    Each letter of a word scores points according to its position in the alphabet:
    'a' = 1, 'b' = 2, 'c' = 3, etc.

    If two words score the same, the word that appears earliest in the string is returned.

    Parameters:
    words_string (str): A string containing words separated by spaces.

    Returns:
    str: The highest scoring word from the input string.
    """
    def word_score(word):
        return sum((ord(c) - 96 for c in word))
    
    words = words_string.split()
    return max(words, key=word_score)