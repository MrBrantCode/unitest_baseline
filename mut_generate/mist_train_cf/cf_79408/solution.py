"""
QUESTION:
Write a function separate_paren_groups that takes a string of parentheses and returns a list of distinct balanced parentheses clusters. The function should ignore whitespace characters, correctly identify balanced parentheses clusters, and handle nested and embedded parentheses.
"""

from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove whitespace characters
    paren_string = paren_string.replace(' ', '')
    
    def is_balanced(s: str) -> bool:
        """
        Helper function to check if parentheses string is balanced
        """
        while '()' in s:
            s = s.replace('()', '')
        return not s
    
    # Get clusters
    clusters = []
    cluster = ''
    count = 0
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        cluster += char
        if count == 0:
            if is_balanced(cluster):
                clusters.append(cluster)
            cluster = ''
    return clusters