"""
QUESTION:
Create a function called `parse_command_line_arguments` that takes a string of command-line arguments as input and returns a dictionary of extracted key-value pairs. The input string is formatted as `--<parameter_name>=<value>`, where each parameter name and value is separated by an equals sign and enclosed in double quotes. The function should extract the parameter names and values, and return them as a dictionary where each key is a parameter name and each value is the corresponding parameter value.
"""

import re

def parse_command_line_arguments(args_str):
    args_dict = {}
    pattern = r'--(\w+\.\w+)="([^"]+)"'
    matches = re.findall(pattern, args_str)
    for match in matches:
        args_dict[match[0]] = match[1]
    return args_dict