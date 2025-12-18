"""
QUESTION:
Write a function named `reverse_encode_decode` that takes a sentence as input, reverses the order of its words, encodes the reversed sentence in Base64 format, decodes the encoded sentence, and returns the decoded sentence in its reversed word form. The function should work with Python's base64 module. The time and space complexities should be specified in Big O notation.
"""

import base64

def reverse_encode_decode(sen):
    # Reverse the input sentence
    reversed_sen = ' '.join(sen.split()[::-1])
    # Encode the reversed sentence in Base64
    encoded_sen = base64.b64encode(reversed_sen.encode())
    # Decode the encoded sentence
    decoded_sen = base64.b64decode(encoded_sen).decode()
    # Return the decoded sentence
    return decoded_sen