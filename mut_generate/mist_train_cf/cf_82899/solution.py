"""
QUESTION:
Develop a function `has_vowel_in_second_position` that takes an array of words as input and returns `True` if at least one word has the vowel 'e' at the second character position (index 1). The function should only consider words with a length of at least 2 characters.
"""

def has_vowel_in_second_position(words):
    for word in words:
        if len(word) >= 2 and word[1] == 'e':
            return True
    return False