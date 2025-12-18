"""
QUESTION:
Write a function `tokenize_code(code: str, token_mapping: dict) -> List[Tuple[str, str]]` that tokenizes the given input code based on the provided character sequence to token type mapping. The function should take two parameters: `code` (a string representing the input code to be tokenized) and `token_mapping` (a dictionary representing the character sequence to token type mapping). It should return a list of tokens, where each token is a tuple containing the token type and the corresponding substring from the input code. The input code is assumed to contain only valid characters and sequences based on the given token mapping.
"""

from typing import List, Tuple, Dict

def tokenize_code(code: str, token_mapping: Dict[str, str]) -> List[Tuple[str, str]]:
    """
    Tokenizes the given input code based on the provided character sequence to token type mapping.

    Args:
    code (str): A string representing the input code to be tokenized.
    token_mapping (Dict[str, str]): A dictionary representing the character sequence to token type mapping.

    Returns:
    List[Tuple[str, str]]: A list of tokens, where each token is a tuple containing the token type and the corresponding substring from the input code.
    """

    tokens = []
    i = 0
    while i < len(code):
        found = False
        for token, value in token_mapping.items():
            if code[i:].startswith(token):
                tokens.append((value, token))
                i += len(token)
                found = True
                break
        if not found:
            if code[i].isalpha():
                j = i
                while j < len(code) and code[j].isalpha():
                    j += 1
                tokens.append(("IDENTIFIER", code[i:j]))
                i = j
            elif code[i].isdigit():
                j = i
                while j < len(code) and code[j].isdigit():
                    j += 1
                tokens.append(("NUMBER", code[i:j]))
                i = j
            else:
                i += 1
    return tokens