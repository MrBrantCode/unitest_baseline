"""
QUESTION:
Write a function `extract_substrings` that takes a string `text` as input. The function should extract substrings enclosed within square brackets `[ ]` and return them in the sequence of their appearance. It should handle nested square brackets, special typographic symbols, unbalanced brackets, empty strings, and strings without brackets. If the input is not a string, is empty, or contains unbalanced brackets, or if no substrings are found within brackets, the function should return an error message.
"""

def extract_substrings(text):
    if not isinstance(text, str):
        return 'Error: Input must be a string'
    elif text == '':
        return 'Error: Empty string'

    stack = []
    result = []
    for i, c in enumerate(text):
        if c == '[':
            stack.append(i)
        elif c == ']':
            if len(stack) == 0:
                return 'Error: Unbalanced brackets'
            else:
                start = stack.pop()
                if len(stack) == 0: 
                    result.append(text[start + 1:i])
    if len(stack) != 0:
        return 'Error: Unbalanced brackets'

    if len(result) == 0:
        return 'Error: No substrings found within brackets'
    else:
        return result