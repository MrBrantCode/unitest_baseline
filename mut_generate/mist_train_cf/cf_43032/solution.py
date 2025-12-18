"""
QUESTION:
Implement a function named `tokenizer` that takes a string `s` as input and returns a list of integers based on the following rules: 
- Each digit (0-9) is assigned its integer representation.
- Each letter (a-z or A-Z) is assigned its position in the English alphabet (0-indexed), where 'a' or 'A' corresponds to 0, 'b' or 'B' corresponds to 1, and so on.
- All other characters are assigned the integer value 20.
"""

import numpy as np

def tokenizer(s):
    """
    Tokenize a string into a list of integers based on the following rules:
    - Each digit (0-9) is assigned its integer representation.
    - Each letter (a-z or A-Z) is assigned its position in the English alphabet (0-indexed).
    - All other characters are assigned the integer value 20.

    Args:
        s (str): The input string to be tokenized.

    Returns:
        numpy.ndarray: A list of integers representing the tokenized string.
    """
    res = []
    for char in s:
        if char.isdigit():
            res.append(int(char))
        elif char.isalpha():
            char_val = ord(char.lower()) - ord('a')
            res.append(char_val)
        else:
            res.append(20)
    return np.array(res)