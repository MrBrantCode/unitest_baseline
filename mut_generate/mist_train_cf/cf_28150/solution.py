"""
QUESTION:
Write a function `fixDivIndentation(html: str) -> str` that takes in a string representing an HTML document with potentially inconsistent indentation of closing `</div>` tags. The function should return the corrected HTML string where the indentation of closing `</div>` tags matches their corresponding opening `<div>` tags. The indentation is represented using 4 spaces.
"""

def fixDivIndentation(html: str) -> str:
    lines = html.split('\n')
    stack = []
    result = []
    indent_level = 0

    for line in lines:
        if line.strip().startswith('<div>'):
            result.append(' ' * indent_level + line.strip())
            stack.append(indent_level)
            indent_level += 4
        elif line.strip().startswith('</div>'):
            indent_level = stack.pop()
            result.append(' ' * indent_level + line.strip())
        else:
            result.append(' ' * indent_level + line.strip())

    return '\n'.join(result)