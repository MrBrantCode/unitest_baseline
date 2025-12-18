"""
QUESTION:
Create a function `rot13(text)` that takes a string as input and returns the string encrypted using the ROT13 cipher. The function should shift each alphabetical character in the string 13 places forward, wrapping around the alphabet if necessary, while leaving non-alphabetical characters unchanged. The function should work with both uppercase and lowercase letters.
"""

def rot13(text):
    result = ""
    
    for char in text:
        code = ord(char)
        if 65 <= code <= 90:
            result += chr((code - 65 + 13) % 26 + 65)
        elif 97 <= code <= 122:
            result += chr((code - 97 + 13) % 26 + 97)
        else:
            result += char
    
    return result