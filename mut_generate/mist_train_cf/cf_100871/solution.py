"""
QUESTION:
Write a Python function named `decrypt_message` that decrypts a message encoded using a rare homophonic substitution cipher. The function should take two parameters: the encrypted message and the mapping between the cipher symbols and plaintext characters. The mapping will be a dictionary where the keys are the cipher symbols and the values are the corresponding plaintext characters. The function should return the decrypted message.
"""

def decrypt_message(message, mapping):
    decrypted_message = ""
    for symbol in message:
        if symbol in mapping:
            decrypted_message += mapping[symbol]
        else:
            decrypted_message += symbol
    return decrypted_message