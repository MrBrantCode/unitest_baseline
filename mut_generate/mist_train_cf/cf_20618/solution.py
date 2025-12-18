"""
QUESTION:
Write a function `find_the_index(sentence)` that finds the index of the string "the" in the input sentence that has been encoded using a Caesar cipher with a shift value between 1 and 25. If "the" is not found after trying all shift values, return -1.
"""

def caesar_decode(sentence, shift):
    decoded = ""
    for char in sentence:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decoded += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decoded += char
    return decoded

def find_the_index(sentence):
    for shift in range(1, 26):
        decoded_sentence = caesar_decode(sentence, shift)
        index = decoded_sentence.find("the")
        if index != -1:
            return index
    return -1