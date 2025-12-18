"""
QUESTION:
Implement the `encrypt_sensitive_info` and `decrypt_sensitive_info` functions to securely store sensitive information using a combination of base64 encoding and a simple substitution cipher. The `encrypt_sensitive_info` function should take in the sensitive information `info` and a `key` as input and return the encrypted string. The `decrypt_sensitive_info` function should take the encrypted string and the `key` as input and return the original sensitive information. 

The encryption scheme should first apply base64 encoding to the input `info`, then use the provided `key` to shift each character of the encoded string by the key value, wrapping around to the beginning of the ASCII table if necessary. The decryption function should reverse this process to retrieve the original sensitive information.
"""

import base64

def encrypt_sensitive_info(info, key):
    encoded_info = base64.b64encode(info.encode()).decode()
    encrypted_info = ''.join([chr((ord(char) + key) % 256) for char in encoded_info])
    return encrypted_info

def decrypt_sensitive_info(encrypted_info, key):
    decrypted_info = ''.join([chr((ord(char) - key) % 256) for char in encrypted_info])
    decoded_info = base64.b64decode(decrypted_info.encode()).decode()
    return decoded_info