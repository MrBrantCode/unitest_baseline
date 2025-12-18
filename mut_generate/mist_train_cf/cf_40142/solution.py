"""
QUESTION:
Implement the `is_well_formed_html(html: str) -> bool` function to check if a given HTML string contains a valid structure of opening and closing tags. The function should return `True` if the HTML is well-formed, and `False` otherwise. The HTML tags can contain lowercase letters, numbers, and hyphens, but cannot start with a number, and must be properly nested and closed in the correct order.
"""

def is_well_formed_html(html: str) -> bool:
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            if html[i+1] == '/':
                if not stack or stack[-1] != html[i+2:i+html[i:].index('>')+2]:
                    return False
                stack.pop()
                i += html[i:].index('>') + 1
            else:
                tag_end = html[i:].index('>')
                tag_name = html[i+1:i+tag_end]
                if not tag_name.replace('-', '', 1).isalnum() or tag_name[0].isdigit():
                    return False
                stack.append(tag_name)
                i += tag_end + 1
        i += 1
    return not stack