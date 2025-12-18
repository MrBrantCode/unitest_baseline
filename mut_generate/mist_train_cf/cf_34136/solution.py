"""
QUESTION:
Implement a function `encode` that takes an input string and a shift amount as parameters and returns the encoded string based on the shift cipher algorithm. The function should handle both uppercase and lowercase letters and keep non-alphabetic characters unchanged. The shift should be circular, wrapping around to the beginning if the shift amount exceeds the length of the alphabet.
"""

def encode(input_str, shift_amount):
    result = ""
    for char in input_str:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + shift_amount) % 26 + shift)
        else:
            result += char
    return result