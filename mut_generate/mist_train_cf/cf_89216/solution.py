"""
QUESTION:
Find the index of the first occurrence of the word "the" in a sentence that is encoded using a Caesar cipher with a random shift value between 1 and 25. The input sentence will be a string consisting of alphabetic characters and spaces only. If no match is found, return -1. Create a function named `decode_caesar_cipher` that takes the encoded sentence as input and returns the index of the first occurrence of the word "the" in the decoded sentence.
"""

def decode_caesar_cipher(sentence):
    def decode_word(word, shift):
        decoded_word = ""
        for char in word:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decoded_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                decoded_word += decoded_char
            else:
                decoded_word += char
        return decoded_word

    words = sentence.split()
    for shift in range(1, 26):
        for i, word in enumerate(words):
            if decode_word(word, shift).lower() == "the":
                return i

    return -1  # Return -1 if no match is found