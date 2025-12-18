"""
QUESTION:
Implement a function called `transfigure_string` that takes a string as input and returns a new string where each alphabetic character is replaced with the next letter in the alphabet. The replacement should be case-sensitive, meaning 'z' or 'Z' should be replaced with 'a' or 'A' respectively, and non-alphabetic characters should remain unchanged.
"""

def transfigure_string(text):
    transfigured_text = ""
    for char in text:
        if char.isalpha():
            if char.lower() == 'z':
                transfigured_text += 'a' if char.islower() else 'A'
            else:
                transfigured_text += chr(ord(char) + 1)
        else:
            transfigured_text += char
    return transfigured_text