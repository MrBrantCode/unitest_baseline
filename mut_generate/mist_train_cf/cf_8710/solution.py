"""
QUESTION:
Implement a function `remove_duplicates(input_string)` that takes a string of lowercase alphabets and spaces as input, removes all duplicated words within it, and returns the resulting string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any additional memory apart from a constant amount of space.
"""

def remove_duplicates(input_string):
    seen = ''
    result = ''
    for char in input_string:
        if char == ' ':
            if seen not in result:
                result += seen + ' '
            seen = ''
        else:
            seen += char
    if seen not in result:
        result += seen
    return result.rstrip()