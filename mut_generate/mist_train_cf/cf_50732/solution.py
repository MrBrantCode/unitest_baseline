"""
QUESTION:
Implement a function `quantum_superposition` that takes a string `message` and an integer `key` as input, representing the shared secret key in quantum key distribution (QKD) protocol, and returns the encrypted message. The function should simulate the cryptographic supremacy of quantum superposition by utilizing its sensitivity to eavesdropping, facilitating secure communication.
"""

def quantum_superposition(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message