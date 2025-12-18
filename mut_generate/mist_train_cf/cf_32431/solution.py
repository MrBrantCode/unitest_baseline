"""
QUESTION:
Implement a function `generate_help_message(options)` that takes a dictionary `options` as input, where each key is an option name and each value is another dictionary containing the keys 'help' (a string describing the option), 'def' (the default value for the option), and 'des' (a short name or description for the option). The function should return a formatted help message including the option name, its default value, and the description in a user-friendly format.
"""

def generate_help_message(options):
    help_message = "Options:\n"
    for option, details in options.items():
        help_message += f"- {option}: {details['des']}, Default: {details['def']}\n"
    return help_message