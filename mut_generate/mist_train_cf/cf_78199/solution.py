"""
QUESTION:
Design a function `convert_to_snake_case` that takes a string `s` as input and returns the string converted to snake case notation. The function should insert an underscore before each uppercase letter in the string and convert all characters to lowercase. If the resulting string starts with an underscore, it should be removed.
"""

def convert_to_snake_case(s):
    return ''.join(['_' + i.lower() if i.isupper() else i for i in s]).lstrip('_')