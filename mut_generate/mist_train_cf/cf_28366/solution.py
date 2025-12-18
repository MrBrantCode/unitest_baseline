"""
QUESTION:
Create a function `count_capital_words` that takes a string representing a code snippet as input and returns the count of words in all capital letters within the comment denoted by the `#` symbol. Assume words are separated by spaces and words in all capital letters consist of uppercase letters only.
"""

import re

def count_capital_words(code_snippet: str) -> int:
    comment = re.search(r'#(.*)', code_snippet).group(1)  # Extract the comment
    capital_words = re.findall(r'\b[A-Z]+\b', comment)  # Find all words in all capital letters
    return len(capital_words)