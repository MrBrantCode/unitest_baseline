"""
QUESTION:
Implement a function named `vigenere_cipher` that takes in two parameters: `text` (the string to be encrypted) and `keyword` (the keyword used for encryption). The function should return the encrypted string using the Vigenère cipher. The input string can contain lowercase letters, uppercase letters, and punctuation marks. The keyword can contain lowercase letters and numbers. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def vigenere_cipher(text, keyword):
    encrypted_text = ""
    text = text.upper()
    keyword = keyword.upper()
    keyword_index = 0

    for char in text:
        if char.isalpha():
            shift = (ord(keyword[keyword_index]) - ord('A')) % 26
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            encrypted_text += char

    return encrypted_text