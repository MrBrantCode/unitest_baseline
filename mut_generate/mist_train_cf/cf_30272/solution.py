"""
QUESTION:
Write a function `parsePeripheralConstants` that takes a string representing a C header code snippet as input and returns a dictionary mapping peripheral names to their values. The code snippet contains `#if defined` blocks, each defining peripherals and their values in the format `<Peripheral> = <Value>,`. Extract the peripheral names and values, where peripheral names and values are alphanumeric and may contain underscores.
"""

import re

def parse_peripheral_constants(code_snippet):
    """
    Parse peripheral constants from a C header code snippet.

    Args:
    code_snippet (str): A string representing a C header code snippet.

    Returns:
    dict: A dictionary mapping peripheral names to their values.
    """
    pattern = r'#if defined\((.*?)\)\s+([\w]+)\s+=\s+(.*?),'
    matches = re.findall(pattern, code_snippet)
    return {match[1]: match[2] for match in matches}