"""
QUESTION:
Write a function called `split_string` that takes two parameters: `string` and `delimiter`. The function should split the input `string` into a list of strings separated by the `delimiter`, while ignoring any occurrences of the `delimiter` within nested parentheses. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def split_string(string, delimiter):
    result = []
    count = 0
    start = 0

    for i in range(len(string)):
        if string[i] == '(':
            count += 1
        elif string[i] == ')':
            count -= 1

        if count == 0 and string[i:i+len(delimiter)] == delimiter:
            result.append(string[start:i])
            start = i + len(delimiter)

    result.append(string[start:])

    return result