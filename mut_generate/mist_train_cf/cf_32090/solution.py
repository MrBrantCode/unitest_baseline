"""
QUESTION:
Implement a function named `rotate` that takes in a string `input_string` and an integer `shift` and returns the resulting string after rotating each alphabetic character by the specified shift. The rotation should preserve the case of the characters and wrap around the alphabet if the shift exceeds its bounds. You can assume that the input string contains only alphabetic characters and the shift value can be positive, negative, or zero.
"""

def rotate(input_string: str, shift: int) -> str:
    result = ""
    for char in input_string:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result