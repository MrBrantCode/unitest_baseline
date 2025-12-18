"""
QUESTION:
Create a function `htmlTagChecker` that takes a string representing an HTML file as input. The function should return `true` if all the opening tags have corresponding closing tags, and `false` otherwise, ignoring any self-closing tags and any tags that do not require a closing tag.
"""

def htmlTagChecker(html_string):
    stack = []
    i = 0
    while i < len(html_string):
        if html_string[i] == '<':
            if html_string[i:i+2] == '</':  
                tag_end = html_string.find('>', i)
                if tag_end == -1:
                    return False  
                closing_tag = html_string[i+2:tag_end]
                if stack and stack[-1] == closing_tag:
                    stack.pop()
                else:
                    return False  
                i = tag_end + 1
            else:  
                tag_end = html_string.find('>', i)
                if tag_end == -1:
                    return False  
                opening_tag = html_string[i+1:tag_end]
                if not opening_tag.endswith('/'):  
                    stack.append(opening_tag)
                i = tag_end + 1
        else:
            i += 1

    return len(stack) == 0 