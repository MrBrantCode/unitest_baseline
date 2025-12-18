"""
QUESTION:
Implement the `encrypt` function that uses a Caesar cipher for encoding. The function should receive a string `s` and a shifting factor `shift` as parameters and return the encoded string. The shift factor can go beyond 'z' or 'Z' and loop back to the start of the alphabet. The function should preserve the case and non-alphabet characters in the original string.
"""

def encrypt(s, shift):
    result = ""

    for v in s:
        if v.isupper():
            result += chr((ord(v) - 65 + shift) % 26 + 65)

        elif v.islower():
            result += chr((ord(v) - 97 + shift) % 26 + 97)

        else:
            result += v
            
    return result