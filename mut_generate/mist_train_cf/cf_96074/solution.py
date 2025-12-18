"""
QUESTION:
Write a function `split_string_with_quotes(string, delimiter)` that splits a string by a specific delimiter while ignoring any delimiter that appears within double quotes in the string, including cases where the double quotes are not properly closed. The function should return a list of substrings split by the delimiter.
"""

def split_string_with_quotes(string, delimiter):
    result = []
    stack = []
    start = 0

    for i in range(len(string)):
        if string[i] == '"':
            if stack and stack[-1] == i - 1:
                stack.pop()
            else:
                stack.append(i)
        elif string[i] == delimiter and not stack:
            result.append(string[start:i])
            start = i + 1

    result.append(string[start:])

    return result