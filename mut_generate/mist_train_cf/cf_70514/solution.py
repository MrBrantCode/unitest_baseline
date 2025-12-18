"""
QUESTION:
Write a function `is_well_formed(html_string)` that determines whether an entered string is a well-formed nested HTML tag. The function should handle cases of deeply nested HTML tags with nested layers of more than two levels deep and verify that each opening tag has a corresponding closing tag.
"""

def is_well_formed(html_string):
    stack = []
    tag = ""
    read_tag = False
    for char in html_string:
        if char == '<':
            read_tag = True
            tag = ""
        elif char == '>':
            read_tag = False
            if tag.startswith("/"):
                if len(stack) == 0 or stack[-1] != tag[1:]:
                    return False
                stack.pop()
            else:
                stack.append(tag)
        elif read_tag:
            tag += char

    return len(stack) == 0