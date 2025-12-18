"""
QUESTION:
Implement a function `isValidHTMLTag(tag)` that takes a string `tag` as input and returns `True` if the tag is a valid HTML tag, and `False` otherwise. A valid HTML tag is either an opening tag that starts with `<` followed by a tag name and ends with `>`, or a closing tag that starts with `</` followed by the tag name and ends with `>`. The tag name can contain lowercase and uppercase letters, numbers, and hyphens, but it cannot start with a number.
"""

def entrance(tag):
    if tag.startswith("</") and tag.endswith(">"):
        tag_name = tag[2:-1]
        if tag_name[0].isalpha() and all(char.isalnum() or char == '-' for char in tag_name):
            return True
    elif tag.startswith("<") and tag.endswith(">"):
        tag_name = tag[1:-1]
        if tag_name[0].isalpha() and all(char.isalnum() or char == '-' for char in tag_name):
            return True
    return False