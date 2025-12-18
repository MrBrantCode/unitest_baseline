"""
QUESTION:
Write a function `generate_command_string(args)` that takes a dictionary `args` of command-line arguments and their values, and returns a string containing the formatted command-line arguments. The function should format boolean arguments without values and non-boolean arguments with their corresponding values. The output string should be in the format `--key1 value1 --key2 --key3 value3`, with no trailing whitespace.
"""

def generate_command_string(args):
    command_string = ""
    for key, value in args.items():
        if isinstance(value, bool):
            if value:
                command_string += f"--{key} "
        else:
            command_string += f"--{key} {value} "
    return command_string.strip()