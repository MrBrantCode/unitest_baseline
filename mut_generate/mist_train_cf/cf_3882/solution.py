"""
QUESTION:
Create a function `decode_string` to decode a given string using a cipher that contains 52 mappings of both lowercase and uppercase alphabets. The function should take two parameters: the input string and a dictionary cipher where each key-value pair represents the mapping of a character to its decoded character. The function should return the decoded string with the same case as the input string and leave non-alphabetic characters unchanged.
"""

def decode_string(s, cipher):
    decoded_string = ""
    for char in s:
        if char in cipher:
            decoded_string += cipher[char]
        else:
            decoded_string += char
    return decoded_string