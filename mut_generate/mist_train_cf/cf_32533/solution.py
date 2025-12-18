"""
QUESTION:
Implement a function `parse_arguments` that takes a list of strings representing command-line arguments as input and returns a dictionary containing the parsed key-value pairs. Each key is preceded by two dashes (--), and the value can be an alphanumeric string, integer, or boolean value (True or False). If a key is followed by a backslash (\), the value continues on the next line. If a key does not have a specified value, it should be treated as a boolean flag with an empty string value.
"""

def parse_arguments(args):
    parsed_args = {}
    current_key = None
    for arg in args:
        if arg.startswith("--"):
            current_key = arg[2:]
            parsed_args[current_key] = ""
        elif current_key is not None:
            if arg.endswith("\\"):
                parsed_args[current_key] += arg[:-1] + " "
            else:
                parsed_args[current_key] += arg
                current_key = None
    return parsed_args