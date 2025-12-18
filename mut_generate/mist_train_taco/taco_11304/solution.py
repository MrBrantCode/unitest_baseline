"""
QUESTION:
Check Tutorial tab to know how to to solve.  

You are given a string $\boldsymbol{s}$ consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in $\boldsymbol{s}$.

It’s guaranteed that every comma and every dot in $\boldsymbol{s}$ is preceeded and followed by a digit.

Sample Input 0
100,000,000.000

Sample Output 0
100
000
000
000
"""

import re

def split_string_by_delimiters(s: str) -> list:
    """
    Splits the input string by commas and dots, and returns a list of digit sequences.

    Parameters:
    s (str): The input string consisting of digits, commas, and dots.

    Returns:
    list: A list of strings, where each string is a sequence of digits.
    """
    return [part for part in re.split('[,\\.]', s) if part]