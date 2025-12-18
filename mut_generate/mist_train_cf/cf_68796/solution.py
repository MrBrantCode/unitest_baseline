"""
QUESTION:
Create a function named `replace_non_alnum` that takes two parameters: `text` and `symbol`. The function should replace all non-alphanumeric characters in the input `text` (excluding whitespace) with the provided `symbol`. The function should support multilingual characters.
"""

import re

def replace_non_alnum(text, symbol):
    return re.sub(r'[^\w\s]', symbol, text)