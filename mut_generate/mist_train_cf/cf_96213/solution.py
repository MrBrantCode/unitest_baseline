"""
QUESTION:
Write a function `find_the_index` that finds the index of the first occurrence of the word "the" in a given encoded sentence. The encoded sentence is created by applying a Caesar cipher with a shift value between 1 and 25. The function should try all possible shift values and return the index of the first occurrence of "the" in the decoded sentence. If "the" is not found after trying all shift values, the function should return -1. The function should ignore case and non-alphabetical characters.
"""

def find_the_index(sentence):
    def caesar_decode(sentence, shift):
        decoded = ""
        for char in sentence:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decoded += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                decoded += char
        return decoded

    for shift in range(1, 26):
        decoded_sentence = caesar_decode(sentence.lower(), shift).lower()
        index = decoded_sentence.find("the")
        if index != -1:
            return index
    return -1