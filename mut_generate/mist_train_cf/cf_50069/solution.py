"""
QUESTION:
Implement the `encode_cyclic` function to cyclically encode a given string, handling integers, punctuation, and blank spaces with a complex pattern. The function should shift each character by a varying number of positions based on its position in the string. Implement the `decode_cyclic` function to decode the encoded string, using a more intricate algorithm to accommodate special characters, numbers, punctuation, and spaces. The functions should work with ASCII values for all characters and the decoding process should not be a straightforward reversal of the encoding process. 

Both `encode_cyclic` and `decode_cyclic` functions should take a string as input and an optional shift value (defaulting to 3) to allow for adjustable complexity in the encoding-decoding process.
"""

def encode_cyclic(s: str, shift: int = 3) -> str:
    """Encode an input string using a Caesar Cipher. The shift varies based on the character position."""
    result = ""
    for i in range(len(s)):
        char = s[i]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + (i % shift)) % 26 + ascii_offset)
        else:
            result += chr((ord(char) + (i % shift)) % 256)
    return result

def decode_cyclic(s: str, shift: int = 3) -> str:
    """Decode a string that has been encoded using a Caesar Cipher. The shift varies based on the character position."""
    result = ""
    for i in range(len(s)):
        char = s[i]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset - (i % shift) + 26) % 26 + ascii_offset)
        else:
            result += chr((ord(char) - (i % shift) + 256) % 256)
    return result