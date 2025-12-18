"""
QUESTION:
Implement a function `decode_strings(encoded_list)` that takes a list of encoded binary strings as input and returns the original input string. Each character in the input string was encoded using zero-width joiners (`\u200D`), zero-width non-joiners (`\u200C`), zero-width spaces (`\u200B`), and the Unicode character for zero-width sequence. The encoding process involves converting each character to its Unicode code point, then converting the code point to its binary representation, and finally encoding the binary representation using the specified zero-width characters. The `\u200D` is used as a separator, `\u200B` represents '0', and `\u200C` represents '1' in the binary representation.
"""

from typing import List

def decode_strings(encoded_list: List[str]) -> str:
    decoded_chars = []
    for encoded_str in encoded_list:
        binary_str = ''
        for char in encoded_str:
            if char == '\u200D':
                if binary_str:
                    decoded_chars.append(chr(int(binary_str, 2)))
                    binary_str = ''
            elif char == '\u200B':
                binary_str += '0'
            elif char == '\u200C':
                binary_str += '1'
        if binary_str:
            decoded_chars.append(chr(int(binary_str, 2)))
    return ''.join(decoded_chars)