"""
QUESTION:
Implement a function `is_well_formed_markup` that checks if a given string representing custom markup content is well-formed, meaning all opening tags have corresponding closing tags in the correct order. The function should return `True` if the markup is well-formed and `False` otherwise. The input string may contain alphanumeric characters, spaces, and the characters `<`, `>`, and `/`. Assume the markup only contains valid opening and closing tags, with no other HTML elements or attributes.
"""

def is_well_formed_markup(markup: str) -> bool:
    stack = []
    i = 0
    while i < len(markup):
        if markup[i] == '<':
            if i+1 < len(markup) and markup[i+1] == '/':
                if stack and stack[-1] == markup[i+2:i+markup[i+2:].find('>')+2]:
                    stack.pop()
                    i += markup[i+2:].find('>') + 3
                else:
                    return False
            else:
                stack.append(markup[i+1:i+markup[i+1:].find('>')+1])
                i += markup[i+1:].find('>') + 2
        else:
            i += 1
    return not stack