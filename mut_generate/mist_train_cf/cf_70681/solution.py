"""
QUESTION:
Write a function called `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, where each string represents a distinct group of balanced parentheses. The input string may contain spaces, which should be ignored. The function should return groups that are not embedded within another group and are balanced (every opening parenthesis is duly closed).
"""

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    groups = []
    start = 0
    bal = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            bal += 1
        else:
            bal -= 1
        if bal == 0:
            groups.append(paren_string[start:i+1])
            start = i+1
    return groups