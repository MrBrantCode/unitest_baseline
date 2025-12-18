"""
QUESTION:
Write a function called `check_html_tags` to implement a simple HTML tag checker. The function should take a string of HTML code as input and return a boolean indicating whether all tags are properly closed. 

The function should be able to handle nested tags, and it should ignore self-closing tags, comments, and doctype declarations. It should also ignore any text outside of tags. 

Do not implement a full HTML parser; assume the input HTML code is mostly valid and does not contain any complex edge cases.
"""

def check_html_tags(html_code):
    """
    Checks if all HTML tags in the given code are properly closed.

    Args:
        html_code (str): A string of HTML code.

    Returns:
        bool: True if all tags are properly closed, False otherwise.
    """
    stack = []
    for i in range(len(html_code)):
        if html_code[i] == '<':
            if html_code[i + 1] == '/':
                j = html_code.find('>', i)
                if j == -1:
                    return False
                tag_name = html_code[i + 2:j]
                if not stack or stack.pop() != tag_name:
                    return False
            else:
                j = html_code.find('>', i)
                if j == -1:
                    return False
                tag_name = html_code[i + 1:j]
                if tag_name.endswith('/'):
                    continue
                stack.append(tag_name)
    return not stack