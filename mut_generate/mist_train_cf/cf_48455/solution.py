"""
QUESTION:
Create a function named `find_caps` that takes a string `text` as input. The string can contain 1 to 1000 characters, including letters, digits, and special characters. The function should return a tuple containing: 
1) a list of unique capital letters found in the string, in alphabetical order, 
2) the total count of capital letters found in the string, and 
3) a list of continuous sequences of capital letters found in the string.
"""

import re
from typing import List, Tuple

def find_caps(text: str) -> Tuple[List[str], int, List[str]]:
    caps = re.findall(r'[A-Z]', text)
    seqs = re.findall(r'[A-Z]+', text)
    return (sorted(set(caps)), len(caps), seqs)