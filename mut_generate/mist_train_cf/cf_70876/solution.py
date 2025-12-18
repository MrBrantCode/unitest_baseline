"""
QUESTION:
Write a function `extract_quoted` that extracts the innermost quoted value from a string, handling nested quotations. The function should take a string `s` as input and return the extracted quoted value. The input string is assumed to be well-formatted with balanced quotes.
"""

def extract_quoted(s):
    stack = []
    extracted = ''

    for char in s:
        if char == '"':
            if stack:
                extracted = ''.join(stack)
                stack = []
            else:
                continue
        if stack is not None:
            stack.append(char)

    return extracted