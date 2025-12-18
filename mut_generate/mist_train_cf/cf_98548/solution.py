"""
QUESTION:
Write a function named `decrypt_message(message, mapping)` that takes a string `message` and a dictionary `mapping` as inputs, where `message` is the encrypted message and `mapping` is a dictionary that maps each cipher symbol to its corresponding plaintext character. The function should return the decrypted message by replacing each symbol in the `message` with its corresponding plaintext character based on the `mapping`. If a symbol is not found in the `mapping`, it should be left unchanged in the decrypted message.
"""

def decrypt_message(message, mapping):
    decrypted_message = ""
    for symbol in message:
        if symbol in mapping:
            decrypted_message += mapping[symbol]
        else:
            decrypted_message += symbol
    return decrypted_message