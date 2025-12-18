"""
QUESTION:
*This is the second Kata in the Ciphers series. This series is meant to test our coding knowledge.*

## Ciphers #2 - The reversed Cipher
This is a lame method I use to write things such that my friends don't understand. It's still fairly readable if you think about it.

## How this cipher works
First, you need to reverse the string. Then, the last character in the original string (the first character in the reversed string) needs to be moved to the back. Words will be separated by spaces, and punctuation marks can be counted as part of the word.

## Example

This is because `"Hello"` reversed is `"olleH"` and `"o"` is moved to the back, and so on. The exclamation mark is considered to be part of the word `"World"`.

Have fun (en)coding!
"""

def encode_reversed_cipher(s: str) -> str:
    """
    Encodes the input string using the reversed cipher method.

    The method works by reversing each word in the string and then moving the first character of the reversed word (which was the last character of the original word) to the end of the word.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return ' '.join((w[-2::-1] + w[-1] for w in s.split()))