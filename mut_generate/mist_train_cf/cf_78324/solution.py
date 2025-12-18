"""
QUESTION:
Implement the `encode_string` function to encode a given string by shifting its alphabetic characters two positions forward in the alphabet, wrapping around to the start of the alphabet if necessary, while non-alphabetic characters remain unchanged. Additionally, implement the `decode_string` function to reverse this process by shifting the characters two positions backward. Ensure both functions handle uppercase and lowercase letters correctly.
"""

def encode_string(text):
    encoded_text = ''
    for c in text:
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            encoded_text += chr((ord(c) - start + 2) % 26 + start)
        else:
            encoded_text += c
    return encoded_text

def decode_string(text):
    decoded_text = ''
    for c in text:
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            decoded_text += chr((ord(c) - start - 2) % 26 + start)
        else:
            decoded_text += c
    return decoded_text