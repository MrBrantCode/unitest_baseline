"""
QUESTION:
Write a function `remove_tags(html_string)` that takes a string of HTML tags as input, removes the HTML tags, and returns the plain text string. The function should handle nested tags and unclosed tags. Assume the HTML string is not malformed, with no occurrences of "><", "<<>>", lone ">" or "<".
"""

def remove_tags(html_string):
    result = ''
    stack = []
    for char in html_string:
        if char == '<':
            stack.append('<')
        elif char == '>':
            if stack:
                stack.pop()
        else:
            if not stack:
                result += char
    return result