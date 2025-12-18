"""
QUESTION:
Write a function named `decode_caesar_cipher` that takes a string `sentence` consisting of alphabetic characters and spaces as input. The function should find the index of the first occurrence of the word "the" in the sentence that is encoded using a Caesar cipher with a shift value between 1 and 25. Return the index of the first occurrence of "the" or -1 if no match is found.
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