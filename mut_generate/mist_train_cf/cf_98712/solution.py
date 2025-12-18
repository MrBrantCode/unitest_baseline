"""
QUESTION:
Write a function called `shift_word` that takes a string `word` as input and returns a new string where each letter in `word` is shifted two characters ahead in the alphabet.
"""

def shift_word(word):
    shifted_word = ""
    for char in word:
        shifted_char = chr((ord(char) - 97 + 2) % 26 + 97)
        shifted_word += shifted_char
    return shifted_word