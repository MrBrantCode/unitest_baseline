"""
QUESTION:
Create a function `countNestedElements(html)` that takes a well-formed HTML string `html` as input and returns the maximum nesting level of HTML elements. The HTML string does not contain any inline JavaScript or CSS, and each element is defined as any tag enclosed within angle brackets.
"""

def maxNestingLevel(html):
    stack = []
    count = 0
    i = 0
    while i < len(html):
        if html[i] == '<':
            if html[i+1] != '/':
                stack.append(html[i:i+html[i:].index('>')+1])
            else:
                stack.pop()
                count = max(count, len(stack))
        i += 1
    return count