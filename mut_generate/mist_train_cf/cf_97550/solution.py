"""
QUESTION:
Write a function `shift_word` that takes a string as input and returns the string with all letters shifted two characters ahead in the alphabet. The function should work for any string of lowercase letters. If the input string is empty, the function should return an empty string.
"""

def shift_word(word):
    shifted_word = ""
    for char in word:
        shifted_char = chr(ord(char) + 2)
        shifted_word += shifted_char
    return shifted_word