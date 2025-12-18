"""
QUESTION:
Develop a function `replace_consecutive_whitespaces` that takes a string as input and returns a string where all consecutive whitespaces are replaced with a single space. The function should ignore any whitespaces at the beginning or end of the string and have a time complexity of O(n), where n is the length of the input string.
"""

def replace_consecutive_whitespaces(string):
    result = ""
    prev_char = None

    i = 0
    while i < len(string) and string[i].isspace():
        i += 1

    while i < len(string):
        if not string[i].isspace() or not prev_char.isspace():
            result += string[i]
        prev_char = string[i]
        i += 1

    while result and result[-1].isspace():
        result = result[:-1]

    return result