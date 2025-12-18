"""
QUESTION:
Create a function `tokenize` that takes two parameters: `input_string` (str) and `token_specification` (List[Tuple[str, str]]). The `token_specification` is a list of tuples, where each tuple contains a token name and a corresponding regular expression pattern. The function should return a list of tokens, where each token is a tuple containing the token name and the matched value from the input string.
"""

import re
from typing import List, Tuple

def tokenize(input_string: str, token_specification: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    tokens = []
    combined_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for match in re.finditer(combined_regex, input_string):
        for name, value in match.groupdict().items():
            if value is not None:
                tokens.append((name, value))
                break
    return tokens