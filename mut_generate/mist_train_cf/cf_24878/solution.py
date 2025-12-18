"""
QUESTION:
Write a function `delete_comments` that takes a string as input and returns a new string where all comments starting with '#' are removed. A comment is considered to start from the '#' symbol and continues until the end of the line.
"""

def delete_comments(input_str):
    return '\n'.join([line.split('#')[0].rstrip() for line in input_str.split('\n')])