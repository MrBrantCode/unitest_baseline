"""
QUESTION:
Write a Python function named `split_string_with_nested_delimiters` that takes two parameters: a string and a delimiter. The function should split the string into a list of strings separated by the given delimiter, handling multiple nested delimiters enclosed within matching parentheses, square brackets, or curly braces. It should split the string at the outer delimiter while ignoring any occurrences of the delimiter within nested delimiters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def split_string_with_nested_delimiters(string, delimiter):
    result = []
    stack = []
    current = ''
    
    for char in string:
        if char == delimiter and not stack:
            result.append(current)
            current = ''
        else:
            current += char
            if char in '([{':
                stack.append(char)
            elif char in ')]}' and stack:
                if (char == ')' and stack[-1] == '(') or \
                   (char == ']' and stack[-1] == '[') or \
                   (char == '}' and stack[-1] == '{'):
                    stack.pop()
    
    result.append(current)
    return result