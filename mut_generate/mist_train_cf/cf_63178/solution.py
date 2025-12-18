"""
QUESTION:
Implement a function named `decrypt_caesar_cypher` that decrypts a message encrypted using a Caesar cipher. The function should take two parameters: `message` (the encrypted message) and `shift` (the shift value used for encryption, defaulting to 3). The function should return the decrypted message as a string.

The decryption process should shift each letter in the encrypted message back by the same amount it was shifted during encryption, without modifying non-alphabetic characters. If the shift operation lands on a character code below 'A' or 'a', it should loop back around to the far end of the alphabet.

The decrypted message should be calculated as the sum of the ASCII values of its characters.
"""

def decrypt_caesar_cypher(message, shift=3):
    result = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result