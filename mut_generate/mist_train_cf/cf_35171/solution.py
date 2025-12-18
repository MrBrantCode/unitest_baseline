"""
QUESTION:
Write a function `parseKeywords` that takes a code snippet as input and returns a dictionary where the keywords are the keys, and the associated tokens and syntax properties are the values. The code snippet is a string containing lines in the format `{"keyword", token, syntax_properties},` where token and syntax_properties are separated by commas and syntax_properties may contain bitwise OR operations. The function should ignore any empty lines or lines that do not match the specified format. Assume the input code snippet is well-formed and follows the same pattern as shown in the example.
"""

import re

def parseKeywords(code_snippet):
    keyword_pattern = r'{"(.*?)",\s+(T_\w+),\s+(SYNTAX_\w+(\s*\|\s*SYNTAX_\w+)*)}'
    matches = re.findall(keyword_pattern, code_snippet)

    keywords_map = {}
    for match in matches:
        keyword = match[0]
        token = match[1]
        syntax_properties = match[2]
        keywords_map[keyword] = {"token": token, "syntax_properties": syntax_properties}

    return keywords_map