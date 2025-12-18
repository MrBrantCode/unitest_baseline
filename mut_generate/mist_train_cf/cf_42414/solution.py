"""
QUESTION:
Write a function `isProperlyStructuredHTML(html)` that takes a string `html` representing an HTML document without attributes or self-closing tags and returns `true` if the document is properly structured (i.e., all tags are properly nested and closed in the correct order) and `false` otherwise.
"""

def isProperlyStructuredHTML(html):
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            if html[i+1] == '/':
                if len(stack) == 0:
                    return False  
                if stack[-1] != html[i+2:i+html[i:].find('>')]:
                    return False  
                stack.pop()
                i += html[i:].find('>')  
            else:
                stack.append(html[i+1:i+html[i:].find('>')])  
                i += html[i:].find('>')  
        i += 1
    return len(stack) == 0  