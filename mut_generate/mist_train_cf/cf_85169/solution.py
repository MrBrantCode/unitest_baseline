"""
QUESTION:
Implement a function `caesar_cipher(text, shift)` that applies the Caesar Cipher technique to a given text expression by shifting alphabetic characters, numeric characters, and special characters by a specified number of positions. The function should handle both uppercase and lowercase alphabetic characters, and consider each block of characters to "wrap around" to the start after reaching the end. The function should also ensure compatibility with Unicode encoded characters.
"""

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        ascii_val = ord(char)
        if char.isalpha():
            if char.isupper():
                result += chr((ascii_val - 65 + shift) % 26 + 65)
            else:
                result += chr((ascii_val - 97 + shift) % 26 + 97)
        elif char.isdigit():
            result += chr((ascii_val - 48 + shift) % 10 + 48)
        elif 32 <= ascii_val <= 47 or 58 <= ascii_val <= 64 or 91 <= ascii_val <= 96 or 123 <= ascii_val <= 126:
            new_ascii = ((ascii_val - 32 + shift) % 15 + 32) if 32 <= ascii_val <= 46 else (
                ((ascii_val - 58 + shift) % 7 + 58) if 58 <= ascii_val <= 64 else (
                ((ascii_val - 91 + shift) % 6 + 91 if 91 <= ascii_val <= 96 else ((ascii_val - 123 + shift) % 4 + 123))))
            result += chr(new_ascii)
        else:
            result += char
    return result