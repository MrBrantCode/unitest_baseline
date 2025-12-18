"""
QUESTION:
Write two functions, `encode_base64(input_string)` and `decode_base64(encoded_string)`, to encode a given string into Base64 and then decode it back to its original form. The input string can contain any ASCII characters. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def base64_encode(input_string):
    base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encodedString = ""
    asciiRepresentation = [ord(c) for c in input_string]
    bitBuffer = 0
    bitsInBuffer = 0

    for c in asciiRepresentation:
        bitBuffer = (bitBuffer << 8) | c
        bitsInBuffer += 8

        while bitsInBuffer >= 6:
            bitsInBuffer -= 6
            encodedString += base64Chars[(bitBuffer >> bitsInBuffer) & 63]

    if bitsInBuffer > 0:
        bitBuffer <<= 6 - bitsInBuffer
        encodedString += base64Chars[bitBuffer & 63]

    while len(encodedString) % 4 != 0:
        encodedString += '='

    return encodedString

def base64_decode(encoded_string):
    base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    decodedString = ""
    bitBuffer = 0
    bitsInBuffer = 0

    for c in encoded_string:
        if c == '=':
            break

        bitBuffer = (bitBuffer << 6) | base64Chars.index(c)
        bitsInBuffer += 6

        if bitsInBuffer >= 8:
            bitsInBuffer -= 8
            decodedString += chr((bitBuffer >> bitsInBuffer) & 255)

    return decodedString