"""
QUESTION:
Write a function `generatePattern` that takes a string `description` as input. For each character in the string, shift it by its 1-based index in the string, wrapping around if necessary for alphabetic characters. Non-alphabetic characters remain unchanged.
"""

def generatePattern(description: str) -> str:
    result = ""
    for i, char in enumerate(description):
        if char.isalpha():
            shift = i + 1
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result