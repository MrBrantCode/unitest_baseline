"""
QUESTION:
Create a function `encrypt_string` that takes a string and a key as parameters. The function should encrypt the string by converting the key to a numeric value (sum of ASCII values of its characters), then for each character in the string, add the key's numeric value to the character's ASCII value, subtract 128 if the result exceeds 127, and convert the result back to a character. The function should return the encrypted string.
"""

def encrypt_string(string, key):
    key_value = sum(ord(c) for c in key)
    encrypted_string = ""
    for char in string:
        char_value = ord(char)
        encrypted_value = char_value + key_value
        if encrypted_value > 127:
            encrypted_value -= 128
        encrypted_char = chr(encrypted_value)
        encrypted_string += encrypted_char
    return encrypted_string