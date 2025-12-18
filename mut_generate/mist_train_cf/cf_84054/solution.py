"""
QUESTION:
Write a recursive function named `traverse_list` that takes a list of words and an optional shift value (defaulting to 2) as input. The function should perform a Caesar shift of the given value on each alphabetical character in each word, ignoring non-alphabetical characters, and print each modified letter on a separate line.
"""

def traverse_list(word_list, shift=2):
    if len(word_list) == 0:
        return
    else:
        word = word_list[0]
        for letter in word:
            print(caesar_shift(letter, shift))
        # Process the remaining words
        traverse_list(word_list[1:], shift)

def caesar_shift(letter, shift):
    # Perform a Caesar shift on a character
    if letter.isalpha():
        ascii_offset = ord('a') if letter.islower() else ord('A')
        return chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
    else:
        return letter