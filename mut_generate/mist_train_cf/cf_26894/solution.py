"""
QUESTION:
Write a function `parse_arguments(args: str) -> dict` that takes a string of command-line arguments in the format "--parameter value" and returns a dictionary containing the parameter names as keys and their corresponding values as values. The values for "eval_episodes" and "seed" should be converted to integers.
"""

import re

def parse_arguments(args: str) -> dict:
    arg_pattern = r"--(\w+)\s+([^\s]+)"
    matches = re.findall(arg_pattern, args)
    parsed_args = {}
    for match in matches:
        key = match[0]
        value = match[1]
        if key == "eval_episodes" or key == "seed":
            value = int(value)
        parsed_args[key] = value
    return parsed_args