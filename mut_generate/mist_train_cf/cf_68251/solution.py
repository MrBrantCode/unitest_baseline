"""
QUESTION:
Create a function called `extract_substrings` that takes a string `text` as input and returns a list of substrings enclosed within round brackets. The function should handle hierarchically nested brackets, special typographic symbols, and erroneous inputs such as unbalanced brackets, empty strings, and strings without brackets. If an error occurs, the function should return an error message instead of a list of substrings. The function should also exclude unprintable characters from the input string.
"""

def extract_substrings(text):
    stack = []
    result = []
    if not text:
        return "The string is empty"
    for char in text:
        if not char.isprintable():
            return "The string contains unprintable characters"
                
    for i, char in enumerate(text):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if len(stack) == 0:
                return "Unbalanced brackets error"
            else:
                start = stack.pop()
                result.append(text[start+1:i])
    if len(stack) > 0:
        return "Unbalanced brackets error"
           
    if len(result) == 0:
        return "No substrings were found in brackets"
    else:
        return result