"""
QUESTION:
*This is my first Kata in the Ciphers series. This series is meant to test our coding knowledge.*

## Ciphers #1 - The 01 Cipher
This cipher doesn't exist, I just created it by myself. It can't actually be used, as there isn't a way to decode it. It's a hash. Multiple sentences may also have the same result.

## How this cipher works
It looks at the letter, and sees it's index in the alphabet, the alphabet being `a-z`, if you didn't know. If it is odd, it is replaced with `1`, if it's even, its replaced with `0`. Note that the index should start from 0. Also, if the character isn't a letter, it remains the same.

## Example

This is because `H`'s index is `7`, which is odd, so it is replaced by `1`, and so on.

Have fun (en)coding!
"""

def encode_01_cipher(s: str) -> str:
    """
    Encodes the input string using the 01 Cipher.

    The 01 Cipher replaces each letter in the string with '1' if its index in the alphabet is odd,
    and with '0' if its index is even. Non-letter characters remain unchanged.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return ''.join((str(1 - ord(c) % 2) if c.isalpha() else c for c in s))