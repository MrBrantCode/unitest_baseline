"""
QUESTION:
Implement a function `parse_syntax` that takes a string representing a custom language syntax as input, where operations are denoted by `op` followed by parentheses containing the operation's arguments, names are denoted by `name` followed by a string literal, newline tokens are denoted by `nl`, and string literals are denoted by `string`. All components are separated by pipes and commas. The function should return a dictionary containing the extracted information with the following keys: `operations`, a list of all operations; `names`, a list of all names; `newlines`, a count of newline tokens; and `strings`, a list of all string literals. Assume the input syntax is well-formed and follows the specified syntax rules.
"""

import re

def parse_syntax(syntax):
    operations = re.findall(r'op\|\'([^\']*)\'', syntax)
    names = re.findall(r'name\|\'([^\']*)\'', syntax)
    newlines = syntax.count('nl|\'\\n\'')
    strings = re.findall(r'string\|\'([^\']*)\'', syntax)
    
    return {
        "operations": operations,
        "names": names,
        "newlines": newlines,
        "strings": strings
    }