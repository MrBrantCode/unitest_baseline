"""
QUESTION:
# How much is the fish! (- Scooter )
The ocean is full of colorful fishes. We as programmers want to know the hexadecimal value of these fishes.

## Task
Take all hexadecimal valid characters (a,b,c,d,e,f) of the given name and XOR them. Return the result as an integer.

## Input
The input is always a string, which can contain spaces, upper and lower case letters but no digits. 

## Example

`fisHex("redlionfish") -> e,d,f -> XOR -> 12`
"""

from functools import reduce

VALID_HEX_CHARS = frozenset('abcdefABCDEF')

def calculate_fish_hex_xor(fish_name: str) -> int:
    """
    Calculate the XOR of all valid hexadecimal characters in the given fish name.

    Parameters:
    fish_name (str): The name of the fish, which can contain spaces, upper and lower case letters but no digits.

    Returns:
    int: The result of XORing all valid hexadecimal characters found in the input string.
    """
    return reduce(lambda b, c: b ^ c, (int(a, 16) for a in fish_name if a in VALID_HEX_CHARS), 0)