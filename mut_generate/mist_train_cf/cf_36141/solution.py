"""
QUESTION:
Implement a function `parseCommandLine` that takes a string representing the command line input and returns a dictionary containing the parsed options and their values. The input string consists of space-separated tokens representing options and their values. Options can be specified using either a short form (e.g., `-f`) or a long form (e.g., `--file`), and their values can be provided immediately after the option or as the next token, separated by a space or an equals sign. The function should return a dictionary where the keys are the option names (without the dashes) and the values are the corresponding option values.
"""

def parseCommandLine(input_str: str) -> dict:
    options = {}
    tokens = input_str.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.startswith("--"):
            option, value = token[2:], None
            if "=" in option:
                option, value = option.split("=")
            else:
                i += 1
                if i < len(tokens) and not tokens[i].startswith("-"):
                    value = tokens[i]
            options[option] = value
        elif token.startswith("-"):
            option, value = token[1:], None
            if len(token) > 2:
                value = token[2:]
            else:
                i += 1
                if i < len(tokens) and not tokens[i].startswith("-"):
                    value = tokens[i]
            options[option] = value
        i += 1
    return options