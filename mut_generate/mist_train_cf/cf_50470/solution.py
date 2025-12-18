"""
QUESTION:
Create a function called `isValid` that takes a string `code` as input and returns `True` if the code is valid according to the following rules:

* The code must be encapsulated within a valid closed tag.
* A closed tag must be in the format `<TAG_NAME>TAG_CONTENT</TAG_NAME>`, where `TAG_NAME` is the same in the opening and closing tags.
* A valid `TAG_NAME` can only contain upper-case letters and its length must be between 1 and 9.
* A valid `TAG_CONTENT` can contain other valid closed tags, CDATA, and any characters except unmatched `<`, unmatched opening and closing tags, and unmatched or closed tags with invalid `TAG_NAME`.
* An opening tag is considered unmatched if there is no corresponding closing tag with the same `TAG_NAME`, and vice versa.
* A `<` is considered unmatched if there is no subsequent `>`.
* CDATA must be in the format `<![CDATA[CDATA_CONTENT]]>`, and `CDATA_CONTENT` can contain any characters.

The input code only contains letters, digits, `<`, `>`, `/`, `!`, `[`, `]`, and ` `.
"""

def isValid(code):
    stack = []
    i = 0
    while i < len(code):
        if code[i] == '<':
            if i + 1 < len(code) and code[i + 1] == '!':
                j = code.find(']]>', i)
                if j == -1: 
                    return False
                i = j + 2
            elif i + 1 < len(code) and code[i + 1] == '/':
                j = code.find('>', i)
                if j == -1: 
                    return False
                tag_name = code[i + 2:j]
                if not tag_name.isupper() or len(tag_name) < 1 or len(tag_name) > 9:
                    return False
                if not stack or stack.pop() != tag_name: 
                    return False
                i = j + 1
            else:
                j = code.find('>', i)
                if j == -1: 
                    return False
                tag_name = code[i + 1:j]
                if not tag_name.isupper() or len(tag_name) < 1 or len(tag_name) > 9:
                    return False
                stack.append(tag_name)
                i = j + 1
        else:
            i += 1
    return not stack