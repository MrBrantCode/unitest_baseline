"""
QUESTION:
Write a function `extract_substrings(text)` that takes a string `text` as input and returns a tuple containing a status message and a list of substrings enclosed within round brackets in the order of their occurrence. The function should be able to handle hierarchically nested round brackets, special typographic symbols, escape sequences for brackets, unbalanced brackets, and empty strings.
"""

def extract_substrings(text):
    stack = []
    result = []
    escape = False
    for i, char in enumerate(text):
        if char == '\\' and not escape:
            escape = True
            continue
        if char == '(' and not escape:
            stack.append(i)
        elif char == ')' and not escape:
            if len(stack) == 0:
                return "Error: Unbalanced brackets.", []
            else:
                start = stack.pop()
                if len(stack) == 0: 
                    result.append(text[start+1:i])

        if escape:
            escape = False
    if len(stack) != 0:
        return "Error: Unbalanced brackets.", []
    return "Success", result