"""
QUESTION:
Create a function called `vigenere_decrypt` that takes two parameters: `encrypted_string` and `encryption_key`, both of which are strings of lowercase letters. The function should decrypt the `encrypted_string` using the `encryption_key` as a Vigenère cipher, where each letter in the encrypted string is decrypted by shifting it backwards in the alphabet by the corresponding letter in the keyword, and return the decrypted string.
"""

def vigenere_decrypt(encrypted_string, encryption_key):
    decrypted_string = ""
    key_length = len(encryption_key)
    
    for i in range(len(encrypted_string)):
        encrypted_char = encrypted_string[i]
        key_char = encryption_key[i % key_length]
        
        encrypted_ascii = ord(encrypted_char) - ord('a')
        key_ascii = ord(key_char) - ord('a')
        
        decrypted_ascii = (encrypted_ascii - key_ascii) % 26
        
        decrypted_char = chr(decrypted_ascii + ord('a'))
        decrypted_string += decrypted_char
    
    return decrypted_string