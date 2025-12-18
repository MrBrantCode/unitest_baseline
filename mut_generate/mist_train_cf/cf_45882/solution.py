"""
QUESTION:
Create two interdependent Python functions, `encode_cyclic` and `decode_cyclic`, that encode and decode strings by cycling characters in sets of four. The functions should be able to handle special characters, command strings, spaces, and punctuation.

Function `encode_cyclic` should take a string `s` as input and return the encoded string. Function `decode_cyclic` should take the encoded string as input and return the original string.

Restrictions: The encoding style should involve modifying every 4th character in some way. The functions should be able to handle edge cases such as special characters, command strings, spaces, and punctuation. The functions should have a time complexity of O(n), where n is the number of characters in the string.
"""

def entrance(s: str, mode: str) -> str:
    """
    Encode or decode a string by cycling characters in sets of four.

    Args:
    s (str): The input string to be encoded or decoded.
    mode (str): The mode of operation, either 'encode' or 'decode'.

    Returns:
    str: The encoded or decoded string.
    """
    result = ""
    for i in range(len(s)):
        if (i+1) % 4 == 0:
            if mode == 'encode':
                result += chr(ord(s[i]) + 2)
            elif mode == 'decode':
                result += chr(ord(s[i]) - 2)
        else:
            result += s[i]
    return result