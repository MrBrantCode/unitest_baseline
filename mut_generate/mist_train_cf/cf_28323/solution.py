"""
QUESTION:
Implement a function `countValidHTMLTags` that takes a string `htmlString` as input and returns the count of valid HTML tags found within the string. A valid HTML tag is defined as an opening tag enclosed within angle brackets, containing alphanumeric characters, hyphens, and underscores, but no spaces or special characters. Opening and closing tags must match, and nested tags should be properly closed. The function should ignore HTML attributes.
"""

def countValidHTMLTags(htmlString):
    stack = []
    count = 0
    i = 0
    while i < len(htmlString):
        if htmlString[i] == '<':
            tag = ""
            i += 1
            while i < len(htmlString) and htmlString[i] != '>':
                tag += htmlString[i]
                i += 1
            if tag and tag[0] != '/':
                stack.append(tag)
            elif tag and tag[0] == '/':
                if stack and stack[-1] == tag[1:]:
                    stack.pop()
                    count += 1
            i += 1
        else:
            i += 1
    return count