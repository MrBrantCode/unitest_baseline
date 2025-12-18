"""
QUESTION:
Write a function `encode(s, a=None)` that encodes a given string `s` in Base64 format. The function should handle custom alphabets consisting of 64 or more unique characters. If a custom alphabet `a` is provided, it should be used for encoding instead of the standard Base64 alphabet.

The string `s` consists of 1 to 1000 printable ASCII characters. The optional custom alphabet `a` consists of 64 to 100 unique printable ASCII characters.
"""

def encode(s, a=None):
    o = ""
    a = a.strip() if a else "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    binrep = ''.join(format(ord(c), '08b') for c in s)
    padamt = (-len(binrep)) % 6

    binrep += '0' * padamt
    padamt = (-len(s)) % 3
    
    for i in range(0, len(binrep), 6):
        o += a[int(binrep[i:i+6], 2)]

    o += ''.join('=' * padamt)

    return o