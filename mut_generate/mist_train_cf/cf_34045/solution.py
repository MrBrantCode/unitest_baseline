"""
QUESTION:
Implement the `is_valid_closing_tag` function, which checks whether a given string contains a valid HTML closing tag that matches the corresponding opening tag. The function should take two parameters: `tag` (the closing tag to be checked) and `opening_tag` (the corresponding opening tag). The function should return `True` if the closing tag is valid and matches the opening tag, and `False` otherwise. A valid closing tag must start with "</" followed by a tag name consisting of only lowercase letters and hyphens, and end with ">". The tag name should match the opening tag it is closing.
"""

def is_valid_closing_tag(tag: str, opening_tag: str) -> bool:
    if tag[:2] != "</" or tag[-1] != ">":
        return False
    closing_tag_name = tag[2:-1]
    opening_tag_name = opening_tag[1:-1]
    return closing_tag_name == opening_tag_name