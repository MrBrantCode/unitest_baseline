"""
QUESTION:
Create a function called `decode_string` that takes an encoded string and a dictionary `decoding_cipher` as parameters. The dictionary contains mappings for lowercase letters, and the function should also account for uppercase letters, numbers, punctuation, and special characters by creating unique mappings for them. If a character is not found in the mappings, it should be kept as it is in the decoded string.
"""

def decode_string(encoded_string, decoding_cipher):
    decoding_cipher.update({ "X" : "A", "Y": "B", "Z" : "C", '1': '4', '2': '5', '3': '6', '!': '?' })

    decoded_string = ''
    for character in encoded_string:
        if character in decoding_cipher.keys():
            decoded_string += decoding_cipher[character]
        else:
            decoded_string += character  
    return decoded_string