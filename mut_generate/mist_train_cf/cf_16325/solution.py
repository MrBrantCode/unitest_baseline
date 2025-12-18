"""
QUESTION:
Write a function `split_string` that takes a string and a delimiter as input and splits the string into a list of strings, separated by the given delimiter. The function should handle nested delimiters, where a nested delimiter is defined as a delimiter that is enclosed within a pair of matching parentheses. The function should split the string at the outer delimiter, while ignoring any occurrences of the delimiter within nested delimiters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def split_string(s, delimiter):
    result = []
    count = 0
    start = 0

    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1

        if count == 0 and s[i:i+len(delimiter)] == delimiter:
            result.append(s[start:i])
            start = i + len(delimiter)

    result.append(s[start:])

    return result