"""
QUESTION:
Write a function `isHTMLProperlyClosed(htmlCode: str) -> bool` that takes a string `htmlCode` as input and returns true if the HTML tags are properly closed and nested, and false if they are not. The function should only consider opening and closing tags for div elements, and the input HTML code may have varying indentation and spacing but proper tag alignment.
"""

def isHTMLProperlyClosed(htmlCode: str) -> bool:
    stack = []
    for line in htmlCode.replace(" ", "").split('\n'):
        line = line.strip()
        if line.startswith('</'):
            if not stack or stack[-1] != line:
                return False
            stack.pop()
        elif line.startswith('<div'):
            stack.append('</div>')
    return len(stack) == 0