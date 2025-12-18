"""
QUESTION:
Example

Input

mmemewwemeww


Output

Cat
"""

import re

def identify_animal(s: str) -> str:
    b = s
    while True:
        s = re.sub('(m|e)mew(e|w)', '\\1\\2', s)
        if b == s:
            break
        b = s
    return 'Cat' if s == 'mew' else 'Rabbit'