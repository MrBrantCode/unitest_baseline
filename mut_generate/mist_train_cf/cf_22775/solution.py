"""
QUESTION:
Implement a function called `vigenere_cipher` that encrypts a given string using the Vigenère cipher with a provided keyword. The input string contains only uppercase letters and spaces, and the keyword contains only uppercase letters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def vigenere_cipher(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    keyword_index = 0

    for char in plaintext:
        if char == " ":
            ciphertext += " "
        else:
            shift = ord(keyword[keyword_index % len(keyword)]) - 65
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += encrypted_char
            keyword_index += 1

    return ciphertext