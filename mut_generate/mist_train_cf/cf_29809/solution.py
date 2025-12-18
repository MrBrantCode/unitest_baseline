"""
QUESTION:
Given a string `s` consisting of lowercase English letters and spaces, and a shift value `shift`, write a function `decode_cipher(s: str, shift: int) -> str` to decode the hidden message by shifting each letter in the string by the given shift value. The function should return the decoded message. The shift should wrap around the alphabet, and non-alphabetic characters should remain unchanged.
"""

def decode_cipher(s: str, shift: int) -> str:
    decoded_message = ""
    for char in s:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decoded_char = chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message