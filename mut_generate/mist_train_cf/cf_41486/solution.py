"""
QUESTION:
Implement the `nac_decrypt` function, which takes a string `encrypted_message` and a string `decryption_key` as input, and returns the decrypted message as a string. The function should decrypt the message using a proprietary algorithm specific to the `decryption_key`, which is assumed to be valid and matches the version of the algorithm used to encrypt the message. The decryption algorithm should only decrypt alphabetic characters, and non-alphabetic characters should remain unchanged.
"""

def nac_decrypt(encrypted_message, decryption_key):
    # Placeholder decryption logic
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            decrypted_message += chr(((ord(char) - 65) % 26) + 65)
        else:
            decrypted_message += char
    return decrypted_message