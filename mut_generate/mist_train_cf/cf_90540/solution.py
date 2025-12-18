"""
QUESTION:
Implement the function `remove_duplicates(input_string)` that takes a string of lowercase alphabets and spaces as input, and returns the string with all duplicate words removed. The function should have a time complexity of O(n), where n is the length of the string, and should not use any additional memory apart from a constant amount of space, nor any built-in functions or data structures for storing intermediate results.
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