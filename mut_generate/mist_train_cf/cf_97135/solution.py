"""
QUESTION:
Develop a function named `replace_consecutive_whitespaces` that takes a string as input, replaces all consecutive whitespaces with a single space, and ignores any whitespaces at the beginning or end of the string. The function must have a time complexity of O(n), where n is the length of the input string.
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