"""
QUESTION:
[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) (RLE) is a very simple form of lossless data compression in which runs of data are stored as a single data value and count.

A simple form of RLE would encode the string `"AAABBBCCCD"` as `"3A3B3C1D"` meaning, first there are `3 A`, then `3 B`, then `3 C` and last there is `1 D`.

Your task is to write a RLE encoder and decoder using this technique. The texts to encode will always consist of only uppercase characters, no numbers.
"""

from re import sub

def run_length_encode(string: str) -> str:
    """
    Encodes a given string using Run-Length Encoding (RLE).

    Parameters:
    - string (str): The input string to be encoded. This string will consist only of uppercase characters.

    Returns:
    - str: The encoded string in RLE format.
    """
    return sub('(.)\\1*', lambda m: str(len(m.group(0))) + m.group(1), string)

def run_length_decode(encoded_string: str) -> str:
    """
    Decodes a given RLE encoded string back to its original form.

    Parameters:
    - encoded_string (str): The RLE encoded string to be decoded.

    Returns:
    - str: The decoded string in its original form.
    """
    return sub('(\\d+)(\\D)', lambda m: m.group(2) * int(m.group(1)), encoded_string)