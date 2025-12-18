"""
QUESTION:
Create a function named vigenere_decrypt that takes two parameters, encrypted_string and encryption_key, and returns the decrypted string. The function should decrypt the encrypted string using a Vigenère cipher, where the encryption key is repeated to match the length of the encrypted string. The input strings will only contain lowercase letters.
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