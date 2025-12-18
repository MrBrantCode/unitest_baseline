"""
QUESTION:
Write a function named `separate_paren_groups` that takes a string of balanced parentheses as input, ignores any whitespace characters, and returns a list of strings where each string represents a distinct and balanced parentheses cluster. The input string may contain embedded parentheses clusters.
"""

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    group = []
    result = []
    for char in paren_string:
        if char == ' ':
            continue
        if char == '(':
            stack.append(char)
            group.append(char)
        if char == ')':
            stack.pop()
            group.append(char)
            if not stack:
                result.append(''.join(group))
                group = []
    return result