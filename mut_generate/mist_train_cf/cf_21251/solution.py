"""
QUESTION:
Create a function called `convert_to_ascii` that takes an integer `n` as input and returns its corresponding ASCII character. The function should handle negative integers by converting them to their positive values before conversion. Do not use any built-in functions that directly convert integers to ASCII characters, except for the `chr` function.
"""

def convert_to_ascii(n):
    if n < 0:
        n = abs(n)
    ascii_char = chr(n)
    return ascii_char