"""
QUESTION:
Shift Letters in a Word. 
Write a function called `shift_letters` that takes a string `word` as input and returns a new string with all letters in the word shifted two positions ahead in the alphabet, considering only lowercase letters and assuming the alphabet is circular (i.e., 'y' shifted two positions becomes 'a', and 'z' becomes 'b').
"""

def shift_letters(word):
    shifted_word = ""
    for char in word:
        if char.isalpha() and char.islower():
            shifted_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            shifted_char = char
        shifted_word += shifted_char
    return shifted_word