"""
QUESTION:
Develop a function `caesar_cipher` that takes three parameters: `action`, `shift`, and `text`. The `action` parameter should be either "encode" or "decode", and the `shift` parameter should be an integer between 1 and 25. The function should apply a Caesar cipher to the `text` string, shifting alphabetic characters by the specified amount while preserving case and leaving non-alphabetic characters unchanged.
"""

def caesar_cipher(action, shift, text):
    result = ""
    
    # valid actions are 'encode' and 'decode'
    if action not in ['encode', 'decode']:
        return "Invalid action"
        
    # adjust shift for decoding
    if action == 'decode':
        shift = -shift

    for char in text:
        # encrypt uppercase characters 
        if char.isupper():
            result += chr((ord(char) - 65 + shift ) % 26 + 65)
        # encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + shift ) % 26 + 97)
        # keep digits, punctuation and whitespace intact
        else:
            result += char
    return result