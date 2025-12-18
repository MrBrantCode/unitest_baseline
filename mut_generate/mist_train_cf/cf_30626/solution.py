"""
QUESTION:
You are tasked with implementing a function `countNestedElements` that takes a string `htmlCode` as input and returns the count of nested HTML elements, considering only the opening tags of HTML elements and ignoring any attributes or closing tags. The function should parse the given HTML code snippet and return the total count of nested HTML elements. The HTML code snippet is guaranteed to be well-formed.
"""

def countNestedElements(htmlCode: str) -> int:
    count = 0
    stack = []
    i = 0
    while i < len(htmlCode):
        if htmlCode[i] == '<':
            j = i + 1
            while j < len(htmlCode) and htmlCode[j] != '>':
                j += 1
            if j < len(htmlCode) and htmlCode[i + 1] != '/':
                tag = htmlCode[i + 1:j]
                stack.append(tag)
                count += 1
            elif j < len(htmlCode) and htmlCode[i + 1] == '/':
                stack.pop()
            i = j
        else:
            i += 1
    return count