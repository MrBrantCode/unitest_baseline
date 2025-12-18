"""
QUESTION:
Implement a function named `parse_arguments` that takes a list of strings representing command-line arguments as input and returns a dictionary containing the parsed arguments. The function should handle both short and long options, as well as their corresponding values. For options without values, the dictionary should contain the option as the key and the value `True`. For option-value pairs, the dictionary should contain the option as the key and the corresponding value as the value.
"""

def parse_arguments(args):
    parsed_args = {}
    i = 0
    while i < len(args):
        if args[i].startswith('-'):
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                parsed_args[args[i]] = args[i + 1]
                i += 2
            else:
                parsed_args[args[i]] = True
                i += 1
        else:
            i += 1
    return parsed_args