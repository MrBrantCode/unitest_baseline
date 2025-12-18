"""
QUESTION:
Write a function `transform_string` that takes a string of alphanumeric characters and special symbols as input, and returns a tuple containing the transformed string and a dictionary with the frequency count of each character in the transformed string. The transformation should follow these rules:

- Reverse the case of each alphabet character.
- For numeric characters, make them even if they are odd, and keep them as is if they are already even. If multiple digits form a number, consider the entire number for this operation, not individual digits.
- Double each unique special symbol.

The function should return a tuple where the first element is the transformed string, and the second element is a dictionary with character frequencies.
"""

from typing import Dict, Tuple
from collections import Counter
import re

def transform_string(string: str) -> Tuple[str, Dict[str, int]]:
    altered_string = []
    for match in re.finditer(r'\D|\d+', string):
        s = match.group()
        if s.isdigit():
            n = int(s)
            altered_string.append(str(n+1 if n%2 else n))
        elif s.isalpha():
            altered_string.append(s.swapcase())
        else:
            altered_string += [s]*2
    altered_string = "".join(altered_string)
    count_dict = Counter(altered_string)
    return (altered_string, count_dict)