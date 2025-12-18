"""
QUESTION:
Write a function `format_json(json_str)` that reformats a given JSON string into properly indented and formatted output with a time complexity of O(n), where n is the length of the input string. The function should handle nested objects and arrays, and the output should have four spaces for each indentation level.
"""

def format_json(json_str):
    formatted_output = ''
    indent = 0

    for c in json_str:
        if c == '{' or c == '[':
            formatted_output += c
            formatted_output += '\n'
            indent += 1
            formatted_output += '    ' * indent
        elif c == '}' or c == ']':
            indent -= 1
            formatted_output += '\n'
            formatted_output += '    ' * indent
            formatted_output += c
        elif c == ',':
            formatted_output += c
            formatted_output += '\n'
            formatted_output += '    ' * indent
        elif c == ':':
            formatted_output += c
            formatted_output += ' '
        else:
            formatted_output += c

    return formatted_output