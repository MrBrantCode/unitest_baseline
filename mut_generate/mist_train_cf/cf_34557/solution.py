"""
QUESTION:
Write a function `isProperlyNested(htmlCode: str) -> bool` that takes a string `htmlCode` representing the HTML code and returns `True` if all the HTML elements are properly nested, and `False` otherwise. The HTML elements are considered properly nested if every opening tag has a corresponding closing tag and they are properly nested within each other.
"""

def isProperlyNested(htmlCode: str) -> bool:
    stack = []
    i = 0
    while i < len(htmlCode):
        if htmlCode[i] == '<':
            if htmlCode[i+1] == '/':
                if len(stack) == 0:
                    return False  # Closing tag without corresponding opening tag
                else:
                    stack.pop()
                    i += 2  # Skip the tag name
            else:
                j = i + 1
                while htmlCode[j] != '>':
                    j += 1
                stack.append(htmlCode[i+1:j])
                i = j + 1
        else:
            i += 1
    return len(stack) == 0  # All opening tags have corresponding closing tags