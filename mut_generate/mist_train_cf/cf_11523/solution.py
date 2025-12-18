"""
QUESTION:
Implement the Caesar cipher algorithm to encode and decode a given string. The function should take two parameters: the string to be encoded/decoded and the shift value. The function should preserve the case of the original string and ignore non-alphabetical characters. The shift should be applied in a circular manner, meaning that shifting 'z' by 1 results in 'a' and shifting 'Z' by 1 results in 'A'. Implement two functions: caesar_cipher_encode and caesar_cipher_decode.
"""

def caesar_cipher_encode(string, shift):
    encoded_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                encoded_string += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encoded_string += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encoded_string += char
    return encoded_string


def caesar_cipher_decode(string, shift):
    decoded_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                decoded_string += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decoded_string += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decoded_string += char
    return decoded_string