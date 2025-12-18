"""
QUESTION:
Implement a function `shift_string(input_string, shift)` that takes an input string and a shift value as parameters. The function should return the input string with each alphabetic character shifted by the specified number of positions in the alphabet, while non-alphabetic characters remain unchanged. The shift should wrap around the alphabet if necessary (e.g., 'z' shifted by 1 becomes 'a'). The function should handle both uppercase and lowercase letters.
"""

def shift_string(input_string, shift):
    shifted_string = ""
    for char in input_string:
        if char.isalpha():
            shift_amount = (ord(char) - ord('a') + shift) % 26 if char.islower() else (ord(char) - ord('A') + shift) % 26
            shifted_char = chr(ord('a') + shift_amount) if char.islower() else chr(ord('A') + shift_amount)
            shifted_string += shifted_char
        else:
            shifted_string += char
    return shifted_string