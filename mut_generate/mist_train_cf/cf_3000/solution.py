"""
QUESTION:
Implement a function called `encrypt_vigenere(text, key)` that takes two parameters: `text` to be encrypted and `key` used for encryption. The `key` must be at least 10 characters long, contain at least one uppercase letter, and one special character. The function should return the encrypted text using a Vigenère cipher, only encrypting uppercase letters and leaving other characters unchanged.
"""

def encrypt_vigenere(text, key):
    encrypted_text = ""
    key_length = len(key)
    text_length = len(text)
    
    extended_key = (key * (text_length // key_length)) + key[:text_length % key_length]
    
    for i in range(text_length):
        char = text[i]
        
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + ord(extended_key[i].lower()) - ord('a')) % 26 + ord('A'))
        else:
            encrypted_char = char
        
        encrypted_text += encrypted_char
    
    return encrypted_text