"""
QUESTION:
Implement a function named `vigenere_cipher` that takes in two parameters: `text` and `keyword`, and returns the encrypted string using the Vigenère cipher. The function should handle strings containing lowercase letters, uppercase letters, and punctuation marks, and keywords containing lowercase letters and numbers. The time complexity of the function should be O(n), where n is the length of the input string.
"""

def vigenere_cipher(text, keyword):
    encrypted_text = ""
    text = text.upper()
    keyword = keyword.upper()
    keyword_index = 0

    for char in text:
        if char.isalpha():
            shift = (ord(keyword[keyword_index % len(keyword)]) - ord('A')) % 26
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            keyword_index += 1
        else:
            encrypted_text += char

    return encrypted_text