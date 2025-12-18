"""
QUESTION:
Write a function `generate_installation_arguments(config_options: dict) -> str` to generate a formatted string of command-line arguments from a dictionary of configuration options. The function should include each option on a new line, prefixing each flag with '-D' and appending '=1' for boolean options that are True, and '=' followed by the value for string options. 

The input dictionary `config_options` contains configuration options as keys and their corresponding values as values. The keys are strings representing the flags, and the values are either booleans or strings. The length of `config_options` is between 1 and 100, inclusive.
"""

def generate_installation_arguments(config_options: dict) -> str:
    arguments = []
    for option, value in config_options.items():
        if isinstance(value, bool) and value:
            arguments.append(f"-D{option}=1")
        elif isinstance(value, str):
            arguments.append(f"-D{option}={value}")
    return '\n'.join(arguments)