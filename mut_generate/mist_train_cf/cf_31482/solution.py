"""
QUESTION:
Implement a function `decrypt_message(encrypted_message, shift)` that takes a string `encrypted_message` and an integer `shift` as input. The function should decrypt the message by shifting each alphabetic character in the `encrypted_message` in the opposite direction of the shift, while non-alphabetic characters remain unchanged. The shift should wrap around the alphabet, i.e., 'A' shifted by 1 becomes 'B', 'Z' shifted by 1 becomes 'A', and similarly for lowercase letters. The function should return the decrypted message as a string.
"""

def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted_char = chr(((ord(char) - shift - 65) % 26) + 65) if char.isupper() else chr(((ord(char) - shift - 97) % 26) + 97)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message